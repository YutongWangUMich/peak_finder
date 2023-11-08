import numpy as np


def sin_waves(n_x_points=200, n_peaks=3, noise = 0.01):
    n = n_x_points
    grids = np.linspace(0, np.pi, n+1)
    # Sine function values at the lattice points
    y = np.sin(0.85*grids)*np.sin(n_peaks*grids)**2 + noise*np.random.randn(n+1)
    y[int(n/10)] += 0.25
    y[int(4.1*n/10)] += 0.25
    y[int((9.5*n)/10)] += 0.25
    return y


def mountains_and_plateau():
    x = np.arange(1000)  # Range from 0 to 999
    y = np.zeros_like(x, dtype=float)  # Initialize y with zeros, as floats

    # First mountain (Gaussian)
    y += 100.0 * np.exp(-0.5 * ((x - 200.0) / 50.0) ** 2)  # Mountain at x=200

    # Second mountain (Sharp, sawtooth-like peak)
    # Define the slope of the ascent and descent
    ascent_slope = 0.8
    descent_slope = -0.9

    # Calculate the ascent and descent of the sawtooth
    ascent = ascent_slope * (x - 666.0 + 50.0 * (x > 666)) * (x > 666) * (x < 716)
    descent = descent_slope * (x - 777.0) * (x >= 716) * (x < 799)
    y += np.maximum(0, ascent + descent)

    # Define the plateau as a flat line between x=400 and x=555
    y[400:556] = 10.0  # Flat plateau at height 10
    y += np.random.randn(len(y))
    return y