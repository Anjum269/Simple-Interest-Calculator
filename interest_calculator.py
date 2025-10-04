# interest_calculator.py

# Formula: SI = (P * R * T) / 100

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print(f"Simple Interest: ₹{SI}")
