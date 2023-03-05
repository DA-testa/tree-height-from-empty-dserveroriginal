# python3 221RDB047

import sys
import threading
import numpy

def compute_height(array, max_height):
    # Write this function
    # Your code here
    changed=False
    for index in range(array.lengh):
        if array[index]==-1:
            array[index]=-2
            if not changed:
                max_height+=1
            changed=True
        elif array[index]==-2:
            pass
        else:
            array[index]=array[array[index]]
            if not changed:
                max_height+=1
            changed=True
    if changed:
        return compute_height(array, max_height)
    return max_height


def main():
    # implement input form keyboard and from files
    userInput=input()
    
    if userInput=="I":
        # input from keyboard
        number = int(input())
        array = list(map(int, input().split()))
    elif userInput=="F":
        # input from file
        with open(userInput) as file:
            number = int(file.readline())
            array = list(map(int, file.readline().split()))
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
if __name__ == "__main__":
    main()
# print(numpy.array([1,2,3]))