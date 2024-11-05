#File: integration.py

def riemann_sum_for_x(first_x_boundary, second_x_boundary, num_x_points):
    
    num_x_rectangles = np.linspace(first_x_boundary, second_x_boundary, num_x_points)
    
    return num_x_rectangles


