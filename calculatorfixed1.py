def math_caluacaltions():
    num1 = float(input("Enter first number: "))
    operator = input("give me a operation")
    num2 = float(input("Enter second number: "))
    valid = {
        "-": f"{num1-num2}",
        "+": f"{num1+num2}",
        "/": f"{num1/num2}",
        "": f"{num1}{num2}",
        "**": f"{num1**num2}"
    }
    if operator in valid:
        final_answer = f"The answer to {num1}{operator}{num2} is " + valid[operator]
        print(final_answer)
    else:
        print(A+B)
def Math_answer():
    while True:
        try:
            math_caluacaltions()
            end=str(input("\n would you want to end the program 1=Yes anything=no"))
            if end=="1":
                break
        except:
            print("Sorry, but excepetion has happend. Please make sure that it is a logcial statment and only numbers and valid symbols are put in.")
            break
Math_answer()
