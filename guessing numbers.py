# Mbaga Tuzinde Mahaga
# Admission no: BSCIT-01-0064/2025
# Number Guessing Game

f = open("C:\\Users\\Admin\\Desktop\\pyhton class\\numberguess.txt", "w")

number = 100  # number to guess

while True:
    guess = int(input("Guess the number between 0 and 100: "))

    if guess < 0 or guess > 100:
        print("Invalid input! Please enter a number between 0 and 100.")
    
    elif guess == number:
        print("YOU WIN!!")
        print("You Win!! The number was", number, file=f)
        break
    
    elif guess > number:
        print("Too high, try again.")
    
    else:
        print("Too low, try again.")

f.close()
