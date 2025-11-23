print("Welcome to my Python program!")

savings = input("How many dollars did you save this month? ")

try:
  savings = float(savings)
except ValueError:
  print("Please enter a valid number.")
  exit()

yearly_savings = savings * 12

print(f"You are predicted to save {yearly_savings} dollars this year.")
