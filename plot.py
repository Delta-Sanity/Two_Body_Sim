# NOTES:
#
# velocity (vel) is assumed to be the distance the change in position experienced by the particle in 1 second
# position is described in meters, mass in kilograms and time in seconds
# 
# standard state array is the following arrangement:
# state[n] = [[pos_x, pos_y], [vel_x, vel_y]]
# absolute state (abs_state) encodes the start and end points of the vector on the (x, y) plane
# relative state (rel_state) encodes the origin of the vector and the location of the tip, as relative to the origin point



from typing import List
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
import numpy as np
from numpy.core.multiarray import array
import sim
            
def paths_array_to_paths_list(__array__):

    dim = np.shape(__array__)
    print(__array__)
    paths_list = []
    for i in range(dim[1]):
        paths_list.append(__array__[0:, i])
    
    return(paths_list)

def extract_points(__array__):
    
    dim = __array__.shape
    

    #Check to make sure that array has dimensions of [n, 2, 2], if it has dimensions [n, 2] it is already in point form, if it is in any other form, it is incorrect

    if ((dim[1] == 2) and (len(dim) == 2)):
        print('InvalidArray: Array provided is already in point form')
        return(__array__)
    elif ((dim[1] != 2) or (dim[2] != 2) or (not (len(dim) == 3))):
        print('InvalidArray: Array provided is not in (n, 2, 2) form')
        return

    #Extract indices that contain points
    points = __array__[0:, 0]
    
    return(points)



def plot_points(__array__, color = '#3D59AB'):
    
    dim = __array__.shape
    if not ((dim[1] == 2) and (len(dim) == 2)):
        raise(TypeError, 'Array is not in the form of a list of (x, y) points')
        return

    
    point_array = __array__
    points_x = list(point_array[0:, 0])
    points_y = list(point_array[0:, 1])
    x_range = (int(min(points_x) - 2), int(2 + max(points_x)))
    y_range = (int(min(points_y) - 2), int(2 + max(points_y)))

    ax.set_xlim(x_range[0], x_range[1])
    ax.set_ylim(y_range[0], y_range[1])

    ax.scatter(points_x, points_y, c = color)
    
    

def plot_paths(paths_list):
    
    fig, ax = plt.subplots()
    
    paths_count = len(paths_list)
    paths_x_max = []
    paths_y_max = []
    paths_x_min = []
    paths_y_min = []
    
    for i in range(0, paths_count): #Check to make sure paths_list is in the form of a list of arrays of (x, y) points
        __array__ = np.array(paths_list[i])
        dim = __array__.shape
        if not ((dim[1] == 2) and (len(dim) == 2)):
            raise(TypeError, 'Array #', i, ' is not in the form of a list of (x, y) points')
            return
    
        paths_x_max.append((int(max(list(__array__[0:, 0])))) + 2)
        paths_y_max.append((int(max(list(__array__[0:, 1])))) + 2)
        paths_x_min.append((int(min(list(__array__[0:, 0])))) - 2)
        paths_y_min.append((int(min(list(__array__[0:, 1])))) - 2)
    
    ax.set_xlim(min(paths_x_min), max(paths_x_max))
    ax.set_ylim(min(paths_y_min), max(paths_y_max))
    
    colors_lib = [
        '#FF0000',
        '#008000',
        '#3D59AB',
        '#98F5FF',
        '#8A2BE2',
        '#8B8989',
        '#FF6347',
        '#EEEE00',
        '#EE3A8C',
        '#00C78C',
        '#473C8B'
        ]
    
    
    for i in range(0, paths_count):
        
        __array__ = paths_list[i]
        
        x_points = list(__array__[0:, 0])
        y_points = list(__array__[0:, 1])
        ax.scatter(x_points, y_points, s=3, c = colors_lib[i])
    
    return
    


