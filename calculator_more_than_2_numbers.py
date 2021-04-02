mathquestion=[]
def operator_finder():
    operator = input("give me a operation")
    mathquestion.append(operator)
def numbers():
    num1 = float(input("Enter a number: "))
    mathquestion.append(num1)
def math_statment():
    try:
        numbers()
        operator_finder()
        numbers()
        print(mathquestion)
        end = str(input("is that the end of your question?: 1=yes anything=No"))
        if end == "1":
            print("Thank you.")
        else:
            while True:
                operator_finder()
                numbers()
                print(mathquestion)
                end = str(input("is that the end of your question?: 1=yes anything=No"))
                if end == "1":
                    print("Thank you.")
                    break
    except:
        print("Sorry, but excepetion has happend. Please make sure that it is a logcial statment and only numbers and valid symbols are put in.")
def math_calulations():
    def insert_and_remove():
        mathquestion.insert(index, answer)
        mathquestion.pop(index + 2)
        mathquestion.pop(index + 1)
        mathquestion.pop(index - 1)
    math_statment()
    while True:
        if len(mathquestion)==1:
            print(f"The answer to the question is {mathquestion}")
            break
        if '**' in mathquestion:
            index = mathquestion.index(('**'))
            number1 = mathquestion[index - 1]
            number2 = mathquestion[index + 1]
            answer=float(number1)**float(number2)
            insert_and_remove()
        elif '*' in mathquestion:
            if "/" in mathquestion:
                index1= mathquestion.index(('/'))
                index2 = mathquestion.index(('*'))
                if index1<index2:
                    index = mathquestion.index(('/'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1)/float(number2)
                    insert_and_remove()
                else:
                    index = mathquestion.index(('*'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1) * float(number2)
                    insert_and_remove()
            else:
                index = mathquestion.index(('*'))
                number1 = mathquestion[index - 1]
                number2 = mathquestion[index + 1]
                answer=float(number1)*float(number2)
                insert_and_remove()
        elif '/' in mathquestion:
            if "*" in mathquestion:
                index1= mathquestion.index(('*'))
                index2 = mathquestion.index(('/'))
                if index1<index2:
                    index = mathquestion.index(('*'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1)*float(number2)
                    insert_and_remove()
                else:
                    index = mathquestion.index(('/'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1) / float(number2)
                    insert_and_remove()
            else:
                index = mathquestion.index(('/'))
                number1 = mathquestion[index - 1]
                number2 = mathquestion[index + 1]
                answer=float(number1)/float(number2)
                insert_and_remove()
        elif '+' in mathquestion:
            if "-" in mathquestion:
                index1= mathquestion.index(('-'))
                index2 = mathquestion.index(('+'))
                if index1<index2:
                    index = mathquestion.index(('/'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1)-float(number2)
                    insert_and_remove()
                else:
                    index = mathquestion.index(('+'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1) + float(number2)
                    insert_and_remove()
            else:
                index = mathquestion.index(('+'))
                number1 = mathquestion[index - 1]
                number2 = mathquestion[index + 1]
                answer=float(number1)+float(number2)
                insert_and_remove()
        elif '-' in mathquestion:
            if "+" in mathquestion:
                index1= mathquestion.index(('+'))
                index2 = mathquestion.index(('-'))
                if index1<index2:
                    index = mathquestion.index(('/'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1)+float(number2)
                    insert_and_remove()
                else:
                    index = mathquestion.index(('-'))
                    number1 = mathquestion[index - 1]
                    number2 = mathquestion[index + 1]
                    answer = float(number1) - float(number2)
                    insert_and_remove()
            else:
                index = mathquestion.index(('-'))
                number1 = mathquestion[index - 1]
                number2 = mathquestion[index + 1]
                answer = float(number1)-float(number2)
                insert_and_remove()
math_calulations()
