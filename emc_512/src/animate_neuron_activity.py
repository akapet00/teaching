import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from neuron_model import HodgkinHuxley

def main():
    C_m = 1.0       # membrane capacitance [F/cm^2]
    g_Na = 120.0    # Sodium (Na) maximum conductances [mS/cm^2]
    g_K  = 36.0     # Postassium (K) maximum conductances [mS/cm^2]
    g_L  = 0.3      # Leak maximum conductances [mS/cm^2]
    E_Na = 50.0     # Sodium (Na) reversal potentials [mV]
    E_K  = -77.0    # Postassium (K) reversal potentials [mV]
    E_L  = -54.387  # Leak reversal potentials [mV]
    I_inj = lambda t: 10*(t>5) - 10*(t>60)
    initial_conds = [-65, 0.05, 0.6, 0.32]
    t = np.arange(0.0, 120.0, 0.01)
    Ts = [0.3, 6.3, 16.3]
    V_m = []

    for T in Ts:
        model = HodgkinHuxley(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, I_inj, T)
        _V_m, *_ = model.simulate(initial_conds, t, ret=True)
        V_m.append(_V_m)

    fig, axs = plt.subplots(nrows=3, ncols=1, sharex=True)
    line_0, = axs[0].plot(0, 0)
    line_1, = axs[1].plot(0, 0)
    line_2, = axs[2].plot(0, 0)
    line = [line_0, line_1, line_2]

    for i, T in enumerate(Ts):
        axs[i].set_xlim(0, 1.05*t.max())
        axs[i].set_ylim(1.1*V_m[0].min(), 1.1*V_m[i].max())
        axs[i].set_ylabel('$V_m$ [mV]')
        axs[i].legend([f'$V_m$ (t, T={T}°C)',])
        axs[i].grid()
    axs[i].set_xlabel('t [ms]')
    
    def run(i):
        line[0].set_data(t[:i], V_m[0][:i])
        line[1].set_data(t[:i], V_m[1][:i])
        line[2].set_data(t[:i], V_m[2][:i])
        return line

    anim = FuncAnimation(fig, run, frames=np.arange(0, t.size, step=100), interval=1)

    #plt.show() 
    anim.save('neuron_activity.mp4', writer='imagemagick', fps=30)


if __name__ == "__main__":
    main()