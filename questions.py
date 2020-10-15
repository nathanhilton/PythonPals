import random
from openpyxl import load_workbook


def load_question():
    wk = load_workbook(filename='python_questions.xlsx')
    ws = wk.active
    while True:
        print("Question Categories: ")
        print("1 Syntax\n2 Vocabulary\n3 Logic\n4 Number Conversion\n5 General\n")
        category = input("Select question category: ")
        if category == '1':
            value = random.randrange(2, 7)
            break
        elif category == '2':
            value = random.randrange(7, 12)
            break
        elif category == '3':
            value = random.randrange(12, 17)
            break
        elif category == '4':
            value = random.randrange(17, 22)
            break
        elif category == '5':
            value = random.randrange(2, 22)
            break
        else:
            print("Invalid Entry: Please enter a number between 1 and 5")

    question = 'B' + str(value)
    print(ws[question].value)

    choices = 'D' + str(value)
    print(ws[choices].value)

    answer = ws['E' + str(value)].value
    guess = input("Enter your answer choice: ")

    if guess == answer or guess == answer.capitalize() or guess == answer + '.' or guess == answer.capitalize() + '.':
        print("Correct!")
        return True
    else:
        print("Incorrect")
        return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_question()
