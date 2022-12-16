import datetime as dt
import os
import yaml

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def fit_p_rx(d, p_rx, deg, info=False):
    """Return linear or polynomial fit for a given 1-d array of power
    measured on the receiver end.

    Parameters
    ----------
    d : numpy.ndarray
        the independent distances where the power is measured
    p_rx : numpy.ndarray
        the dependent data - power values
    deg : int
        the degree of fit
    info : bool, optional
        if set to True, additional info on goodness-of-fit will be
        returned

    Returns
    -------
    popt : tuple
        fitted parameters of length `N`, where `N` is dependant of
        the given degree
    gof : tuple, optional
        goodness-of-fit measure; for `deg`=1, `gof` contains R squared
        value, p value and standard error measure; for `deg`=2, `gof`
        contains uncertainty for each fitted parameter
    """
    if deg==1:
        bias, intercept, r2, p_value, std_err = linregress(d, p_rx)
        popt = (bias, intercept)
        gof = (r2, p_value, std_err)
    elif deg==2:
        popt, pcov = np.polyfit(d, p_rx, deg=deg, full=False, cov=True)
        popt = tuple(popt)
        gof = tuple(np.sqrt(np.diag(pcov)))
    else:
        raise ValueError('degree must be an integer in [1, 2]')
    if info:
        return popt, gof
    return popt


def RMSE(y_true, y_pred):
    """Return the root mean square distance between the actual values
    and fitted values.

    Parameters
    ----------
    y_true : numpy.ndarray
        true, measured values
    y_pred : numpy.ndarray
        predicted or fitted values
    
    Returns
    -------
    float
        root mean square error
    """
    return float(np.sqrt(np.mean((y_true - y_pred)**2)))


def loss_free_space_empirical(f, d, G_tx, G_rx):
    """Return the loss in free space in dB.

    Parameters
    ----------
    f : float
        frequency [MHz]
    d : float or numpy.ndarray
        tx-to-rx distance(s) in meters
    G_tx : float
        tx antenna gain in dBi
    G_rx : float
        rx antenna gain in dBi
    """
    return 32.5 + (20*np.log10(f)) + (20*np.log10(d/1000)) - (G_tx + G_rx)


def run():
    with open('set_input.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # input config
    p_tx = config['transmitted_power']
    f = config['operating_frequency']
    g_tx =  config['tx_antenna_gain']
    g_rx = config['rx_antenna_gain']
    d = config['rx_power_to_distance']['distance']
    d = np.asarray(d, dtype=np.float32)
    p_rx = config['rx_power_to_distance']['rx_power']
    p_rx = np.asarray(p_rx, dtype=np.float32)
    save_fig = config['save_fig']
    # fitting config
    deg = config['degree']
    info = config['additional_info']

    # fitting the data
    if info:
        popt, gof = fit_p_rx(d, p_rx, deg, info)
    else:
        popt = fit_p_rx(d, p_rx, deg, info)

    if deg == 1:
        n = popt[0]
        p_rx_fit = popt[0]*d + popt[1]
        p_rx_rmse = RMSE(p_rx, p_rx_fit)
        if info:
            r2, p_value, std_err = gof
            p_rx_fit_ub = p_rx_fit * (1 + std_err)
            p_rx_fit_lb = p_rx_fit * (1 - std_err)
    elif deg == 2:
        n = np.mean(popt[:2])
        p_rx_fit = popt[0]*d**2 + popt[1]*d + popt[2]
        p_rx_rmse = RMSE(p_rx, p_rx_fit)
        print(gof)
        if info:
            p_rx_fit_ub = (popt[0] + gof[0])*d**2 \
                        + (popt[1] + gof[1])*d \
                        + (popt[2] + gof[2])
            p_rx_fit_lb = (popt[0] - gof[0])*d**2 \
                        + (popt[1] - gof[1])*d \
                        + (popt[2] - gof[2])

    # calculating free space approx. loss vs empirical loss
    a_fs = loss_free_space_empirical(f, d, g_tx, g_rx)
    a_emp = p_tx - p_rx
    a_rmse = RMSE(a_emp, a_fs)

    # data viz
    fig, ax = plt.subplots(2, sharex=True, figsize=(8, 6))
    ax[0].plot(d, p_rx, 'o-', color='red', label='$P_{rx}$, measured ')
    ax[0].plot(d, p_rx_fit, 's--', color='green', label='linear fit')
    ax[0].fill_between(d, p_rx_fit_lb, p_rx_fit_ub, color='green', alpha=0.2,
        label='leastsq standard error')
    ax[0].plot(d, -2*d + popt[1], '-.', color='black', label='free space, $n=2$')
    ax[0].set_ylabel('$P_{rx}$ [dBm]')
    ax[0].legend(loc='lower left')
    if info and deg==1:
        ax[0].set_title(
            f'polynomial degree = {deg}; '
            f'RMSE = {round(p_rx_rmse, 2)} dB; '
            f'$R^2$ = {round(np.abs(r2), 2)}, $p$ = {round(p_value, 4)}')
    elif info and deg==2:
        ax[0].set_title(
            f'polynomial degree = {deg}; '
            f'RMSE = {round(p_rx_rmse, 2)} dB')

    ax[1].plot(d, a_fs, 'o-', color='red', label='free space loss')
    ax[1].plot(d, a_emp, 's-', color='green', label='measured loss')
    ax[1].set_xlabel('$d$ [m]')
    ax[1].set_ylabel('$a$ [dB]')
    ax[1].legend()
    ax[1].set_title(
        f'$n$ = {round(np.abs(n), 2)}; '
        F'RMSE = {round(a_rmse, 2)} dB')

    ax[0].grid()
    ax[1].grid()
    
    if save_fig:
        fname = dt.datetime.now().strftime('%y%m%d_%H%M%S')
        fig.savefig(os.path.join('output', 'propagation_constant_' + fname + '.pdf'), bbox_inches='tight', format='pdf')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
