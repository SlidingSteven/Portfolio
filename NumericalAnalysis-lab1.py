#!/usr/bin/env python3
#not sure if the shebang above is necessary but I want to be as thorough as possible
#Name: Steven Tucker
#Date: 9/12/19

arr = [ [1, 3, 2, 1, -2],
        [4, 2, 1, 2, 2],
        [2, 1, 2, 3, 1],
        [1, 2, 4, 1, -1]] 
# function to print the matrix from GeeksForGeeks https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
def printMat(mat): 
    n = len(mat)
    for i in range(n): 
        for j in range(n+1): 
            print(mat[i][j] , " ", end="") 
        print() 


#function to print the array 
def printarr(arr): 
    n = len(arr)
    for i in range(n): 
        print(arr[i] , " ", end="") 
        print() 
print("Original Matrix:") 
printMat(arr)


def NaiveGauss(arr):
    for col in range(0,len(arr)):   
        for row in range(0, len(arr)):
            if arr[col][row] < arr[0][0]:
                temp = arr[0]
                arr[0] = arr[col]
                arr[col]=temp
 
    for row in range(0, len(arr)-1):
        for col in range(row+1, len(arr)):
            alpha = - arr[col][row]/arr[row][row]

            for k in range (0, len(arr)+1):        
                arr[col][k] = arr[col][k] + (alpha * arr[row][k])
    return(arr)


def BackwardsSubstitution(mat):
    returnArray=[1] * len(mat)
    i = len(mat) -1 

    returnArray[i] = mat[i][i+1]/mat[i][i]
    i -=1
    while i >= 0:


        for col in range(i+1, len(mat)):
            if mat[i][col] > 0:

                num = mat[i][col] * returnArray[col]
                newNum = mat[i][len(mat)]-num
                mat[i][len(mat)] = newNum
                mat[i][col] = 0
                #BackwardsSubstitution(mat)
            else:

                returnArray[i] = mat[i][len(mat)]/mat[i][i]
        i-=1

    return(returnArray)


arr1 = NaiveGauss(arr)
print("After NGE: ")
printMat(arr1)
end = BackwardsSubstitution(arr1)
print("Final Array: ")
printarr(end)

