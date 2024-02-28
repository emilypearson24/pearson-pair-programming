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
    r (int, float, or ndarray) : polar r-value
    theta (int, float, or ndarray): the angle theta of the polar coordinate
     
    Returns
    -------
    x (int, float, or ndarray) : Cartesian x-coordinate of the point
    y (int, float, ndarray) : Cartesian y-coordinate of the point
    
    """
    assert (type(r)==float) or (type(r)==int) or (type(r)==np.ndarray)
    x = r * np.cos(theta)  #x-coordinate = r*cos(theta)
    y = r * np.sin(theta)  #y-coordinate = r*sin(theta)
    return(x, y)

