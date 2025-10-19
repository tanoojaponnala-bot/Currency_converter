# Simple Currency Converter (INR to USD, EUR, GBP, JPY)

print("💰 Welcome to the INR Currency Converter 💰")
print("--------------------------------------------")

# Get amount in INR from user
inr = float(input("Enter amount in INR: "))

# Static exchange rates (you can update these anytime)
usd_rate = 0.012     # 1 INR = 0.012 USD
eur_rate = 0.011     # 1 INR = 0.011 EUR
gbp_rate = 0.0095    # 1 INR = 0.0095 GBP
jpy_rate = 1.77      # 1 INR = 1.77 JPY

# Convert INR to other currencies
usd = inr * usd_rate
eur = inr * eur_rate
gbp = inr * gbp_rate
jpy = inr * jpy_rate

# Display results
print("\nConverted Amounts:")
print(f"💵 USD  : {usd:.2f}")
print(f"💶 EUR  : {eur:.2f}")
print(f"💷 GBP  : {gbp:.2f}")
print(f"💴 JPY  : {jpy:.2f}")

print("\nThank you for using the converter! 😊")