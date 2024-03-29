#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
# print(input ("What was the total bill? $"))
# print(input("What percentage tip would you like to give? 10, 12, or 15? "))
# print(input("How many people to split the bill? "))

# print(input("Each person should pay: $"))

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


final_bill = bill * (tip / 100 + 1)


payment = final_bill / people
final_amount = round(payment, 2)

print(f"Each person should pay: ${final_amount}")

