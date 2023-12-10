#!/usr/bin/python3
import numpy as np

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
pipe_types = {"|": ["up", "down"], "-": ["left", "right"], "L": ["up", "right"], "J": ["up", "left"], "7": ["down", "left"], "F": ["down", "right"], "S": [], ".": []}

def startStep(map):
    start = np.where(map == 'S')
    start = [start[0][0], start[1][0]]

    possible_start_directions = []
    for dir, move in directions.items():
        x = start[0] + move[0]
        y = start[1] + move[1]

        if(x < 0 or x >= map.shape[0] or y < 0 or y >= map.shape[1]):
            continue
        pipe_type = map[x][y]
        possible_directions = pipe_types[pipe_type]
        invalid_direction = getInvalidDirection(dir)

        if invalid_direction in possible_directions:
            possible_start_directions.append(dir)

    next_direction = possible_start_directions[0]

    # Find start pype type
    start_pipe_type = ''
    if("up" in possible_start_directions and "down" in possible_start_directions):
        start_pipe_type = "|"
    if("left" in possible_start_directions and "right" in possible_start_directions):
        start_pipe_type = "-"
    if("up" in possible_start_directions and "right" in possible_start_directions):
        start_pipe_type = "L"
    if("up" in possible_start_directions and "left" in possible_start_directions):
        start_pipe_type = "J"
    if("down" in possible_start_directions and "left" in possible_start_directions):
        start_pipe_type = "7"
    if("down" in possible_start_directions and "right" in possible_start_directions):
        start_pipe_type = "F"


    return start, next_direction, start_pipe_type


def nextStep(map, current_location, direction):
    move = directions[direction]

    x = current_location[0] + move[0]
    y = current_location[1] + move[1]

    next_location = [x, y]

    invalid_next_direction = getInvalidDirection(direction) 

    pipe_type = map[x][y]
    if(pipe_type == 'S'):
        return 0, [0]

    possible_direction = pipe_types[pipe_type]
    
    # Take the value which is not the "invalid_next_direction"
    next_direction = [v for v in possible_direction if v != invalid_next_direction]

    return next_direction[0], next_location


def getInvalidDirection(direction):
    invalid_direction = ''
    match direction:
        case "up": invalid_direction = 'down'
        case "down": invalid_direction = 'up'
        case "right": invalid_direction = 'left'
        case "left": invalid_direction = 'right'

    return invalid_direction


def updatePipePath(pipe_map, pipe_path, current_location):
    if(len(current_location) == 2):
        x = current_location[0] 
        y = current_location[1]

        pipe_path[x][y] = pipe_map[x][y]


with open("data.txt") as file:
    lines = file.readlines()
    pipe_map = []
    for line in lines:
        pipe_map_line = np.array(list(line.strip()))

        if(len(pipe_map) == 0):
            pipe_map = pipe_map_line
            continue

        pipe_map = np.vstack((pipe_map, np.array(pipe_map_line)))

    pipe_path = np.zeros(pipe_map.shape, dtype=int)
    pipe_path = pipe_path.astype(str)

    start = np.where(pipe_map == 'S')
    start = [start[0][0], start[1][0]]

    start, next_direction, start_pipe_type = startStep(pipe_map)
    updatePipePath(pipe_map, pipe_path, start)
    pipe_path[start[0]][start[1]] = start_pipe_type

    current_location = start
    while(next_direction != 0):
        next_direction, current_location = nextStep(pipe_map, current_location, next_direction)
        updatePipePath(pipe_map, pipe_path, current_location)
    
    def countPipeCrossings(pipe_path, location):
        x = location[1]
        y = location[0]

        count = 0
        for i in range(x, -1, -1):
            thing = pipe_path[y][i]

            if(thing == "L" or thing == "J" or thing == "|"):
                count += 1

        return count


    solution = 0
    for i, row in enumerate(pipe_path):
        num_of_changes = 0
        for j in range(0, len(row)):
            curr_type = row[j]
            if(curr_type == '0'):
                crossings = countPipeCrossings(pipe_path, [i,j])

                if(crossings % 2):
                    pipe_path[i][j] = '1'
                    solution += 1

    print(f"Anwser is: {solution}")
                


