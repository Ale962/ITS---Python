# The turtle and the hare

import random
import time

print("BANG!! AND THEY ARE OFF!!")

positionH : list = ["H"]
positionT : list = ["T"]

while True:

    time.sleep(1)

    nH = random.randint(1, 11)
    if nH <= 2:
        continue
    elif 2 < nH <= 4:
        for x1 in range(1, 10):
            positionH.append("H")
    elif 4 < nH <= 5:
        for x2 in range(1, 13):
            if len(positionH) > 1:
                positionH.pop[-1]
            else:
                continue
    elif 5 < nH <= 8:
        positionH.append("H")
    else:
        for x3 in range(1, 3):
            if len(positionH) > 1:
                positionH.pop[:-1]

    nT = random.randint(1, 11)
    if nT <= 5:
        for x4 in range(1, 4):
            positionT.append("T")