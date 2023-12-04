#!/usr/bin/python3

numbers_spelled_out = {"one": "o1e", "two": "t2o", "three": "th3ee", "four": "f4ur", "five": "f5ve", "six": "s6x", "seven": "se7en", "eight": "ei8ht", "nine": "n9ne"}

with open("data.txt") as file:
    lines = file.readlines()
    
    sum = 0
    # Iterate through lines
    for line in lines:
        # Iterate through characters
        numbers = []

        for num in numbers_spelled_out:
            print(line)
            line = line.replace(num, numbers_spelled_out[num])
#            num_idx = 0
#            while line[num_idx:].find(num) >= 0:
#                num_idx = line.find(num)
#                line = line[0:num_idx+1]+str(numbers_spelled_out[num]) + line[num_idx:]
#                num_idx += len(num)
#                print(len(line))
#                if(len(line) < num_idx):
#                    break

        # Iterate through characters
        for c in line:
            # Check if the ASCII value matches a number
            if(ord(c) >= 48 and ord(c) <= 57):
                numbers.append(int(c))


        print(numbers)
        if(len(numbers) > 0):
            line_num = int(str(numbers[0]) + str(numbers[-1]))
            print(line_num)
            print()
            sum += line_num

    print(sum)
    


