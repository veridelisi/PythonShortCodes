#https://github.com/veridelisi/PythonShortCodes/new/main/CFA/Graph/sofrzerocurve.jpg

![alt text](https://github.com/[veridelisi/[PythonShortCodes/CFA]/blob/[Graph]/sofrzerocurve.jpg?raw=true)

import datetime
import numpy as np

# Update the spot rate and daydiff values
spot_rate = 0.0531600


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 2, 15)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded


# Update the spot rate
spot_rate = 0.0531728


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 2, 22)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded


# Update the spot rate
spot_rate = 0.053195


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 2, 29)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded

# Update the spot rate
spot_rate = 0.0532340


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 3, 8)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded


# Update the spot rate
spot_rate = 0.0532750


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 4, 8)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded


# Update the spot rate
spot_rate = 0.0532250


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 5, 8)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded

# Update the spot rate
spot_rate = 0.0529360


# Calculate the continuously compounded discount factor
# Define the dates for the calculation
te = datetime.datetime(2024, 6, 10)  # End date
ts = datetime.datetime(2024, 2, 8)   # Start date
t = datetime.datetime(2024, 2, 6)  # Reference date

# Calculate day differences
daydiff_te_ts = (te - ts).days
daydiff_te_t = (te - t).days

# Compute the continuously compounded discount factor using the zero rate
zero_1 = -np.log(1 / (1 + spot_rate * daydiff_te_ts / 360)) / (daydiff_te_ts / 360)
discount_factor_continuously_compounded = np.exp(-zero_1 * daydiff_te_t / 360)

discount_factor_continuously_compounded
