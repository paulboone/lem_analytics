from collections import namedtuple

from matplotlib import pyplot as plt
from matplotlib.figure import figaspect
import numpy as np

LemConsts = namedtuple('LemConsts', ['m', 'n', 'k', 'd'])

def calc_drainage_area(z, x_size):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        drainage = 0.0
        # look left
        j = i - 1
        while j >= 0 and z[j] > z[j + 1]:
            drainage += x_size
            j -= 1

        j = i + 1
        # look right
        while j < len(z) - 1 and z[j] > z[j - 1]:
            drainage += x_size
            j += 1

        results[i] = drainage
    return results

def calc_steepest_slope(z, x_size):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        slopes = []
        if i > 0:
            slopes.append((z[i - 1] - z[i]) / x_size)
        if i < len(z) - 1:
            slopes.append(z[i + 1] - z[i] / x_size)
        results[i] = min(0, *slopes)
    return results

def calc_d2z_dx2(z, x_size):
    return np.gradient(np.gradient(z, x_size), x_size)


def calc_dz_dt(z, x_size, c):
    a = calc_drainage_area(z, x_size)
    # print(a)
    s = calc_steepest_slope(z, x_size)
    sp = calc_d2z_dx2(z, x_size)
    return c.k*(a**c.m)*(s**c.n) + c.d * sp


def plot(x, zs):
    z_orig = zs[0]
    num_plots = len(zs)

    w, h = figaspect(0.5)
    fig = plt.figure(figsize=(w,(h + 1) * num_plots))

    for i, z in enumerate(zs):
        # print(len(x), len(zs), len(z))
        ax = fig.add_subplot(num_plots, 2, i*2 + 1)
        ax.grid(linestyle='-', color='0.7', zorder=0)
        # ax.set_ylim(0, 0.05)
        ax.plot(x,z)
        ax = fig.add_subplot(num_plots, 2, i*2 + 2)
        ax.grid(linestyle='-', color='0.7', zorder=0)
        ax.set_ylim(0, 0.05)
        ax.plot(x,z_orig - z)

    fig.show()
