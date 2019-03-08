import math
from random import shuffle

num_iterations = 3
start_length = 5
end_length = 10

for length in range(start_length, end_length + 1):
    shuffle_history = []
    print(f"length {length}, max shuffles = {length}! = {math.factorial(length)}")

    for iteration in range(num_iterations):
        print(f"\titeration {iteration}")

        items = []
        history = []
        shuffles = 0
        hasSeenBefore = False

        for i in range(length):
            items.append(i)

        items_copy = [i for i in items]

        while not hasSeenBefore:
            shuffle(items_copy)

            if items_copy in history:
                hasSeenBefore = True
            else:
                history.append([i for i in items_copy])
                shuffles += 1

        shuffle_history.append(shuffles)
        print(f"\t\tTook {shuffles} shuffles")
    print(f"\taverage {sum(shuffle_history[0:len(shuffle_history)]) / len(shuffle_history)}")