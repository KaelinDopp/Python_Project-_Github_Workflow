#Display a welcome message.
print("Welcome to my Python program!")

#Creates a variable for savings and asks user for their monthly savings.
savings = input("How many dollars did you save this month? ")

#Creates an error handling by presenting an error and correction method if the input is not a number.
try:
  savings = float(savings)
except ValueError:
  #Displays the correction statement to the user.
  print("Please enter a valid number.")
  exit()

#Multi[lies the input monthly savings by 12 due to the 12 months in a year to predict yearly savings.
yearly_savings = savings * 12

#Displays the predicted yearly savings based of previous calculations.
print(f"You are predicted to save {yearly_savings} dollars this year.")
