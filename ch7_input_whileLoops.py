# string = 'string' * 5
# print(string)

# message = input("Tell me something: ")
# print(message)

# # --------------
# height = input("\nHow tall are you in inches? ")
# height = int(height)

# if height >= 48:
#     print("\tYou're tall enough to ride!")
# else:
#     print("\tSorry, you'll be able to ride when you're a little older.")

# ---------------
# EXERCISE 7-1:
# car = input("What kind of rental car would you like to rent? ")
# print(f"\tLet me see if we have a {car.title()} in stock for you.")

# # ---------------
# # EXERCISE 7-2:
# group = input("\nHow many people are in your dinner group? ")
# group = int(group)

# if group > 8:
#     print("\tFor that size group, the wait will be about 30 minutes.")
# else:
#     print("\tGreat, we have a table available for you now.")

# # ---------------
# # EXERCISE 7-3
# number = input("\nEnter a number, and I'll tell you if it's divisible by 10: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"\tThe number {number} is divisible by 10!")
# else:
#     print(f"\tThe number {number} is not divisible by 10.")

# ---------------
# age = int(input("Please enter your age: "))
# birthday = input(
#     "Have you had a birthday yet this year? Please enter y or n: ")

# if birthday == "n":
#     year = (99 - age) + 2021
#     print(f"\tYou will turn 100 in the year {year}")
# if birthday == "y":
#     year = (100 - age) + 2021
#     print(f"\tYou will turn 100 in the year {year}")


# practicing stoping an infinite while loop
# x = 1
# while x <= 5:
#     print(x)


# --------------------
# EXERCISE 7-4:
# prompt = "\nPlease enter a topping you'd like to add to your pizza"
# prompt += "\nType 'quit' when you're finished adding toppings: "

# pizza_topping = ""
# while pizza_topping != "quit":
#     pizza_topping = input(prompt)
#     if pizza_topping == 'quit':
#         break
#     else:
#         print(f"\t{pizza_topping.title()} has been added to your pizza.")

# - or same thing can be written as, but this doesn't work in this case or eles when user types 'quit' it gets printed in the message still
# prompt = "\nPlease enter a topping you'd like to add to your pizza"
# prompt += "\nType 'quit' when you're finished adding toppings: "

# pizza_topping = ""
# while pizza_topping != "quit":
#     pizza_topping = input(prompt)
#     print(f"\t{pizza_topping.title()} has been added to your pizza.")

# ----------------
# EXERCISE 7-5:
# movie_ticket = int(input(
#     "Hello, to find out the price of your movie ticket, please enter your age: "))

# if movie_ticket < 3:
#     print(f"\nYour ticket is free!")
# elif movie_ticket <= 12:
#     print(f"\nYour ticket is $10.")
# else:
#     print(f"\nYour ticket is $15.")

# - now do it with a while loop:
# prompt = "Hello, to find out the price of a movie ticket, please enter your age"
# prompt += "\nPlease type 'quit' when you're done. "

# while True:
#     age = input(prompt)
#     if age == "quit":
#         break
#     age = int(age)

#     if age < 3:
#         print(f"\tYour ticket is free!")
#     elif age <= 12:
#         print(f"\tYour ticket is $10.")
#     else:
#         print(f"\tYour ticket is $15.")


# ------------------
# EXERCISE 7-6, now do it using an active variable:
# prompt = "Hello, to find out the price of a movie ticket, please enter your age"
# prompt += "\nPlease type 'quit' when you're done. "

# active = True
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)

#         if age < 3:
#             print(f"\tYour ticket is free!")
#         elif age <= 12:
#             print(f"\tYour ticket is $10.")
#         else:
#             print(f"\tYour ticket is $15.")


# ---------------------
# -- example in book of Moving items from one list to another using while loop
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

#     print("\nThe following users have been confirmed:")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())


# --------------------
# EXERCISE 7-8:
# make a list of sandwich orders, and an empty finished sandwiches list and move sandwiches from the orders list into the finished list when they're done being made and print list of finished sandwiches:

# sandwich_orders = ['blt', 'tuna', 'turkey club', 'meatball sub']
# finished_sandwiches = []

# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print(f"\nYour {current_order} sandwich is being made.")

#     finished_sandwiches.append(current_order)

#     print("\nThe following sandwiche(s) are ready:")
#     for sandwich in finished_sandwiches:
#         print(f"{sandwich.title()}")


# -------------------
# EXERCISE 7-9:
# Using same lists as above, list one sandwich type 3 times and then say you're out of that type of sandwich and remove it from the list usinga while loop. Then run rest of program and ensure tuna was removed:

# sandwich_orders = ['blt', 'tuna', 'turkey club',
#                    'tuna', 'meatball sub', 'tuna']
# finished_sandwiches = []

# print("We apologize, but we are currently all out of tuna for the day.")
# while 'tuna' in sandwich_orders:
#     sandwich_orders.remove('tuna')


# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print(f"\nYour {current_order} sandwich is being made.")

#     finished_sandwiches.append(current_order)

#     print("\nThe following sandwiche(s) are ready:")
#     for sandwich in finished_sandwiches:
#         print(f"{sandwich.title()}")


# --------------------
# EXERCISE 7-10:
# Make a poll that asks users about their dream vacation and then print results of the poll -- use a while loop and store the information collected in a dictionary:

poll_responses = {}

polling_active = True

while polling_active:
    # prompt for user's name and their response:
    name = input("\nWhat is your name? ")
    response = input(
        "If you could visit any one place in the world, where would you go? ")

    # Store the responses in the dictionary
    poll_responses[name] = response

    # ask if others are going to take the poll, if not, then stop loop
    question = input(
        "Would you like to let another person respond to the poll? (yes or no): ")
    if question == "no":
        polling_active = False

# when polling is completed, print results
print(f"\n--- Poll Results ---")
for name, response in poll_responses.items():
    print(f"{name.title()} would like to visit {response.title()}")
