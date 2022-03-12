import random
options = ["rock", "paper", "scissors"]


def rockPaperScissors():
    option = random.choices(options)
    return(option)


# print(rockPaperScissors())
