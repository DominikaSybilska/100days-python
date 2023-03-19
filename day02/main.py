print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_of_ppl = int(input("How many people to split the bill? "))
tip_as_percentage = float(tip/100)
cost_per_person = (total_bill + (total_bill * tip_as_percentage)) / num_of_ppl
final_amount = round(cost_per_person, 2)
message = f"Each person should pay: £{final_amount}"
print(message)