import random
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def makeHBQuestion():
    intValue = random.randrange(0, 511)
    dummy1 = random.randrange(0, 511)
    dummy2 = random.randrange(0, 511)
    dummy3 = random.randrange(0, 511)

    print("What is the hexadecimal " + hex(intValue)[2:] + " in binary representation?\n")
    print(bin(intValue)[2:])
    print(bin(dummy1)[2:])
    print(bin(dummy2)[2:])
    print(bin(dummy3)[2:])

    answer = input("Select Answer\n")
    if answer == bin(intValue)[2:]:
        print('Correct')
    else:
        print('Oof')

def makeBHQuestion():
    intValue = random.randrange(0, 511)
    dummy1 = random.randrange(0, 511)
    dummy2 = random.randrange(0, 511)
    dummy3 = random.randrange(0, 511)

    print("What is the binary " + bin(intValue)[2:] + " in hexadecimal representation?\n")
    print(hex(intValue)[2:])
    print(hex(dummy1)[2:])
    print(hex(dummy2)[2:])
    print(hex(dummy3)[2:])

    answer = input("Select Answer\n")
    if answer == hex(intValue)[2:]:
        print('Correct')
    else:
        print('Oof')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    makeBHQuestion()
    makeHBQuestion()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
