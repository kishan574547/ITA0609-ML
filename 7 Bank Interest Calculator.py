principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = int(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate / 100) ** time - principal
print("Simple Interest =", simple_interest)
print("Compound Interest =", round(compound_interest, 2))