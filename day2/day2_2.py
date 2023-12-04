#!/usr/bin/python3
import re

def getNumInString(s):
    tmp = s.split()
    for t in tmp:
        if(t.isdigit()):
            return int(t)


with open("data.txt") as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        print(line)
        game_ID = int(line[0:line.find(":")].split()[1])
        game_data = line[line.find(":")+1:]

        # Find all numbers
        number_of_colored_cubes = re.findall(r'\d+', game_data)
        number_of_colored_cubes = [int(num) for num in number_of_colored_cubes]

        # Find corresponding colors
        colors = re.findall(r'\b[a-zA-Z]+\b', game_data)

        max_value_in_game = {"red": 0, "green": 0, "blue": 0}
        for i, num in enumerate(number_of_colored_cubes):
            corresponding_color = colors[i]
            if(max_value_in_game[corresponding_color] < num):
                max_value_in_game[corresponding_color] = num

        game_power = max_value_in_game["red"]*max_value_in_game["green"]*max_value_in_game["blue"]
        sum += game_power

    print(sum)
