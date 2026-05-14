import os
import logging
import numpy as np
from pathlib import Path
from dataclasses import dataclass, asdict, field, fields

# example usage
# params = CSSParameters(force_eman=True)
# params.CSS_mbin_reextract_mics_0o95box
# getattr(params, "CSS_mbin_reextract_mics_0o95box", "default value")

logger = logging.getLogger("CSSParameters")

@dataclass
class CSSParameters: 
    ##### Microscope related inputs #####
    # from config_em_settings.yaml
    EM_mics_apix: float|None = None
    # EM_kV       : int  |None = None
    # EM_Cs       : float|None = None

    # defocus     : float|None = None

    # micrograph size
    mics_upper_bound: int|None = None # = micrograph size
    mics_lower_bound: int = 0

    ##### User provided inputs #####
    # reference map and mask
    ref3d_path : str = "Not Provided"
    mask3d_path: str = "Not Provided"

    # binning factors
    large_binning_factor : float = 1.0
    medium_binning_factor: float = 1.0

    # mask padding (only one should be provided)
    padding_pixels    : int   = 0
    padding_angstrom  : float = 0.0
    padding_percentage: float = 0.0

    # from analysis scripts
    reference_particle_size_pix   : int   = 0
    reference_particle_size_angpix: float = 0.0

    initial3d_particle_size_pix   : int   = 0
    initial3d_particle_size_angpix: float = 0.0

    ctflimit_boxsize_pix   : int   = 0
    ctflimit_boxsize_angpix: float = 0.0

    ##### Options #####
    use_eman_boxsizes : bool = True

    ##### Extras #####
    fresnel_boxsize : float|None = None

    def __post_init__(self):
        # todo: complete the other validation
        # note: validation is informed via logging; it is NOT asserted
        self.validate_padding()

    ##### Common 
    @property
    def SS_comm_class2d_pmd(self):
        # voxels
        result  = self.reference_particle_size_pix
        result += self.padding_pixels

        # convert to angstrom
        result *= self.reference_particle_size_angpix
        result += self.padding_pixels

        # percentage padding
        result *= (1.0+self.padding_percentage)

        return int(np.ceil(result))
    
    @property
    def SS_comm_optimal_pmd(self):
        result = self.initial3d_particle_size_pix * self.initial3d_particle_size_angpix
        return int(np.ceil(result))

    @property
    def SS_comm_lbin_angpix(self):
        return self.EM_mics_apix * self.large_binning_factor

    @property
    def SS_comm_lbin_ref3d_path(self):
        return self.ref3d_path    
    
    @property
    def SS_comm_lbin_mask3d_path(self):
        return self.mask3d_path
    
    @property
    def SS_comm_lbin_ref3d_name(self):
        return Path(self.SS_comm_lbin_ref3d_path).name

    @property
    def SS_comm_lbin_mask3d_name(self):
        return Path(self.SS_comm_lbin_mask3d_path).name

    @property
    def SS_comm_mbin_angpix(self):
        return self.EM_mics_apix * self.medium_binning_factor

    ##### 030_GTF_Create_Stack #####
    @property
    def GTF_lbin_extract_mics_box(self):
        # convert to angstrom
        boxsize_A = self.ctflimit_boxsize_pix        * self.ctflimit_boxsize_angpix
        psize_A   = self.initial3d_particle_size_pix * self.initial3d_particle_size_angpix

        # get the biggest in pixel (comparison in angstrom)
        if boxsize_A >= psize_A:
            result = adjust_boxsize(self.ctflimit_boxsize_pix, self.use_eman_boxsizes)
        else:
            result = self.initial3d_particle_size_pix / 0.95

        return result

    @property
    def GTF_lbin_extract_mics_0o95box(self):
        result = self.GTF_lbin_extract_mics_box * 0.95
        return adjust_boxsize(result, self.use_eman_boxsizes)

    @property
    def GTF_lbin_extract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.GTF_lbin_extract_mics_box, 
                                           binned_pixelsize=self.SS_comm_lbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.use_eman_boxsizes)

    @property
    def GTF_lbin_extract_parts_x_min(self):
        result = compute_extract_coordinates_min(boxsize=self.GTF_lbin_extract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return result

    @property
    def GTF_lbin_extract_parts_x_max(self):
        result = compute_extract_coordinates_max(boxsize=self.GTF_lbin_extract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return result

    @property
    def GTF_lbin_extract_parts_y_min(self):
        result = compute_extract_coordinates_min(boxsize=self.GTF_lbin_extract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return result

    @property
    def GTF_lbin_extract_parts_y_max(self):
        result = compute_extract_coordinates_max(boxsize=self.GTF_lbin_extract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return result

    ##### 050_GTF_AbInitReconst3D #####
    @property
    def GTF_lbin_abinit3d_pmd(self):
        return "Not Implemented"

    ##### 070_CSS_Init_Refine3D #####
    @property
    def CSS_mbin_reextract_mics_box(self):
        return "Not Implemented"
        
    @property
    def CSS_mbin_reextract_mics_0o95box(self):
        result = self.CSS_mbin_reextract_mics_box * 0.95
        return adjust_boxsize(result, self.use_eman_boxsizes)

    @property
    def CSS_mbin_reextract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.CSS_mbin_reextract_mics_box, 
                                           binned_pixelsize=self.SS_comm_mbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.use_eman_boxsizes)

    @property
    def CSS_mbin_reextract_parts_x_min(self):
        result = compute_extract_coordinates_min(boxsize=self.CSS_mbin_reextract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return result

    @property
    def CSS_mbin_reextract_parts_x_max(self):
        result = compute_extract_coordinates_max(boxsize=self.CSS_mbin_reextract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return result
    
    @property
    def CSS_mbin_reextract_parts_y_min(self): 
        result = compute_extract_coordinates_min(boxsize=self.CSS_mbin_reextract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return result

    @property
    def CSS_mbin_reextract_parts_y_max(self):
        result = compute_extract_coordinates_max(boxsize=self.CSS_mbin_reextract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return result

    ### auxiliary methods ###
    def to_dict(self, parameters_of_interest):
        return {poi:getattr(self, poi) for poi in parameters_of_interest}

    @classmethod
    def get_valid_fields(cls):
        return {f.name for f in fields(cls)}

    ### validation methods ###
    def validate_padding(self):
        cond_a = self.padding_pixels     > 0
        cond_b = self.padding_angstrom   > 0
        cond_c = self.padding_percentage > 0
        if sum([cond_a, cond_b, cond_c])>=2:
            logger.warning("PADDING: More than one option provided!")
            logger.warning(f"PADDING: + padding_pixels     = {self.padding_pixels}")
            logger.warning(f"PADDING: + padding_angstrom   = {self.padding_angstrom}")
            logger.warning(f"PADDING: + padding_percentage = {self.padding_percentage}")

        cond_a = self.padding_pixels     == 0
        cond_b = self.padding_angstrom   == 0
        cond_c = self.padding_percentage == 0
        if cond_a and cond_b and cond_c:
            logger.warning("PADDING: No padding provided! To pad, set one of these variables: ")
            logger.warning("PADDING: + padding_pixels")
            logger.warning("PADDING: + padding_angstrom")
            logger.warning("PADDING: + padding_percentage")
        
        return


### css parameter calculation
def compute_extract_coordinates_min(boxsize, lower_bound=0):
    return int(lower_bound + (boxsize // 2))

def compute_extract_coordinates_max(boxsize, upper_bound):
    return int(upper_bound - (boxsize // 2))

def compute_extract_parts_box(boxsize, binned_pixelsize, micrograph_pixelsize):
    return boxsize / (binned_pixelsize / micrograph_pixelsize)

def adjust_boxsize(n, use_eman_boxsizes=False):
    if use_eman_boxsizes:
        return get_next_eman_boxsize(n)
    # if use_xxx_values:
    #   return xxx(n)
    return n

### general
def get_next_eman_boxsize(n):
    """
    Return the smallest element in the list that is ≥ than the input boxsize
    """
    boxsize_list = np.array([24, 32, 36, 40, 44, 48, 52, 56, 60, 64,
                                72, 84, 96, 100, 104, 112, 120, 128, 132, 140,
                                168, 180, 192, 196, 208, 216, 220, 224, 240, 256,
                                260, 288, 300, 320, 352, 360, 384, 416, 440, 448,
                                480, 512, 540, 560, 576, 588, 600, 630, 640, 648,
                                672, 686, 700, 720, 750, 756, 768, 784, 800, 810,
                                840, 864, 882, 896, 900, 960, 972, 980, 1000, 1008, 
                                1024, 
                                # values below are not empirically tested
                                1050, 1080, 1120, 1134, 1152, 1176, 1200, 1250, 1260,
                                1280, 1296, 1344, 1350, 1372, 1400, 1440, 1458, 1470,
                                1500, 1512, 1536, 1568, 1600, 1620, 1680, 1728, 1750,
                                1764, 1792, 1800, 1890, 1920, 1944, 1960, 2000, 2016,
                                2048, 2058, 2100, 2160, 2240, 2250, 2268, 2304, 2352,
                                2400, 2430, 2450, 2500, 2520, 2560, 2592, 2646, 2688,
                                2700, 2744, 2800, 2880, 2916, 2940, 3000, 3024, 3072,
                                3136, 3150, 3200, 3240, 3360, 3402, 3430, 3456, 3500,
                                3528, 3584, 3600, 3750, 3780, 3840, 3888, 3920, 4000,
                                4032, 4050, 4096 
    ]) # from: https://blake.bcm.edu/emanwiki/EMAN2/BoxSize
    

    result = n

    mask = (result <= boxsize_list)
    if sum(mask) > 0:
        result = boxsize_list[mask].min()
    
    return result

def get_pixel_size(voxel_size):
    return voxel_size[0] if isinstance(voxel_size, list) else voxel_size

