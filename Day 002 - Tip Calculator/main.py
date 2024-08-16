print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give in percentage? "))
people = int(input("How many people to split the bill? "))

tip = total_bill / 100 * tip_percentage
total_with_tip = total_bill + tip
total_per_person = round(total_with_tip / people, 2)

print(f"Each person should pay: ${total_per_person}")