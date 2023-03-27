import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from scipy.optimize import minimize

from cosamp import cosamp


# generate a signal and compute its power spectral density
n = 4096
t = np.linspace(0, 1, n)
x = np.cos(97 * 2 * np.pi * t) + np.cos(777 * 2 * np.pi * t)
xt = np.fft.fft(x)
PSD = xt * xt.conjugate() / n

# randomly sample signal by using discrete measurements
p = 128
perm = np.floor(np.random.rand(p) * n).astype(int)
y = x[perm]

# solve compressed sensing problem- and reconstruct the undersampled signal
Psi = dct(np.identity(n))
Theta = Psi[perm, :]
s = cosamp(Theta, y, 10, tol=1.e-10, max_iter=10)
xrecon = idct(s)

# compute the power spectral density of the reconstructed signal
xtrecon = np.fft.fft(xrecon, n)
PSDrecon = xtrecon * xtrecon.conjugate() / n

# visualize
w = np.array([1024, 1280])/4096
freq = np.arange(n)
L = int(np.floor(n/2))
fig, axs = plt.subplots(2, 2)
axs = axs.reshape(-1)

# original signal
axs[0].plot(t, x, 'k', lw=2)
axs[0].plot(perm/n, y, 'rx', ms=10, mew=2)
axs[0].set_xlim(w[0], w[1])
axs[0].set_ylim(-2, 2)
axs[1].plot(freq[:L], PSD[:L], 'k', lw=2)
axs[1].set_xlim(0, 1024)
axs[1].set_ylim(0, 1200)

# reconstruction
axs[2].plot(t, xrecon, 'r', lw=2)
axs[2].set_xlim(w[0], w[1])
axs[2].set_ylim(-2, 2)
axs[3].plot(freq[:L], PSDrecon[:L], 'r', lw=2)
axs[3].set_xlim(0, 1024)
axs[3].set_ylim(0, 1200)

plt.show()
