#File: integration.py

import numpy as np
from numpy import *

def riemann_sum_for_X(first_x_boundary, second_x_boundary, num_x_points):
    """
    Input: A minimum and maximum x boundary (int or float), a number of points to create Riemann Sum distances out of (int)
    Output: The points for the Riemann Sum distances in x (array of floats)
    """
    
    #give equal distance (delta x) points between the two boundaries -- number of points depends on num_x_points input
    num_x_dims = linspace(first_x_boundary, second_x_boundary, num_x_points)    
    
    return num_x_dims


def riemann_sum_for_Y(first_y_boundary, second_y_boundary, num_y_points):
    """
    Input: A minimum and maximum y boundary (int or float), a number of points to create Riemann Sum distances out of (int)
    Output: The points for the Riemann Sum distances in y (array of floats)
    """

    #give equal distance (delta y) points between the two boundaries -- number of points depends on num_y_points input
    num_y_dims = linspace(first_y_boundary, second_y_boundary, num_y_points)
    
    return num_y_dims

def calculate_approx_volume(first_x_boundary, second_x_boundary, first_y_boundary, second_y_boundary, num_x_points, num_y_points, z):
    """
    Calculates the approximate volume of a rectangular prism region using Riemann Sum.
    
    Input for x: A minimum and maximum x boundary (int or float), a number of points to create riemann sum distances out of (int)
    Input for y: A minimum and maximum y boundary (int or float), a number of points to create riemann sum distances out of (int)
    Input: z (int) for height of rectangular prisms for riemann sum
    Output: approximate volume of the region under z = n (float), and the accuracy of the approximate volume relative to a general box volume
    """

    #initialize the total volume (each prism adds to it)
    total_volume = 0

    #call upon the first 2 functions to create the points to multiply to each other (arrays)
    num_x_dims = riemann_sum_for_X(first_x_boundary, second_x_boundary, num_x_points)
    num_y_dims = riemann_sum_for_Y(first_y_boundary, second_y_boundary, num_y_points)

    #make a general box volume to compare the approximate volume to later
    box_volume = (second_x_boundary - first_x_boundary) * (second_y_boundary - first_y_boundary) * z

    #simulataneously iterate through the arrays of x and y points to multiply to each other 
    for x, y in np.nditer([num_x_dims, num_y_dims]):

        #create a rectangle with area x*y
        x_y_area = x * y

        #add the rectangle * height (z) to the initialized approximate volume
        approx_volume += z * x_y_area

    #checking accuracy relative to the box volume
    if approx_volume < box_volume:
        print("Approx volume is more accurate than total box volume")
    elif approx_volume > box_volume:
        print("Approx volume is less accurate than total box volume, add more x and y points")
    else:
        print("Approx volume is the same as total box volume, add more x and y points") 
        
    return approx_volume

