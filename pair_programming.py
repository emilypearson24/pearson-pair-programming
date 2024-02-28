## Author: Emily Pearson
## GPGN 268 Geophysical Data Analysis
## SA05-pair-programming
## Prompt 2: Change coordinates from polar to Cartesian (rectangular)

import numpy as np

def polar_to_rect(r, theta):  #define function
    """This function changes coordinates from polar to rectangular
    
    It takes a point defined in polar coordinates and changes the point to rectangular/Cartesian coordinates
    
    Parameters
    ----------
    input : int or float
        Input is values for the coordinates (r, theta)
        
    Returns
    -------
    output : float
        Output is the rectangular coordinates (x, y) of the point
    
    """
    x = r * np.cos(theta)  #x-coordinate = r*cos(theta)
    y = r * np.sin(theta)  #y-coordinate = r*sin(theta)
    
    return(x, y)

