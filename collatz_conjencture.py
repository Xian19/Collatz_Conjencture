import random
import sys

# Get the maximum integer value that Python can handle
max_int = sys.maxsize

loop = 0

while loop == 0:

    startNum = random.randint(0, max_int)
    
    maxNum = startNum
    steps = 0
    newNum = startNum
    
    while newNum != 1:
        if newNum % 2 == 0:
            newNum = newNum / 2
        else:
            newNum = (newNum * 3) + 1
        steps += 1
        if newNum > maxNum:
            maxNum = newNum
    
    print("Starting Number is " + str(startNum))
    print("Maximum Number is " + str(maxNum))
    print("Number of steps: " + str(steps))