import pandas
import random


def word_input_checker(question, num_letter, valid_answer):

    error = f"please choose {valid_answer[0]} or {valid_answer[1]}"

    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[:num_letter] or response == word:
                return word

        print(error)
        print()


def currency(x):
    return "${:.2f}".format(x)


# no. of tickets to sell
MAX_TICKETS = 7

# no. of tickets user has sold
tickets_sold = 0

# the total amount of profit
profit = 0

# price of a ticket
price = 0

# variables to be used later
age = 0
name = ""
payment_method = ["cash", "credit"]

# data lists for table of results
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used when formatting table
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# main here
while tickets_sold < MAX_TICKETS:

    # asks the user for their name
    while name == "":
        name = input("please enter your name or type 'xxx' to quit \n")

        if name == "":
            print("this cannot be blank, try again \n")

    # early exit code
    if name == 'xxx':
        break

    while True:

        try:

            # asks user for their age
            age = int(input("so {} how many years old are you? \n".format(name)))

            if 12 <= age <= 120:
                ticket_valid = "yes"
                break

            else:
                ticket_valid = "no"
                name = ""
                break

        except ValueError:
            print("please enter a whole number")

    # compares age with the ticket prices
    if ticket_valid == "yes":
        if age <= 15:
            price = 7.50

        elif age <= 65:
            price = 10.50

        else:
            price = 6.50

        tickets_sold += 1

    # if you're too old, or too young this bit prints a
    elif ticket_valid == "no":

        if age > 120:

            print("that looks to be a typo, try again")

        else:
            print("you're too young for this movie")
            name = ""

        continue

    cash_cred = word_input_checker("will you pay with cash or credit? (ca/cr is acceptable) \n",
                                   2, payment_method,)

    if cash_cred == "credit":
        surcharge = price * 0.05
    else:
        surcharge = 0

    profit += price

    # this chunk prints a ticket price
    if ticket_valid == "yes":
        print(f"your ticket will cost ${price + surcharge:.2f}")

    else:
        print("you dont get a ticket")

    all_names.append(name)
    all_ticket_costs.append(price)
    all_surcharge.append(surcharge)

    # resets name for next loop
    name = ""

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the ticket and profit totals
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame["Profit"].sum()

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# picks a random person to be a winner
winner_name = random.choice(all_names)

# get the information of the winner
winner_index = all_names.index(winner_name)

# Finds the amount of money won
total_won = mini_movie_frame.at[winner_index, 'Total']

print("|>=+---Ticket Data --+=<|")
print()

print(mini_movie_frame)

print()
print("|>=+--- Ticket cost / Profit ---+=<|")

print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))
# outputs no. of tickets sold and total profit
if tickets_sold == MAX_TICKETS:
    print(f"Congrats, you have sold all the tickets! you have gained a profit of {profit:.2f}")

# outputs profit when exit code is used
else:
    print("you have sold {} ticket/s for ${:.2f} total, with {} "
          "ticket/s remaining".format(tickets_sold, profit,
                                      MAX_TICKETS - tickets_sold))


# Set index at the end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

print()
print("|>=+--- Raffle Winner ---+=<|")
print(f"congratulations {winner_name} you have won a free ticket / {total_won}! ")
