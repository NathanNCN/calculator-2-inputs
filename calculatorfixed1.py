def math_caluacaltions():
    num1 = float(input("Enter first number: "))
    operator = input("give me a operation")
    num2 = float(input("Enter second number: "))
    valid = ["-", "+", "/", "", "**"]
    if operator in valid:
        math_method=valid.index(operator)
        if math_method==0:
            print(f"The answer to {num1}{operator}{num2} is {num1-num2}")
        if math_method==1:
            print(f"The answer to {num1}{operator}{num2} is {num1+num2}")
        if math_method==2:
            print(f"The answer to {num1}{operator}{num2} is {num1/num2}")
        if math_method==3:
            print(f"The answer to {num1}{operator}{num2} is {num1num2}")
        if math_method==4:
            print(f"The answer to {num1}{operator}{num2} is {num1**num2}")
    else:
        print(A+B)
def Math_answer():
    while True:
        try:
            math_caluacaltions()
            end=str(input("\n would you want to end the program 1=Yes anything=no"))
            if end=="1":
                break
            elif end!="1":
                pass
        except:
            print("Sorry, but excepetion has happend. Please make sure that it is a logcial statment and only numbers and valid symbols are put in.")
            break
Math_answer()
