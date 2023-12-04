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

def checkForTwoNumbers(subArray):
    number_present_sub = (subArray >= 0)
    num_of_numbers = 0
    num_loc = []
    for r, row in enumerate(number_present_sub):
        c = np.where(row == True)
        if(len(c[0]) > 0):
            if(len(c[0]) == 2 and c[0][0] == 0 and c[0][1] == 2): # two different numbers are in the subarray
                    num_of_numbers +=2
                    for n in c[0]:
                        num_loc.append([r-1, n-1])
                    continue

            num_of_numbers += 1
            num_loc.append([r-1, c[0][0]-1])


    if num_of_numbers == 2:
        return True, num_loc
    else:
        return False, num_loc
    
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
            if(ch == "."):
                number_map.append(-1)
            # character is a star symbol
            elif(ch == "*"):
                number_map.append(-2)
            # character is a symbol
            elif(ord(ch) < ord("0") or ord(ch) > ord("9")):
                number_map.append(-3)
            # character is a number
            else:
                number_map.append(int(ch))
        number_map = np.array(number_map)

        if(len(schematic_data) == 0):
            schematic_data = number_map 
            continue
        schematic_data = np.vstack((schematic_data, number_map))

    sum = 0
    prev_num = 0
    for row in range(np.size(schematic_data, 0)):
        for col in range(np.size(schematic_data, 1)):
            num = schematic_data[row][col]
            # Star at this position
            if(num == -2):
                # Check if two numbers are nearby
                subArray = getSubArray(schematic_data, col, row)
                gear_present, num_loc = checkForTwoNumbers(subArray)
                if(gear_present):
                    num_loc_1 = num_loc[0]
                    num_1 = extractNumber(schematic_data, col + num_loc_1[1], row + num_loc_1[0])

                    num_loc_2 = num_loc[1]
                    num_2 = extractNumber(schematic_data, col + num_loc_2[1], row + num_loc_2[0])

                    gear_ratio = num_1 * num_2
                    sum += gear_ratio

    
    print()
    print(f"Anwser is: {sum}")
                



            

