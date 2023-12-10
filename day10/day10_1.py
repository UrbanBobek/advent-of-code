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

    return start, next_direction


def nextStep(map, current_location, direction):
    move = directions[direction]

    x = current_location[0] + move[0]
    y = current_location[1] + move[1]

    next_location = [x, y]

    invalid_next_direction = getInvalidDirection(direction) 

    pipe_type = map[x][y]
    if(pipe_type == 'S'):
        return 0, 0

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

with open("data.txt") as file:
    lines = file.readlines()
    pipe_map = []
    for line in lines:
        pipe_map_line = np.array(list(line.strip()))

        if(len(pipe_map) == 0):
            pipe_map = pipe_map_line
            continue

        pipe_map = np.vstack((pipe_map, np.array(pipe_map_line)))

    start = np.where(pipe_map == 'S')
    start = [start[0][0], start[1][0]]

    start, next_direction = startStep(pipe_map)

    next_direction, current_location = nextStep(pipe_map, start, next_direction)
    step_count = 1
    while(next_direction != 0):
        next_direction, current_location = nextStep(pipe_map, current_location, next_direction)
        step_count += 1

    solution = step_count//2
    
    print(f"Anwser is: {solution}")
                



            

