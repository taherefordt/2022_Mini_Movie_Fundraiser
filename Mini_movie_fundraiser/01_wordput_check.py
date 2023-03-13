yeno_answer = ["yes", "no"]


def word_input_checker(question, valid_answer, error):
    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[:1] or response == word:
                return word

        print(error)
        print()


answer = word_input_checker("ye/no?", yeno_answer, "answer y/n!")

print(f"you said {answer}")
