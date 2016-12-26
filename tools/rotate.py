#!/usr/bin/env python

import numpy as np
from scipy import ndimage

def Rotate(image, phi, clip=True):
    
    """
    Rotate the input image by phi about its center.  Do not resize the 
    image, but pad with zeros.  
    
    Inputs: 
    1. image:   2D array
    2. phi:     rotation angle in radians
    3. image2:  2D array (optional).  If supplied, the same transformation
                will be applied.
    4. clip:    boolean (optional): clip array by sqrt(2) to remove
                fill values?  Default True.

    Outputs:
    rotated image of the same shape as the input image, with zero-padding

    """

    x = np.arange(image.shape[0])
    med_n = np.median(x)
    x -= int(med_n)			# edit MjR Oct 2016
    x, y = np.meshgrid(x, x)

    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    x = r*np.cos(theta + phi) + med_n
    y = r*np.sin(theta + phi) + med_n

    imageout = ndimage.map_coordinates(image, [y, x], order=1, prefilter=False)
        
    if clip:
        i = int(imageout.shape[0]*(1. - 1./np.sqrt(2.))/2.)
        imageout = imageout[i:-i, i:-i]
    
    return imageout
