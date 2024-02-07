#Source: https://rateslib.readthedocs.io/en/latest/z_swpm.html#cook-swpm-doc
#SOFRCURVE: #https://github.com/veridelisi/PythonShortCodes/new/main/CFA/Graph/sofrzerocurve.jpg

pip install rateslib
pip install solver
import pandas as pd
from rateslib import *

# 6 February 2024 SOFR Market Rates : Curve 490
data = pd.DataFrame({
    "Term": ["1W", "2W", "3W", "1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M", "9M", "10M", "11M", "12M", "18M", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y", "10Y", "12Y", "15Y", "20Y", "25Y", "30Y", "40Y", "50Y"],
    "Rate": [5.31600, 5.31728, 5.31950, 5.32340, 5.32750, 5.32250, 5.29360, 5.24886, 5.20773, 5.15769,5.10760, 5.05860,5.00365, 4.95200, 4.89506, 4.54145, 4.30220, 4.02810, 3.89550, 3.82646, 3.79230, 3.77327, 3.76390, 3.76185, 3.76315, 3.77600, 3.79400, 3.77500, 3.69700, 3.61000, 3.41500, 3.20710]
})

#Please add 2 days for settlement
data["Termination"] = [add_tenor(dt(2024, 2, 8), _, "F", "nyc") for _ in data["Term"]]

#Show Market Rates with termination 
with pd.option_context("display.float_format", lambda x: '%.6f' % x):
    print(data)
  
#Create sofr curve dt(2024, 2, 6) : 6 February 2024
sofr = Curve(
    id="sofr",
    convention="Act360",
    calendar="nyc",
    modifier="MF",
    interpolation="log_linear",
    nodes={
        **{dt(2024, 2, 6): 1.0},  # <- this is today's DF,
        **{_: 1.0 for _ in data["Termination"]},
    }
)
sofr_args = dict(effective=dt(2024, 2, 8), spec="usd_irs", curves="sofr")
solver = Solver(
    curves=[sofr],
    instruments=[IRS(termination=_, **sofr_args) for _ in data["Termination"]],
    s=data["Rate"],
    instrument_labels=data["Term"],
    id="us_rates",
)

#Print Data
data["DF"] = [float(sofr[_]) for _ in data["Termination"]]

with pd.option_context("display.float_format", lambda x: '%.6f' % x):
    print(data)
