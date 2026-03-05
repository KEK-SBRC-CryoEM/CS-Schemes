import numpy as np 
from dataclasses import dataclass, asdict, fields

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

    particle_contour_radius        : float
    negative_density_region_radius : float
    fresnel_boxsize : float

    ##### Temporary input (later: calculate from micrograph) #####
    mics_upper_bound : int # = micrograph size
    mics_lower_bound : int = 0
    
    ##### Options #####
    force_eman : bool = True
    force_prime: bool = True # not used yet
    force_even : bool = True # not used yet

    ##### Common 
    @property
    def SS_comm_class2d_pmd(self): # to test
        # todo: define in the input yaml that we want 'radius' from 'contour_size'
        # example inputs
        # radius = json.loads(analyses["contour_size"]["runtime"]["output"].stdout)["radius"] # [pixel]
        # apix   = analyses["parameters"]["EM_mics_apix"] # [angstrom/pixel]
        # compute_SS_comm_class2d_pmd(radius, apix)

        # adjust boxsize
        boxsize = adjust_boxsize(self.particle_contour_radius*2, force_eman=True) # [pixel]
        
        # convert to A
        particle_diameter = boxsize * self.EM_mics_apix # [angstrom] # todo: check if EM_mics_apix or from mrc file
        
        return particle_diameter # todo: due to pix multiplication, should it be converted to int?
    
    @property
    def SS_comm_optimal_pmd(self): # to test
        # adjust boxsize
        boxsize = adjust_boxsize(self.negative_density_region_radius*2, force_eman=True) # [pixel]
        
        # convert to A
        particle_diameter = boxsize * self.EM_mics_apix # [angstrom] # todo: check if EM_mics_apix or from mrc file
        
        return particle_diameter

    ##### 030_GTF_Create_Stack #####
    @property
    def GTF_lbin_extract_mics_box(self): # to test
        # todo: pixel size conversion?
        # todo: clarify about the inputs properly (pixel size for conversion)
        # example inputs
        # fresnel_boxsize = json.loads(analyses["fresnel"]["runtime"]["output"].stdout)["boxsize"]
        # neg_radius      = json.loads(analyses["negative_density"]["runtime"]["output"].stdout)["negative_radius"]
        # compute_GTF_lbin_extract_mics_box(fresnel_boxsize, neg_radius)

        # 1. adjust boxsize   
        fresnel  = adjust_boxsize(self.fresnel_boxsize, force_eman=True)
        negative = adjust_boxsize(self.negative_density_region_radius*2, force_eman=True)

        return max(fresnel, negative)

    @property
    def GTF_lbin_extract_mics_0o95box(self):
        result = self.GTF_lbin_extract_mics_box * 0.95
        return adjust_boxsize(result, self.force_eman)

    @property
    def GTF_lbin_extract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.GTF_lbin_extract_mics_box, 
                                           binned_pixelsize=self.SS_comm_lbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.force_eman)

    @property
    def GTF_lbin_extract_parts_x_min(self):
        result = compute_extract_coordinates_min(boxsize=self.GTF_lbin_extract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return adjust_boxsize(result, self.force_eman)

    @property
    def GTF_lbin_extract_parts_x_max(self):
        result = compute_extract_coordinates_max(boxsize=self.GTF_lbin_extract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return adjust_boxsize(result, self.force_eman)

    @property
    def GTF_lbin_extract_parts_y_min(self):
        result = compute_extract_coordinates_min(boxsize=self.GTF_lbin_extract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return adjust_boxsize(result, self.force_eman)

    @property
    def GTF_lbin_extract_parts_y_max(self):
        result = compute_extract_coordinates_max(boxsize=self.GTF_lbin_extract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return adjust_boxsize(result, self.force_eman)

    ##### 050_GTF_AbInitReconst3D #####
    @property
    def GTF_lbin_abinit3d_pmd(self): # todo
        # input percentage: Fixed size - factor of 1.1 or 1.2 - or  1pixel or 5 pixels - or user input
        return input_percentage * self.SS_comm_class2d_pmd

    ##### 070_CSS_Init_Refine3D #####
    @property
    def CSS_mbin_reextract_mics_box(self): # to test
        # todo: pixel size conversion?
        # same as GTF_lbin_extract_mics_box but different pixel size conversion
        # 1. adjust boxsize   
        fresnel  = adjust_boxsize(self.fresnel_boxsize, force_eman=True)
        negative = adjust_boxsize(self.negative_density_region_radius*2, force_eman=True)

        return max(fresnel, negative)
        
    @property
    def CSS_mbin_reextract_mics_0o95box(self):
        result = self.CSS_mbin_reextract_mics_box * 0.95
        return adjust_boxsize(result, self.force_eman)

    @property
    def CSS_mbin_reextract_parts_box(self):
        result = compute_extract_parts_box(boxsize=self.CSS_mbin_reextract_mics_box, 
                                           binned_pixelsize=self.SS_comm_mbin_angpix,
                                           micrograph_pixelsize=self.EM_mics_apix)
        return adjust_boxsize(result, self.force_eman)

    @property
    def CSS_mbin_reextract_parts_x_min(self):
        result = compute_extract_coordinates_min(boxsize=self.CSS_mbin_reextract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return adjust_boxsize(result, self.force_eman)

    @property
    def CSS_mbin_reextract_parts_x_max(self):
        result = compute_extract_coordinates_max(boxsize=self.CSS_mbin_reextract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return adjust_boxsize(result, self.force_eman)
    
    @property
    def CSS_mbin_reextract_parts_y_min(self): 
        result = compute_extract_coordinates_min(boxsize=self.CSS_mbin_reextract_mics_box, 
                                                 lower_bound=self.mics_lower_bound)
        return adjust_boxsize(result, self.force_eman)

    @property
    def CSS_mbin_reextract_parts_y_max(self):
        result = compute_extract_coordinates_max(boxsize=self.CSS_mbin_reextract_mics_box,
                                                 upper_bound=self.mics_upper_bound)
        return adjust_boxsize(result, self.force_eman)

    def to_dict(self, parameters_of_interest):
        return {poi:getattr(self, poi) for poi in parameters_of_interest}

    @classmethod
    def get_valid_fields(cls):
        return {f.name for f in fields(cls)}

### css parameter calculation
def compute_extract_coordinates_min(boxsize, lower_bound=0):
    return lower_bound + (boxsize / 2)

def compute_extract_coordinates_max(boxsize, upper_bound):
    return upper_bound - (boxsize / 2)

def compute_extract_parts_box(boxsize, binned_pixelsize, micrograph_pixelsize):
    return boxsize / (binned_pixelsize / micrograph_pixelsize)

def adjust_boxsize(boxsize, force_eman=True):#, force_prime=True, force_even=True):
    result = boxsize

    if force_eman:
        result = get_next_eman_boxsize(result)
    # if force_even:
    #     result = get_next_even_number(result)
    # if force_prime:
    #     result = get_next_prime_decomposition(result)

    return result

### general
def get_next_eman_boxsize(boxsize):
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
    

    result = boxsize

    mask = (result <= boxsize_list)
    if sum(mask) > 0:
        result = boxsize_list[mask].min()
    
    return result

def get_next_even_number():
    # eman boxsizes are all even, so dont need this function right now
    pass

def get_next_prime_decomposition():
    # implent after the core functionality is finalized
    pass


