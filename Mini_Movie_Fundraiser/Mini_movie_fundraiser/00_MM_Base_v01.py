
#asks the user a question and checks whether their anwer is a valid response or not

def choice_check(question, valid_answer, error):
    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[0] or response == word:
                return word

        print(error)
        print()

#no. of tickets to sell
MAX_TICKETS = 3


#loop for selling the tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter your name or type 'xxx' to quit")

    if name == 'xxx':
        break

    tickets_sold += 1

#outputs no. of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congrats, you have sold all the tickets!")

else:
    print("you have sold {} ticket/s, with {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))

