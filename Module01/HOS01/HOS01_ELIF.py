attempts = 0
randomNumber = 5

while attempts <= 3:
    guess = int(input("Please guess a interger between 1 and 6: "))
    
    if (guess == randomNumber):
        print("Congrats, you got it! ")
        break
    else:
        print("Oops, goodluck next time!")
    attempts += 1