# python3 221RDB047

import sys
import threading
import numpy

def compute_height(array):
    # Write this function
    # Your code here
    max_height = 0
    copy=array.copy()
    for index in range(len(array)):
        height = 0
        while array[index] != -1:
            height += 1
            array[index] = array[copy[index]]
        if height > max_height:
            max_height = height
    
    return max_height


def main():
    # implement input form keyboard and from files
    userInput=input("")
    
    if "I" in userInput.capitalize():
    #     # input from keyboard
        number = input("")
        array = list(map(int, input("").split(" ")))
    else:
        # input from file
        try:
            with open("test/"+input()) as file:
                number = int(file.readline())
                array = list(map(int, file.readline().split()))
        except:
            print("File not found")
            return
    #print(array)
    print(compute_height(array))
     
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #print(compute_height([4, -1, 4, 1, 1],1))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))