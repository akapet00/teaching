import numpy as np
import matplotlib.pyplot as plt


# generate a 40 Hz sine signal and sample it 800 times per second
f = 25
tstart = -0.3
tend = 0.3
t = np.linspace(tstart, tend, 800)
x = np.cos(2 * np.pi * t) + np.cos(2 * np.pi * f * t)

# sample the signal by using 80 Hz sampling rate
fs1 = 2 * f
T1 = 1 / (fs1)
n1 = np.arange(tstart/T1, tend/T1+1)
x1 = np.cos(2 * np.pi * n1 * T1) + np.cos(2 * np.pi * f * n1 * T1)

# sample the signal by using the rate of 35 Hz - below the Nyquist criterium
fs2 = int(0.8 * f)
T2 = 1 / (fs2)
n2 = np.arange(tstart/T2, tend/T2+1)
x2 = np.cos(2 * np.pi * n2 * T2) + np.cos(2 * np.pi * f * n2 * T2)

# visualize
plt.plot(t, x, 'k-', label='original signal')
plt.plot(n1*T1, x1, 'r.-.', label=f'reconstruction at {fs1} Hz')
plt.plot(n2*T2, x2, 'bx--', label=f'reconstruction at {fs2} Hz')
plt.xlabel('time, s')
plt.ylabel('amplitude')
plt.legend()
plt.show()