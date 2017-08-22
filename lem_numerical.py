#
# Steps:
# - calculate drainage area A
# - calculate steepest slope
# - numerically calculate second derivative
#
#

import numpy as np

from pylem import LemConsts, calc_dz_dt

x_dist = 100
x_size = 1

timesteps = 1000
plot_every = 100
slope = -0.1

lem_consts = LemConsts(0.5, 1.0, 5e-6, 3e-2)

x = np.linspace(0.0, x_dist, x_dist / x_size + 1)
z_orig = np.linspace(-slope * x_dist, 0.0, x_dist / x_size + 1)

zs = [z_orig]
z = z_orig.copy()


for plot_index in range(1, timesteps + 1):
    z[-1] = 0.0
    dz_dt = calc_dz_dt(z, x_size, lem_consts)
    z += dz_dt

    if plot_index % plot_every == 0:
        zs += [z.copy()]

print("Total erosion (1000 timesteps)= %.2f" % (z - z_orig).sum())
# plot(x, zs)

dz_dt = calc_dz_dt(z_orig, x_size, lem_consts)
zs = [z_orig, z_orig + dz_dt]
print("Total erosion (1 timesteps * 1000) = %.2f" % ((dz_dt).sum() * 1000))
# plot(x, zs)
