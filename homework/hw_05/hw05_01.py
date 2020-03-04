import math
import numpy as np
import scipy.stats
import timeit
import matplotlib.pyplot as plt

"""
    Exe.1
"""


def sample_normal_twelve(mu, sigma):
    a = np.sum(np.random.uniform(sigma, -sigma, 12))
    return mu + a


def rejection_sample(mu, sigma):
    interval = 5 * sigma

    # Using scipy.stats.norm class
    norm = scipy.stats.norm(mu, sigma)
    max_density = norm.pdf(mu)
    while True:
        x = np.random.uniform(mu - interval, mu + interval, 1)[0]
        y = np.random.uniform(0, max_density, 1)
        if norm.pdf(x) >= y:
            return x


def sample_normal_box_muller(mu, sigma):
    u = np.random.uniform(0, 1, 2)
    u1 = u[0]
    u2 = u[1]
    x = math.cos(2 * np.pi * u1) * math.sqrt(-2 * math.log(u2, math.e))
    return mu + x

# Evaluate 3 different sampling methods

