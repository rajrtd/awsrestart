import sys

def printHyphens(input):
    for hyphenSpacing in range(3):
        for hyphenRow in range(int(input)):
            print("-", end = "")
        print("", end = " ")
    print()

def printPipes(input):
    for pipeRows in range(int(input)):
        for pipes in range(2):
            for emptySpaces in range(int(input)):
                print(end = " ") #prints empty spaces userInput amount of times
            print("|", end = "") #prints a pipe after it's finished printing an empty space userInput amount of times, then goes back to
        print() # goes to the next line userInput amount of times

def printBoard(size):
    for i in range(2):
        printPipes(size)
        printHyphens(size)
    printPipes(size)

n = input("How large do you want your tic-tac-toe board to be? ")
f = open("output.txt", 'w')
sys.stdout = f
printBoard(n)
f.close()