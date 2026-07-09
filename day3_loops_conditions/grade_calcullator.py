marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        grade = "A+"
        print(f"Grade: {grade} (Honors)")
    elif marks >= 75:
        grade = "A"
        print(f"Grade: {grade}")
    else:
        print("Pass")
else:
    print("Fail")
    
