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


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Assuming dt is an alias for datetime for simplicity
dt = datetime

# Your start date
start_date = dt(2024, 2, 8)

# Define a function to add time based on your term format (e.g., "1W", "2M", "1Y")
def add_time_to_date(start_date, term):
    unit = term[-1]  # Last character (W, M, Y)
    quantity = int(term[:-1])  # All but the last character
    
    if unit == "W":
        return start_date + timedelta(weeks=quantity)
    elif unit == "M":
        return start_date + relativedelta(months=quantity)
    elif unit == "Y":
        return start_date + relativedelta(years=quantity)
    else:
        return None  # For unsupported units

# Your terms
terms = ["1W", "2W", "3W", "1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M", "9M", "10M", "11M", "12M", "18M", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y", "10Y", "12Y", "15Y", "20Y", "25Y", "30Y", "40Y", "50Y"]

# Calculate dates for each term
dates_for_terms = [add_time_to_date(start_date, term) for term in terms]

# Example of how you might print these dates
for term, date in zip(terms, dates_for_terms):
    print(f"{term}: {date.strftime('%Y-%m-%d')}")

# Now, assuming you have a method to get the zero rate for a given date, you would use these dates in that method.
# For example:
zero_rates = [sofr.shift(7).rate(date, "1d") for date in dates_for_terms]
zero_rates
