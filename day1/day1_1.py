#!/usr/bin/python3

with open("data.txt") as file:
    lines = file.readlines()
    
    sum = 0
    # Iterate through lines
    for line in lines:
        numbers = []
        # Iterate through characters
        for c in line:
            # Check if the ASCII value matches a number
            if(ord(c) >= 48 and ord(c) <= 57):
                numbers.append(int(c))

        if(len(numbers) > 0):
            line_num = int(str(numbers[0]) + str(numbers[-1]))
            sum += line_num

    print(sum)
    


