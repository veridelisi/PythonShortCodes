#Show that the two-year spot rate of r(2) = 10% and the three-year spot rate of r(3) = 11% are geometric averages of the one-year spot rate and the forward rates.

# Given spot rates and forward rates
r_1 = 0.09  # One-year spot rate
f_1_1 = 0.1101  # One-year forward rate from year 1 to 1
f_2_1 = 0.1303  # One-year forward rate from year 2 to 1

# Calculate r(2) as the geometric average
r_2= ((( (1+ r_1)    * (1+ f_1_1)   )** (1/2))-1)*100

# Calculate r(3) as the geometric average
r_3= ((( (1+ r_1)    * (1+ f_1_1) * (1+ f_2_1)  )** (1/3))-1)*100

# Result
print(r_2)
print(r_3)

![Screenshot](SpotRatesForwardRates.JPG)
