#!/usr/bin/python3
import re

def getNumInString(s):
    tmp = s.split()
    for t in tmp:
        if(t.isdigit()):
            return int(t)

valid_cubes = {"red": 12, "green": 13, "blue": 14}

with open("data.txt") as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        print(line)
        game_ID = int(line[0:line.find(":")].split()[1])
        game_data = line[line.find(":")+1:]

        # Find all numbers
        number_of_colored_cubes = re.findall(r'\d+', game_data)

        # Find corresponding colors
        colors = re.findall(r'\b[a-zA-Z]+\b', game_data)

        is_valid_game = True
        for i, num in enumerate(number_of_colored_cubes):
            corresponding_color = colors[i]
            if int(num) > valid_cubes[corresponding_color]:
                is_valid_game = False
                break

        if(is_valid_game):
            sum += game_ID

        print(sum)
