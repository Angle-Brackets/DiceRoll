import random, math


# First Python Program, Completed 12/5/19 at 10:12PM

def slowRoll(diceNum, sideNum, addVal):
    return diceRoll(diceNum, sideNum) + addVal


def fastRoll():
    str = raw_input("Enter roll condition [Dice Number]d[Side Number] + [Additional Value]: \t").replace(" ", "")
    return diceRoll(int(str[0:str.find('d')]), int(str[str.find('d') + 1:str.find('+')])) + int(str[str.find('+') + 1])


def diceRoll(dice, sides):
    total = 0
    for i in range(0, dice):
        total += math.ceil((random.random() * sides))
    return total


roll = raw_input("Fast or Slow Input?\t").lower()

if roll == "fast":
    print(fastRoll())
elif roll == "slow" :
    dice = input("How many Dice?\t")
    sides = input("How many Sides?\t")
    addNum = input("How much should be added to the total roll?\t")
    print("Sum of the rolls was: " + str(slowRoll(dice, sides, addNum)))
else:
    raise Exception("Invalid input type, must be FAST or SLOW")