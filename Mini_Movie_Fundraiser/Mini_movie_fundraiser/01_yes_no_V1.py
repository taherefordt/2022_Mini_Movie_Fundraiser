yeno_answer = ["yes", "no", "yeah", "nah"]


def yes_no(question, valid_answer, error):
    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[0] or response == word:
                return word

        print(error)
        print()

answer = yes_no("y/n?", yeno_answer, "answer y/n!")