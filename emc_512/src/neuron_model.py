import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pprint


class HodgkinHuxley(object):
    """Full Hodgkin-Huxley Model implementation.

    For more details and original implementation, visit: 
    https://hodgkin-huxley-tutorial.readthedocs.io/en/latest
    """
    def __init__(self, C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, I_inj=None, T=6.3):
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
        I_inj : callable, optional
            Injected current [uA/cm^2]
        T : float, optional
            Temperature of the environment in which the neuron is
            located [°C]

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
        if I_inj:
            assert callable(I_inj), 'external current must be callable'
            self.I_inj = I_inj
        else:
            self.I_inj = lambda t: 10*(t>100) - 10*(t>200) + 35*(t>300) - 35*(t>400)   
        self.T = T

    def temp_scaler(self, T):
        """Return the value of the closing rate scaler for a given
        temperature of the environment in which neuron is located.
        
        Parameters
        ----------
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            closing rate scaler for a given temperature
        """
        return 3**((T-6.3)/10)

    def alpha_m(self, V_m, T):
        """Return the value of the alpha_m parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            alpha_m value
        """
        return 0.1 * self.temp_scaler(T) * (V_m+40.0) \
            / (1.0-np.exp(-(V_m+40.0)/10.0))

    def beta_m(self, V_m, T):
        """Return the value of the beta_m parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            beta_m value
        """
        return 4.0 * self.temp_scaler(T) * np.exp(-(V_m+65.0)/18.0)

    def alpha_h(self, V_m, T):
        """Return the value of the alpha_h parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            alpha_h value
        """
        return 0.07 * self.temp_scaler(T) * np.exp(-(V_m+65.0)/20.0)

    def beta_h(self, V_m, T):
        """Return the value of the beta_h parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            beta_h value
        """
        return self.temp_scaler(T) / (1.0+np.exp(-(V_m+35.0)/10.0))

    def alpha_n(self, V_m, T):
        """Return the value of the alpha_n parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            alpha_n value
        """
        return 0.01 * self.temp_scaler(T) * (V_m+55.0) \
            / (1.0-np.exp(-(V_m+55.0)/10.0))

    def beta_n(self, V_m, T):
        """Return the value of the beta_n parameter.
        
        Parameters
        ----------
        V_m : float
            Membrane potential [mV]
        T : float
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        float
            beta_n value
        """
        return 0.125 * self.temp_scaler(T) * np.exp(-(V_m+65)/80.0)

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

    def basic_HH(self, initial_conds, t, T):
        """Hodgkin Huxley model based on a set of four coupled ODEs.
        
        For details, go to:
        https://en.wikipedia.org/wiki/Hodgkin-Huxley_model

        Parameters
        ----------
        initial_conds : list
            Initial conditions for resting membrane potential and m, h
            and n activation variables
        t : numpy.ndarray
            A sequence of time points for which to solve for y
        T : float, optional
            Temperature of the environment in which the neuron is
            located [°C]
            
        Returns
        -------
        tuple
            Membrane potential and m, h adn n activation variables
        """
        V_m, m, h, n = initial_conds

        dV_mdt = (self.I_inj(t) - self.I_Na(V_m, m, h) - self.I_K(V_m, n) \
                - self.I_L(V_m)) / self.C_m
        dmdt = self.alpha_m(V_m, T)*(1.0-m) - self.beta_m(V_m, T)*m
        dhdt = self.alpha_h(V_m, T)*(1.0-h) - self.beta_h(V_m, T)*h
        dndt = self.alpha_n(V_m, T)*(1.0-n) - self.beta_n(V_m, T)*n
        return (dV_mdt, dmdt, dhdt, dndt)

    def induction_HH(self, initial_conds, t, T, a, b, k, k_1, k_2):
        """Hodgkin Huxley model of neuron exposed to magnetic field from TMS coil.

        Parameters
        ----------
        initial_conds : list
            Initial conditions for resting membrane potential and m, h and n activation variables
        t : numpy.ndarray
            A sequence of time points for which to solve for y
        T : float, optional
            Temperature of the environment in which the neuron is
            located [°C]
        a, b, k, k_1, k_2 : float
            Additional arguments for the magnetic flux dynamics equation
            
        Returns
        -------
        tuple
            Membrane potential and m, h adn n activation variables
        """
        V_m, phi, m, h, n = initial_conds

        dV_mdt = (self.I_inj(t) - self.I_Na(V_m, m, h) - self.I_K(V_m, n) \
            - self.I_L(V_m) - k*V_m*(a + 3*b*phi**2)) / self.C_m
        dmdt = self.alpha_m(V_m, T)*(1.0-m) - self.beta_m(V_m, T)*m
        dhdt = self.alpha_h(V_m, T)*(1.0-h) - self.beta_h(V_m, T)*h
        dndt = self.alpha_n(V_m, T)*(1.0-n) - self.beta_n(V_m, T)*n
        dphidt = k_1*V_m - k_2*phi
        return (dV_mdt, dmdt, dhdt, dndt, dphidt)
    
    def simulate(self, initial_conds, t, induction_params=None,
            ret=False, viz=False):
        """Run simulation.

        Parameters
        ----------
        initial_conds : list
            Initial conditions for resting membrane potential and m, h
            and n activation variables
        t : numpy.ndarray
            A sequence of time points for which to solve for y
        induction_params : tuple, optional
            Additional arguments for electrical induction.
            If `induction_params` are specified, `induction_HH` is used.    
        ret : bool, optional
            If True, calculated electrical parameters will be returned
        viz : bool, optional
            If True, simulation will be visualized
        
        Returns
        -------
        tuple or None
            if `ret` is set to True, tuple containg membrane potential,
            activation functions and currents will be returned
        """
        self.t = t
        if induction_params:
            sol = odeint(self.induction_HH, initial_conds, self.t,
                args=(self.T, *induction_params))
        else:
            sol = odeint(self.basic_HH, initial_conds, self.t, 
                args=(self.T, ))
        V_m = sol[:, 0]
        m = sol[:, 1]
        h = sol[:, 2]
        n = sol[:, 3]
        if induction_params:
            phi = sol[:, 4]
        ina = self.I_Na(V_m, m, h)
        ik = self.I_K(V_m, n)
        il = self.I_L(V_m)
        iinj = np.array([self.I_inj(t) for t in self.t])
        
        if viz:
            _, ax = plt.subplots(nrows=4, ncols=1, sharex=True,
                figsize=(8, 10))
            ax[0].plot(self.t, V_m)
            ax[0].set_ylabel(r'$V$ [mV]')
            ax[0].grid()

            ax[1].plot(self.t, ina, label=r'$I_{Na}$')
            ax[1].plot(self.t, ik, label=r'$I_{K}$')
            ax[1].plot(self.t, il, label=r'$I_{L}$')
            ax[1].set_ylabel(r'$I$ [$\mu$A]')
            ax[1].legend()
            ax[1].grid()

            ax[2].plot(self.t, m, label=r'$m$')
            ax[2].plot(self.t, h, label=r'$h$')
            ax[2].plot(self.t, n, label=r'$n$')
            ax[2].set_ylabel(r'Gating activation')
            ax[2].legend()
            ax[2].grid()

            ax[3].plot(self.t, iinj)
            ax[3].set_xlabel(r'$t$ [ms]')
            ax[3].set_ylabel(r'$I_{inj}$ [$\mu$A $\cdot$ $cm^{-2}$]')
            ax[3].grid()

            plt.tight_layout()
            plt.show()
        
        if ret:
            if induction_params:
                return (V_m, phi, m, h, n, ina, ik, il, iinj)
            return (V_m, m, h, n, ina, ik, il, iinj)