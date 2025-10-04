 
# interest_calculator.py

# SI = (P * R * T) / 100
# CI = P * ( (1 + R/100)^T - 1 )

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100
CI = P * ((1 + R / 100) ** T - 1)

print(f"Simple Interest: ₹{SI}")
print(f"Compound Interest: ₹{CI:.2f}")
