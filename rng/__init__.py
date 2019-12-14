import numpy as np

theta = np.linspace(0, np.pi, 181)
sin_theta, cos_theta = np.sin(theta), np.cos(theta)
one_minus_ct = 1 - cos_theta
sin2_t = np.power(sin_theta, 2)
