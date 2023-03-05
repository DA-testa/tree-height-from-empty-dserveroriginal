# python3 221RDB047

import sys
import threading
import numpy

counted=[]

def node_height(array, index, height):
    if array[index]==-1:
        return height
    elif counted[array[index]]==0:
        counted[array[index]]=node_height(array, array[index], height+1)
    return counted[array[index]]+1

def compute_height(array, max_height):
    # Write this function
    # Your code here
    for index in range(len(array)):
        height=node_height(array, i, 1)
        if height>max_height:
            max_height=height
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
    for index in range(len(array)):
        counted.append(0)
    print(compute_height(array, 0))
     
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