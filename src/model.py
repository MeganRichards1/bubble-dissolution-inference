import numpy as np

R0 = 15  # global constant for the initial radius in this paper

def radius_model(t, k):
    return np.sqrt(np.maximum(R0**2 - 2*k*t, 0))

def exponential_model(t, k):
    return R0 * np.exp(-k * t)

def time_to_dissolution(k):
    return R0**2 / (2*k)