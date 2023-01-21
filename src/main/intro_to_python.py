import numpy as num
def main():
    matrix = x_equals_y(3)
    print(matrix)
    print("")
    matrix = step_2_transform(matrix)
    print(matrix)
    print("")
    matrix = step_3_transform(matrix)
    print(matrix)
    print("")
    

def x_equals_y(size):
    matrix = num.zeros((size, size))
    for x in range(size):
        for y in range(size):
            if x==y:
                matrix[x,y] = 1
    return matrix

def step_2_transform(arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if x==y:
                continue
            arr[x,y] +=3
    return arr

def step_3_transform(arr):
    arr = num.delete(arr,2,1)
    return arr

main()


   
