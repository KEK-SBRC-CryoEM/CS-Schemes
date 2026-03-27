import numpy as np
from dataclasses import dataclass, asdict, field, fields

# example usage
# params = CSSParameters(force_eman=True)
# params.CSS_mbin_reextract_mics_0o95box
# getattr(params, "CSS_mbin_reextract_mics_0o95box", "default value")

@dataclass
class CSSParameters: 
    # consider adding metadata to the fields

    ##### Inputs #####
    EM_mics_apix        : float
    SS_comm_lbin_angpix : float
    SS_comm_mbin_angpix : float
    GTF_lbin_abinit3d_pmd_increase_percentage: float

    particle_contour_radius    : float
    particle_contour_pixelsize : float

    negative_density_region_radius    : float
    negative_density_region_pixelsize : float

    fresnel_boxsize : float

    ##### Temporary input (later: calculate from micrograph) #####
    mics_upper_bound : int # = micrograph size
    mics_lower_bound : int = 0
    
    ##### Options #####
    boxsize_eman_values : bool = True
    # boxsize_optimal_FFT : bool = False # not used
    # boxsize_prime: bool = True # not used
    # boxsize_even : bool = True # not used

    def __post_init__(self):
        pass

    ##### Common 
    @property
    def SS_comm_class2d_pmd(self):
        # adjust boxsize
        boxsize = adjust_boxsize(self.particle_contour_radius*2, self.boxsize_eman_values) # [pixel]
        
        # convert to A
        particle_diameter = boxsize * get_pixel_size(self.particle_contour_pixelsize) # [angstrom]
        
        return particle_diameter
    
    @property
    def SS_comm_optimal_pmd(self):
        # adjust boxsize
        boxsize = adjust_boxsize(self.negative_density_region_radius*2) # [pixel]
        
        # convert to A
        particle_diameter = boxsize * get_pixel_size(self.negative_density_region_pixelsize) # [angstrom]
        
        return particle_diameter

    ##### 030_GTF_Create_Stack #####
    @property
    def GTF_lbin_extract_mics_box(self):
        # convert real-space box to pixels
        fresnel_boxpix = self.fresnel_boxsize/self.SS_comm_lbin_angpix

        # adjust boxsize
        fresnel  = adjust_boxsize(fresnel_boxpix, self.boxsize_eman_values)
        negative = adjust_boxsize(self.negative_density_region_radius*2, self.boxsize_eman_values)

        # choose bigger box
        return max(fresnel, negative)

    @property
    def GTF_lbin_extract_mics_0o95box(self):
        result = self.GTF_lbin_extract_mics_box * 0.95
        return adjust_boxsize(result, self.boxsize_eman_values)

    @property
    def GTF_lbin_extract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.GTF_lbin_extract_mics_box, 
                                           binned_pixelsize=self.SS_comm_lbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.boxsize_eman_values)

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
    def GTF_lbin_abinit3d_pmd(self): # todo
        # input percentage: Fixed size - factor of 1.1 or 1.2 - or  1pixel or 5 pixels - or user input
        return self.GTF_lbin_abinit3d_pmd_increase_percentage * self.SS_comm_class2d_pmd

    ##### 070_CSS_Init_Refine3D #####
    @property
    def CSS_mbin_reextract_mics_box(self):
        # convert real-space box to pixels
        fresnel_boxpix = self.fresnel_boxsize/self.SS_comm_mbin_angpix
        
        # adjust boxsize   
        fresnel  = adjust_boxsize(fresnel_boxpix, self.boxsize_eman_values)
        negative = adjust_boxsize(self.negative_density_region_radius*2, self.boxsize_eman_values)

        # choose bigger box
        return max(fresnel, negative)
        
    @property
    def CSS_mbin_reextract_mics_0o95box(self):
        result = self.CSS_mbin_reextract_mics_box * 0.95
        return adjust_boxsize(result, self.boxsize_eman_values)

    @property
    def CSS_mbin_reextract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.CSS_mbin_reextract_mics_box, 
                                           binned_pixelsize=self.SS_comm_mbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.boxsize_eman_values)

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

    def to_dict(self, parameters_of_interest):
        return {poi:getattr(self, poi) for poi in parameters_of_interest}

    @classmethod
    def get_valid_fields(cls):
        return {f.name for f in fields(cls)}

### css parameter calculation
def compute_extract_coordinates_min(boxsize, lower_bound=0):
    return int(lower_bound + (boxsize // 2))

def compute_extract_coordinates_max(boxsize, upper_bound):
    return int(upper_bound - (boxsize // 2))

def compute_extract_parts_box(boxsize, binned_pixelsize, micrograph_pixelsize):
    return boxsize / (binned_pixelsize / micrograph_pixelsize)

def adjust_boxsize(n, use_eman_values=False):
    if use_eman_values:
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

