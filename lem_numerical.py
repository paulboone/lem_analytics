#
# Steps:
# - calculate drainage area A
# - calculate steepest slope
# - numerically calculate second derivative
#
#


m = 0.5
n = 1.0
k = 1
d = 1


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import figaspect

def calc_drainage_area(z):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        drainage = 0
        # look left
        j = i - 1
        while j >= 0 and z[j] > z[j + 1]:
            drainage += 1
            j -= 1

        j = i + 1
        # look right
        while j < len(z) - 1 and z[j] > z[j - 1]:
            drainage += 1
            j += 1

        results[i] = drainage
    return results

def calc_steepest_slope(z):
    results = np.zeros(len(z))
    for i,_ in enumerate(z):
        slopes = []
        if i > 0:
            slopes.append(z[i - 1] - z[i])
        if i < len(z) - 1:
            slopes.append(z[i + 1] - z[i])
        results[i] = min(0, *slopes)
    return results

def calc_d2z_dx2(z):
    return np.gradient(np.gradient(z))


def calc_dz_dt(z):
    a = calc_drainage_area(z)
    s = calc_steepest_slope(z)
    sp = calc_d2z_dx2(z)
    return k*(a**m)*(s**n) + d * sp




x = np.arange(0,100)
z = np.arange(100,0, -1)

dz_dt = calc_dz_dt(z)
print(dz_dt)
print(z + dz_dt)

num_plots = 1
w, h = figaspect(0.5)
fig = plt.figure(figsize=(w,(h+1)*num_plots))
ax = fig.add_subplot(num_plots, 1, plot_index)
ax.plot(x,z)


# print(z1, len(z2))
# print(z2, len(z2))
