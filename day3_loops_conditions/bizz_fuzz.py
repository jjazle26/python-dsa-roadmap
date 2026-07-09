for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBang")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Bang")
    else:
        print(i)
        