from finance_tools.loan import calculate_emi
from finance_tools.tax import calculate_tax

# TAX CALCULATOR
print("===== TAX CALCULATOR =====")

income = float(input("Enter your annual income: "))
tax_rate = float(input("Enter your tax rate (%): "))

tax = calculate_tax(income, tax_rate)

print(f"Your calculated tax is: {tax:.2f}")

# LOAN EMI CALCULATOR
print("\n===== LOAN EMI CALCULATOR =====")

principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period (years): "))

emi = calculate_emi(principal, annual_rate, years)

print(f"Your monthly EMI is: {emi:.2f}")