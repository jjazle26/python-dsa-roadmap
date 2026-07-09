correct_pin = "1234"
balance = 5000
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print(f"Login successful! Balance: ${balance}")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. {attempts} tries left.")

if attempts == 0:
    print("Account locked.")
    