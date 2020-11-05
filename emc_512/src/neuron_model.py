import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


class HodgkinHuxley(object):
    """Full Hodgkin-Huxley Model implementation.
    Original implementation: 
    https://hodgkin-huxley-tutorial.readthedocs.io/en/latest/_static/Hodgkin%20Huxley.html
    """
    def __init__(self, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L):
        """Constructor.
        
        Parameters
        ----------
        C_m : float
            Membrane capacitance [F/cm^2]
        g_Na : float
            Sodium (Na) maximum conductances [mS/cm^2]
        g_K : float
            Postassium (K) maximum conductances [mS/cm^2]
        g_L : float
            Leak maximum conductances [mS/cm^2]
        E_Na : float
            Sodium (Na) reversal potentials [mV]
        E_K : float
            Postassium (K) reversal potentials [mV]
        E_L : float
            Leak reversal potentials [mV]
        
        Returns
        -------
        None
        """
        self.C_m = C_m 
        self.g_Na = g_Na
        self.g_K  = g_K 
        self.g_L  = g_L 
        self.E_Na = E_Na
        self.E_K = E_K 
        self.E_L = E_L 

    def alpha_m(self, V_m):
        """Return the value of the alpha_m parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            alpha_m value
        """
        return 0.1 * (V_m+40.0) / (1.0-np.exp(-(V_m+40.0)/10.0))

    def beta_m(self, V_m):
        """Return the value of the beta_m parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            beta_m value
        """
        return 4.0 * np.exp(-(V_m+65.0)/18.0)

    def alpha_h(self, V_m):
        """Return the value of the alpha_h parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            alpha_h value
        """
        return 0.07 * np.exp(-(V_m+65.0)/20.0)

    def beta_h(self, V_m):
        """Return the value of the beta_h parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            beta_h value
        """
        return 1.0 / (1.0+np.exp(-(V_m+35.0)/10.0))

    def alpha_n(self, V_m):
        """Return the value of the alpha_n parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            alpha_n value
        """
        return 0.01 * (V_m+55.0) / (1.0-np.exp(-(V_m+55.0)/10.0))

    def beta_n(self, V_m):
        """Return the value of the beta_n parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            beta_n value
        """
        return 0.125 * np.exp(-(V_m+65)/80.0)

    def I_Na(self, V_m, m, h):
        """Return the Na ion channel current densitiy.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            Na ion channel current density [uA/cm^2]
        """
        return self.g_Na * m**3 * h * (V_m - self.E_Na)

    def I_K(self, V_m, n):
        """Return the K ion channel current densitiy.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            K ion channel current density [uA/cm^2]
        """
        return self.g_K * n**4 * (V_m - self.E_K)
    
    def I_L(self, V_m):
        """Return the density of the leak current.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
            
        Returns
        -------
        float
            Leak current density [uA/cm^2]
        """
        return self.g_L * (V_m - self.E_L)

    def I_inj(self, t):
        """Return the external current values over simulation time, `t`.
        
        Parameters
        ----------
        t : float
            Simulation time point
            
        Returns
        -------
        numpy.ndarray
            External current density [uA/cm^2]:
            step up to 10 uA/cm^2 at t>100
            step down to 0 uA/cm^2 at t>200
            step up to 35 uA/cm^2 at t>300
            step down to 0 uA/cm^2 at t>400
        """
        return 10*(t>100) - 10*(t>200) + 35*(t>300) - 35*(t>400)

    def ode_system(self, initial_conds, t):
        """Hodgkin Huxley model based on a set of four coupled ODEs.
        For details, go here: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model#Voltage-gated_ion_channels

        Parameters
        ----------
        initial_conds : list
            Initial conditions for resting membrane potential and m, h and n activation variables
        t : numpy.ndarray
            A sequence of time points for which to solve for y
            
        Returns
        -------
        tuple
            Membrane potential and m, h adn n activation variables
        """
        V_m, m, h, n = initial_conds

        dV_mdt = (self.I_inj(t) - self.I_Na(V_m, m, h) - self.I_K(V_m, n) - self.I_L(V_m)) / self.C_m
        dmdt = self.alpha_m(V_m)*(1.0-m) - self.beta_m(V_m)*m
        dhdt = self.alpha_h(V_m)*(1.0-h) - self.beta_h(V_m)*h
        dndt = self.alpha_n(V_m)*(1.0-n) - self.beta_n(V_m)*n
        return (dV_mdt, dmdt, dhdt, dndt)
    
    def simulate(self, initial_conds, t, ret=False, viz=False):
        """Hodgkin Huxley model based on a set of four coupled ODEs.
        For details, go here: https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model#Voltage-gated_ion_channels

        Parameters
        ----------
        initial_conds : list
            Initial conditions for resting membrane potential and m, h and n activation variables
        t : numpy.ndarray
            A sequence of time points for which to solve for y
        ret : bool, optional
            If True, calculated electrical parameters will be returned
        viz : bool, optional
            If True, simulation will be visualized
            
        Returns
        -------
        tuple or None
            if `ret` is set to True, tuple containg membrane potential, activation functions and currents will be returned
        """
        self.t = t
        sol = odeint(self.ode_system, initial_conds, self.t)
        V_m = sol[:, 0]
        m = sol[:, 1]
        h = sol[:, 2]
        n = sol[:, 3]
        ina = self.I_Na(V_m, m, h)
        ik = self.I_K(V_m, n)
        il = self.I_L(V_m)
        iinj = [self.I_inj(t) for t in self.t]
        
        if viz:
            fig, ax = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(8, 10))
            ax[0].plot(self.t, V_m)
            ax[0].set_ylabel('$V$ [mV]')
            ax[0].grid()

            ax[1].plot(self.t, ina, label='$I_{Na}$')
            ax[1].plot(self.t, ik, label='$I_{K}$')
            ax[1].plot(self.t, il, label='$I_{L}$')
            ax[1].set_ylabel('$I$ [$\\mu$A]')
            ax[1].legend()
            ax[1].grid()

            ax[2].plot(self.t, m, label='$m$')
            ax[2].plot(self.t, h, label='$h$')
            ax[2].plot(self.t, n, label='$n$')
            ax[2].set_ylabel('Gating activation')
            ax[2].legend()
            ax[2].grid()

            ax[3].plot(self.t, iinj)
            ax[3].set_xlabel('$t$ [ms]')
            ax[3].set_ylabel('$I_{inj}$ [$\\mu$A $\cdot$ $cm^{-2}$]')
            ax[3].grid()

            plt.tight_layout()
            plt.show()
        
        if ret:
            return (V_m, m, h, n, ina, ik, il, iinj)