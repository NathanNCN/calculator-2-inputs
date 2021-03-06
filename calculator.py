def Math_answer():
    value_last_question=None
    valid=["-","+","/","*","**"]
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("give me a operation")
            num2 = float(input("Enter second number: "))
            if operator not in valid:
                print("sorry that is a invalid operator please input valid symbol and or number")
            if operator=="-":
                answer=num1-num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
            elif operator == "+":
                answer = num1+num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
            elif operator == "*":
                answer = num1*num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
            elif operator == "/":
                answer = num1/num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
            elif operator == "**":
                answer = num1**num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
            elif operator == "%":
                answer = num1%num2
                print(f"The answer is {answer}")
                end=input("\n would you want to end the program 1=Yes anything=no")
                if end=="1":
                    break
                else:
                    pass
        except:
            print("Sorry, but excepetion has happend. Please make sure that it is a logcial statment and only numbers and valid symbols are put in.")


Math_answer()
