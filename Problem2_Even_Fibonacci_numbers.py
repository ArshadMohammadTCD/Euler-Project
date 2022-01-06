

def main():
    currentNumber = 1
    nextNumber = 1
    runningTotal = 0
    while (currentNumber < 4000000):
        nextNumber = currentNumber + nextNumber
        currentNumber = nextNumber - currentNumber
        if (currentNumber%2 == 0):
            runningTotal += currentNumber
    print(runningTotal)
main()