import random
def randomMath(min,max):
    return random.randint(min,max)

def guessTheNumber(randomNumber):
    guess = int(input("Guess the number:"))
    if guess == randomNumber:
        print("You Win")
    else:
        print("Try Again")
        guessTheNumber(randomNumber)

rand = randomMath(1,100)
print(rand)
guessTheNumber(rand)