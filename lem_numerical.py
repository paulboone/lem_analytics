#
# Steps:
# - calculate drainage area A
# - calculate steepest slope
# - numerically calculate second derivative
#
#

from collections import namedtuple

from matplotlib import pyplot as plt
from matplotlib.figure import figaspect
import numpy as np

def calc_drainage_area(z):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        drainage = 0
        # look left
        j = i - 1
        while j >= 0 and z[j] > z[j + 1]:
            drainage +=  x_size
            j -= 1

        j = i + 1
        # look right
        while j < len(z) - 1 and z[j] > z[j - 1]:
            drainage += x_size
            j += 1

        results[i] = drainage
    return results

def calc_steepest_slope(z):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        slopes = []
        if i > 0:
            slopes.append((z[i - 1] - z[i]) / x_size)
        if i < len(z) - 1:
            slopes.append(z[i + 1] - z[i] / x_size)
        results[i] = min(0, *slopes)
    return results

def calc_d2z_dx2(z):
    return np.gradient(np.gradient(z))


def calc_dz_dt(z, c):
    a = calc_drainage_area(z)
    s = calc_steepest_slope(z)
    sp = calc_d2z_dx2(z)
    return c.k*(a**c.m)*(s**c.n) + c.d * sp


def plot(x, zs):
    z_orig = zs[0]
    num_plots = len(zs)

    w, h = figaspect(0.5)
    fig = plt.figure(figsize=(w,(h + 1) * num_plots))

    for i, z in enumerate(zs):
        print(len(x), len(zs), len(z))
        ax = fig.add_subplot(num_plots, 2, i*2 + 1)
        ax.grid(linestyle='-', color='0.7', zorder=0)
        # ax.set_ylim(0, 0.05)
        ax.plot(x,z)
        ax = fig.add_subplot(num_plots, 2, i*2 + 2)
        ax.grid(linestyle='-', color='0.7', zorder=0)
        ax.set_ylim(0, 0.05)
        ax.plot(x,z_orig - z)

    fig.show()

LemConsts = namedtuple('LemConsts', ['m', 'n', 'k', 'd'])
lem_consts_t1 = LemConsts(0.5, 1.0, 5e-6, 3e-2)
lem_consts_t1000 = LemConsts(0.5, 1.0, 5e-6 * 1000, 3e-2 * 1000)

x_dist = 100
x_size = 1

timesteps = 1000
plot_every = 100
slope = -1

# x = np.arange(0, x_dist / x_size)
x = np.linspace(0.0, x_dist, x_dist / x_size + 1)
z_orig = np.linspace(-slope * x_dist, 0.0, x_dist / x_size + 1)
print(x, z_orig)

zs = [z_orig]
z = z_orig.copy()

for plot_index in range(1, timesteps + 1):
    z[-1] = 0.0
    dz_dt = calc_dz_dt(z, lem_consts_t1)
    z += dz_dt

    if plot_index % plot_every == 0:
        zs += [z.copy()]

print("Total erosion (1000 timesteps)= %.2f" % (z - z_orig).sum())
plot(x, zs)

dz_dt = calc_dz_dt(z_orig, lem_consts_t1000)
zs = [z_orig, z_orig + dz_dt]
print("Total erosion (1 timesteps * 1000) = %.2f" % (dz_dt).sum())
plot(x, zs)
