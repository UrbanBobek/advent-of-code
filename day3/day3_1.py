#!/usr/bin/python3
import numpy as np

def getSubArray(array, col, row):
    num_of_cols = np.size(array, 1)
    num_of_rows = np.size(array, 0)

    cols = [col -1, col, col + 1]
    rows = [row -1, row, row + 1]

    if(col <= 0):
        cols = [col, col + 1]
    elif(col >= num_of_cols -1):
        cols = [num_of_cols - 2, num_of_cols -1]

    if(row <= 0):
        rows = [row, row + 1]
    elif(row >= num_of_rows -1):
        rows = [num_of_rows - 2, num_of_rows - 1]

    subarray = schematic_data[np.ix_(rows,cols)]
    return subarray

def checkForSymbol(subArray):
    return np.any(subArray <= -2)


def extractNumber(array, col, row):
    num_of_cols = np.size(array, 1)

    digits = str(array[row][col])

    i = 1
    while(col+i < num_of_cols and array[row][col+i] >= 0 ):
        digits = digits + str(array[row][col+i])
        i += 1
    i = 1
    while(col-i >= 0 and array[row][col-i] >= 0):
        digits = str(array[row][col-i]) + digits
        i += 1

    return int(digits)


with open("data.txt") as file:
    lines = file.readlines()
    schematic_data = []
    for line in lines:
        line = line[0:-1]
        print(line)
        number_map = []
        for ch in line:
            # character is a dot
            if(ord(ch) == ord(".")):
                number_map.append(-1)
            # character is a symbol
            elif(ord(ch) != 46 and (ord(ch) < ord("0") or ord(ch) > ord("9"))):
                number_map.append(-2)
            # character is a number
            else:
                number_map.append(int(ch))
        number_map = np.array(number_map)

        if(len(schematic_data) == 0):
            schematic_data = number_map 
            continue
        schematic_data = np.vstack((schematic_data, number_map))

    print(schematic_data)

    sum = 0
    prev_num = 0
    for row in range(np.size(schematic_data, 0)):
        for col in range(np.size(schematic_data, 1)):
            num = schematic_data[row][col]
            if(num >= 0 and num <= 9):
                subArray = getSubArray(schematic_data, col, row)
                if(checkForSymbol(subArray)):
                    num = extractNumber(schematic_data, col, row)
                    if(num == prev_num):
                        continue
                    sum += num
                    prev_num = num
            else:
                prev_num = 0
    
    print()
    print(f"Anwser is: {sum}")
                



            

