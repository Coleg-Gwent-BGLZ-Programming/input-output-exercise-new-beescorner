# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")

# Ask the customer for their name

name = input("What is your name? ")
# Ask how many smoothies they want (convert to integer)

smoothies = int(input("How many smoothies would you like to buy? "))

# Calculate the total cost (each smoothie is £3.50)

price_per_smoothie = 3.50
total_cost = smoothies * price_per_smoothie

# Ask if they want a reusable cup (£1 extra)

cup = input("Would you like to add a reusable cup for £1 extra? (yes/no) ").strip(). lower()
if cup == "yes":
   total_cost +1
   cup_message = "Reusable cup added (£1)."
else:
   cup_message = "No reusable cup added."
  
# Display the message

print(f"\nThank you, {name}!")
print(f"You ordered {smoothies} smoothie(s).")
print(cup_message)
print(f"Your total cost is £{total_cost:.2f}")
