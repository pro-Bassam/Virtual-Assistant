import random
import time
from pygame import mixer


cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


def pickCard():
    mixer.init()
    mixer.music.load("data/records/card_shuffle.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {rank[0]} of {card[0]}")


# print(pickCard())
