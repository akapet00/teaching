import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec
import numpy as np

from neuron_model import HodgkinHuxley


def animation_1():
    C_m = 1.0       # membrane capacitance [F/cm^2]
    g_Na = 120.0    # Sodium (Na) maximum conductance [mS/cm^2]
    g_K  = 36.0     # Postassium (K) maximum conductance [mS/cm^2]
    g_L  = 0.3      # Leak maximum conductance [mS/cm^2]
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
    lines = []
    for i, T in enumerate(Ts):
        line, = axs[i].plot(0, 0)
        lines.append(line)
        axs[i].set_xlim(0, 1.05*t.max())
        axs[i].set_ylim(1.1*V_m[i].min(), 1.2*V_m[i].max())
        axs[i].set_ylabel('$V_m$ [mV]')
        axs[i].legend([f'$V_m$ (t, T={T}°C)',])
        axs[i].grid()
    _ = plt.xlabel('t [ms]')
    
    def run(frame):
        for idx, line in enumerate(lines):
            line.set_data(t[:frame], V_m[idx][:frame])
        return lines

    anim = FuncAnimation(fig, run, frames=np.arange(0, t.size, step=100), interval=1)
    #plt.show() 
    anim.save('Vm_in_time_for_different_temperatures.gif', writer='imagemagick', fps=30)


def animation_2():
    C_m = 1.0       # membrane capacitance [F/cm^2]
    g_Na = 120.0    # Sodium (Na) maximum conductance [mS/cm^2]
    g_K  = 36.0     # Postassium (K) maximum conductance [mS/cm^2]
    g_L  = 0.3      # Leak maximum conductance [mS/cm^2]
    E_Na = 50.0     # Sodium (Na) reversal potentials [mV]
    E_K  = -77.0    # Postassium (K) reversal potentials [mV]
    E_L  = -54.387  # Leak reversal potentials [mV]
    I_inj = lambda t: 10*(t>5) - 10*(t>60) + 35*(t>80) - 35*(t>100)
    initial_conds = [-65, 0.05, 0.6, 0.32]
    t = np.arange(0.0, 140.0, 0.01)
    T = 6.3

    model = HodgkinHuxley(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, I_inj, T)
    V_m, m, h, n, ina, ik, il, iinj = model.simulate(initial_conds, t, ret=True)

    gs = GridSpec(3, 3)
    fig = plt.figure(figsize=(8, 8))
    fig.set_tight_layout(True)
    ax0 = plt.subplot(gs[0, :])
    ax1 = plt.subplot(gs[1, :])
    ax20 = plt.subplot(gs[2, 0])
    ax21 = plt.subplot(gs[2, 1])
    ax22 = plt.subplot(gs[2, 2])

    ax0.set_xlim(0, 1.05*t.max())
    ax0.set_ylim(1.1*V_m.min(), 1.1*V_m.max())
    ax0.set_ylabel('$V_m$ [mV]')
    ax0.set_xlabel('$t$ [ms]')
    ax0.grid()
    ax1.set_xlim(0, 1.05*t.max())
    ax1.set_ylim(iinj.min()-0.1*iinj.max(), 1.1*iinj.max())
    ax1.set_ylabel(r'$I$ [$\mu A \cdot cm^{-2}$]')
    ax1.set_xlabel('$t$ [ms]')
    ax1.grid()
    ax20.set_xlim(1.1*V_m.min(), 1.1*V_m.max())
    ax20.set_ylim(m.min()-0.1, 1.1*m.max())
    ax20.set_ylabel('$m$')
    ax20.set_xlabel('$V_m$ [mV]')
    ax20.grid()
    ax21.set_xlim(1.1*V_m.min(), 1.1*V_m.max())
    ax21.set_ylim(h.min()-0.1, 1.1*h.max())
    ax21.set_ylabel('$h$')
    ax21.set_xlabel('$V_m$ [mV]')
    ax21.grid()
    ax22.set_xlim(1.1*V_m.min(), 1.1*V_m.max())
    ax22.set_ylim(n.min()-0.1, 1.1*n.max())
    ax22.set_ylabel('$n$')
    ax22.set_xlabel('$V_m$ [mV]')
    ax22.grid()
    
    line0, = ax0.plot(0, 0, color='red', label=f'$V_m$ (t, T={T}°C)')
    line1, = ax1.plot(0, 0, color='green', label=f'$I$ (t)')
    line20, = ax20.plot(0, 0, color='blue', alpha=0.8, label=f'$m(V_m)$')
    line21, = ax21.plot(0, 0, color='blue', alpha=0.8, label=f'$h(V_m)$')
    line22, = ax22.plot(0, 0, color='blue', alpha=0.8, label=f'$n(V_m)$')
    lines = [line0, line1, line20, line21, line22]
    
    def run(frame):
        lines[0].set_data(t[:frame], V_m[:frame])
        lines[1].set_data(t[:frame], iinj[:frame])
        lines[2].set_data(V_m[:frame], m[:frame])
        lines[3].set_data(V_m[:frame], h[:frame])
        lines[4].set_data(V_m[:frame], n[:frame])
        return lines

    anim = FuncAnimation(fig, run, frames=np.arange(0, t.size, step=100), interval=0.1)
    ax0.legend()
    ax1.legend()
    ax20.legend()
    ax21.legend()
    ax22.legend()
    #plt.show()
    anim.save('Vm_and_Ixt_in_time.gif', writer='imagemagick', fps=30)


if __name__ == "__main__":
    animation_1()
    animation_2()