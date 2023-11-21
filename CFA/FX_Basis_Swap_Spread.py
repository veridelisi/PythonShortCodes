from datetime import date, timedelta

# Define dates
start_dt = date(2023, 10, 11)
#settle_dt = start_dt + timedelta(days=2)  # Spot settles T+2 (in this case)
end_dt = date(2024, 1, 12)
days = (end_dt - start_dt).days + 2


# Define input data
spot_bid = 1.0599
fwd_bid = 1.064748

usd_yld_bid = 0.056683
eur_yld_bid = 0.038785

# Compute implied yield
print("Days to expiry =", days)
paper = 360 / days * (fwd_bid / spot_bid * (1 + eur_yld_bid * days / 360)) - 1
print("Wrong Formula Implied USD Yield =", paper)
cip_solved = 360 / days * (fwd_bid / spot_bid * (1 + eur_yld_bid * days / 360) - 1)
print("Correct Formula Implied USD Yield =", cip_solved)
print("USD Implied Yield Pct =", round(cip_solved * 100, 4))
print("Spread Bid =", round((cip_solved - usd_yld_bid) * 100, 4))


#https://veridelisi.hashnode.dev/indicator-of-stress-in-us-dollar-funding
