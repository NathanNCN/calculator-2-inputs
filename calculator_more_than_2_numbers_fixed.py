mathquestion=[]
def ask_for_number():
    num1 = float(input("Enter a number: "))
    mathquestion.append(num1)
def ask_for_operator_and_numbers():
    operator = input("give me a operation")
    mathquestion.append(operator)
    ask_for_number()
    print(mathquestion)
def create_equation():
    try:
        ask_for_number()
        ask_for_operator_and_numbers()
        end = str(input("is that the end of your question?: 1=yes anything=No"))
        if end == "1":
            print("Thank you.")
        else:
            while True:
                ask_for_operator_and_numbers()
                end = str(input("is that the end of your question?: 1=yes anything=No"))
                if end == "1":
                    print("Thank you.")
                    break
    except:
        print("Sorry, but excepetion has happend. Please make sure that it is a logcial statment and only numbers and valid symbols are put in.")
def perform_calculations():
    def get_index_and_numbers_from_token(token):
        index = mathquestion.index(token)
        number1 = mathquestion[index - 1]
        number2 = mathquestion[index + 1]
        return (index, number1, number2)
    def insert_and_remove():
        mathquestion.insert(index, answer)
        mathquestion.pop(index + 2)
        mathquestion.pop(index + 1)
        mathquestion.pop(index - 1)
    while True:
        if len(mathquestion)==1:
            print(f"The answer to the question is {mathquestion}")
            break
        if '**' in mathquestion:
            get_index_and_numbers_from_token("**")
            index, number1, number2 = get_index_and_numbers_from_token('**')
            answer = float(number1) ** float(number2)
            insert_and_remove()
        elif '*' in mathquestion or '/' in mathquestion:
            if "/" in mathquestion and '*' in mathquestion:
                index1= mathquestion.index(('/'))
                index2 = mathquestion.index(('*'))
                if index1<index2:
                    get_index_and_numbers_from_token("/")
                    index, number1, number2 = get_index_and_numbers_from_token('/')
                    answer = float(number1)/float(number2)
                    insert_and_remove()
                else:
                    get_index_and_numbers_from_token("*")
                    index, number1, number2 = get_index_and_numbers_from_token('*')
                    answer = float(number1) * float(number2)
                    insert_and_remove()
            elif "/" in mathquestion and '*' not in mathquestion:
                get_index_and_numbers_from_token("/")
                index, number1, number2 = get_index_and_numbers_from_token('/')
                answer = float(number1) / float(number2)
                insert_and_remove()
            else:
                get_index_and_numbers_from_token("*")
                index, number1, number2 = get_index_and_numbers_from_token('*')
                answer = float(number1) * float(number2)
                insert_and_remove()
        elif '+' in mathquestion or '-' in mathquestion:
            if "-" in mathquestion and "+" in mathquestion:
                index1= mathquestion.index(('-'))
                index2 = mathquestion.index(('+'))
                if index1<index2:
                    get_index_and_numbers_from_token("-")
                    index, number1, number2 = get_index_and_numbers_from_token('-')
                    answer = float(number1)-float(number2)
                    insert_and_remove()
                else:
                    get_index_and_numbers_from_token("+")
                    index, number1, number2 = get_index_and_numbers_from_token('+')
                    answer = float(number1) + float(number2)
                    insert_and_remove()
            elif "-" in mathquestion and "+" not in mathquestion:
                get_index_and_numbers_from_token("-")
                index, number1, number2 = get_index_and_numbers_from_token('-')
                answer = float(number1) - float(number2)
                insert_and_remove()
            else:
                get_index_and_numbers_from_token("+")
                index, number1, number2 = get_index_and_numbers_from_token('+')
                answer=float(number1)+float(number2)
                insert_and_remove()
if __name__ == '__main__':
    create_equation()
    perform_calculations()
