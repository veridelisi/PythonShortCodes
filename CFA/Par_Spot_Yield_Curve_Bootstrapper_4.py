# https://github.com/jrvarma/bond_pricing
# pip install bond_pricing

from numpy import (array, arange, empty_like, vectorize,  # noqa E401
                   ceil, log, exp, interp, nan, where, dot,
                   concatenate)
import numpy as np
from bond_pricing.simple_bonds import bond_coupon_periods, equiv_rate
from bond_pricing.utils import newton_wrapper, dict_to_dataframe
from bond_pricing.no_scipy_workarounds import no_scipy

def par_yld_to_zero(par, freq=1, return_dataframe=False):
    r"""Bootstrap a complete par bond yield curve to zero

    Parameters
    ----------
    par : sequence of floats
          The par bond yields for various maturities in decimal
          Maturities are spaced 1/freq years apart
    freq : int, optional
          The coupon frequency (equals compounding frequency)
    return_dataframe : bool, optional
         whether to return pandas DataFrame instead of dict
    Returns
    -------
    dict or DataFrame:

          zero_yields: array of zero yields in decimal

          zero_prices: array of zero prices

          forward_rates: array of forward rates in decimal

          (Maturities are spaced 1/freq years apart)

    Examples
    --------
    >>> par_yld_to_zero(
    ... par=[1.0200e-2, 1.2000e-2, 1.4200e-2, 1.6400e-2, 1.9150e-2,
    ...      2.1900e-2, 2.4375e-2, 2.6850e-2, 2.9325e-2, 3.1800e-2],
    ... freq=2, return_dataframe=True)
       zero_yields  zero_prices  forward_rates
    0     0.010200     0.994926       0.010200
    1     0.012005     0.988102       0.013812
    2     0.014220     0.978970       0.018656
    3     0.016445     0.967776       0.023133
    4     0.019245     0.953245       0.030487
    5     0.022068     0.936279       0.036242
    6     0.024630     0.917891       0.040066
    7     0.027218     0.897504       0.045429
    8     0.029837     0.875223       0.050915
    9     0.032492     0.851159       0.056545

    """
    annuity = 0
    prev_zero = 1
    zp = empty_like(par)
    zyld = empty_like(par)
    fwd = empty_like(par)
    for i, cpn in enumerate(par):
        n = i + 1
        pv_intermediate = annuity * cpn/freq
        pv_final = 1 - pv_intermediate
        zero_price = pv_final / (1 + cpn/freq)
        zp[i] = zero_price
        zyld[i] = (zero_price**(-1.0/n) - 1) * freq
        fwd[i] = (prev_zero / zero_price - 1) * freq
        prev_zero = zero_price
        annuity += zero_price
    result = dict(zero_yields=zyld, zero_prices=zp, forward_rates=fwd)
    if return_dataframe:
        return dict_to_dataframe(result)
    else:
        return result

par_yld_to_zero(
    par=[0.02, 0.024, 0.0276, 0.030840, 0.033756, 0.036380],freq=2, return_dataframe=True)
