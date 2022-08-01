import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# refractive index
mu = 1.3
# max intensity
I_0 = 1
# angle of incidence
theta_inc = 90*np.pi/180
# angle of refraction
theta_ref = np.arcsin(np.sin(theta_inc)/mu)
# wavelength in nanometers
wavelength = np.linspace(380, 780, 1000)

# thickness in nanometers
thickness = np.linspace(0, 2000, 2000)


def intensity(w,t):
    inner = (2*np.pi*mu*t/wavelength)*np.cos(theta_ref)
    return I_0 * (np.sin(inner))**2


W, T = np.meshgrid(wavelength, thickness)  # generate the mesh of points (w,t)
Z = intensity(W, T)

pcm = ax.pcolormesh(W, T, Z, cmap="gist_gray")  # renders the colormap
ax.set_xlabel(r"Wavelength $\lambda$ (nm)")
ax.set_ylabel(r"Thickness $t$ (nm)")
cbar = fig.colorbar(pcm)  # places the colorbar with label
cbar.set_label("Intensity")
fig.savefig("thin_film_interference.png", dpi=1000)
