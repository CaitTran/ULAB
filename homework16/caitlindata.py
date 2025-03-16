import torch
import numpy as np

# Underlying Pattern we are trying to find 
x_data = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_data = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)

#Hidden pattern
pattern = np.sin(np.sqrt(np.clip(X**4, 0, None))) + np.cos(np.sqrt(np.clip(Y**4, 0, None)))

# Actual data 
# Defining the dataset dimensions
N, D_in, H, D_out = 1000, 2, 50, 1

#input data still on scale of pi
x = torch.randn(N, D_in) * 3.1415
y = (torch.sqrt(x[:, 0]**4).sin() + torch.sqrt(x[:, 1]**4).cos()).unsqueeze(1)

#add noise
noise = torch.randn(N, D_out) * 3 #lots of noise
y += noise

#plotting
x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()