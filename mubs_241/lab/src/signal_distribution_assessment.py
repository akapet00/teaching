import datetime as dt
import os
import yaml

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rice
from scipy.stats import kstest


def ecdf(p_rx):
    """Returnc cumulative distribution function of measured power.

    Parameters
    ----------
    p_rx : numpy.ndarray
        power values

    Returns
    -------
    x : numpy.ndarray
        sorted power values
    y : numpy.ndarray
        cumulative distribution of power
    """
    n = p_rx.size
    x = np.sort(p_rx)
    y = np.arange(1, n+1) / n
    return x, y


def run():
    with open('set_input.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # input config
    p_rx = config['rx_power_to_distance']['rx_power']
    p_rx = np.asarray(p_rx, dtype=np.float32)
    save_fig = config['save_fig']

    x_emp, cdf_emp = ecdf(p_rx)
    x_gaussian, cdf_gaussian = ecdf(np.random.normal(np.mean(p_rx),
        np.std(p_rx), 1000))
    gauss_statistic, gauss_pvalue = kstest(p_rx, 'norm',
        args=(np.mean(p_rx), np.std(p_rx)))

    b, loc, scale = rice.fit(p_rx)
    rice_rvs = rice.rvs(b, loc, scale, size=1000)
    x_rician, cdf_rician = ecdf(rice_rvs)
    rice_statistic, rice_pvalue = kstest(p_rx, 'rice', args=(b, loc, scale))

    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10, 4))
    ax[0].plot(x_emp, cdf_emp, 'r.', label='$P_{rx}$, measured')
    ax[0].plot(x_gaussian, cdf_gaussian, 'k-', label='normal distribution')
    ax[0].text(0.45, 0.25, (
        f'Kolmogorov-Smirnov test: \n'
        f'test statistics = {round(gauss_statistic, 2)} \n'
        f'p value = {round(gauss_pvalue, 2)}'),
        transform=ax[0].transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax[0].set_xlabel('$P_{rx}$ [dBm]')
    ax[0].set_ylabel('CDF')
    ax[0].legend()
    ax[0].grid()

    ax[1].plot(x_emp, cdf_emp, 'r.', label='$P_{rx}$, measured')
    ax[1].plot(x_rician, cdf_rician, 'k-', label='Rice distribution')
    ax[1].text(0.45, 0.25, (
        f'Kolmogorov-Smirnov test: \n'
        f'test statistics = {round(rice_statistic, 2)} \n'
        f'p value = {round(rice_pvalue, 2)}'),
        transform=ax[1].transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax[1].set_xlabel('$P_{rx}$ [dBm]')
    ax[1].legend()
    ax[1].grid()

    if save_fig:
        fname = dt.datetime.now().strftime('%y%m%d_%H%M%S')
        fig.savefig(os.path.join('output', 'channel_distribution_' \
            + fname + '.pdf'), bbox_inches='tight', format='pdf')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()