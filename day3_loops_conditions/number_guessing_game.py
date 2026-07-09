name = input("Enter your name to start: ")
secret_number = (len(name) * 7) % 20 + 1  

attempts_left = 5

print(f"\nWelcome {name}!")
print("I am thinking of a number between 1 and 20.")
print(f"You have {attempts_left} attempts to guess it.\n")

while attempts_left > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
        
    attempts_left -= 1
    if attempts_left > 0:
        print(f"Attempts remaining: {attempts_left}\n")
    else:
        print(f"\nGame over! The correct number was {secret_number}.")