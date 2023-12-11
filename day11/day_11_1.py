#!/usr/bin/python3
import numpy as np
import math

def expandSpaceMap(space_map):
    expanded_space_map = space_map
    # Expand columns
    empty_columns = []
    for i in range(expanded_space_map.shape[0]):
        column = expanded_space_map[:,i]
        if((column == '.').all()):
            empty_columns.append(i)

    empty_column = np.full((1, expanded_space_map.shape[0]), '.')
    for i, ec in enumerate(empty_columns):
        expanded_space_map = np.insert(expanded_space_map, i+ec, empty_column, axis=1)

    # Expande rows
    empty_rows = []
    for i in range(space_map.shape[1]):
        row = space_map[i,:]
        if((row == '.').all()):
            empty_rows.append(i)

    empty_row = np.full((1, expanded_space_map.shape[1],), '.')
    for i, er in enumerate(empty_rows):
        expanded_space_map = np.insert(expanded_space_map, i+er, empty_row, axis=0)

    return expanded_space_map

def numberTheGalaxies(space_map):
    galaxy_num = 0
    galaxy_coordinates = []
    for i in range(space_map.shape[0]):
        for j in range(space_map.shape[1]):
            if(space_map[i][j] == '#'):
                space_map[i][j] = galaxy_num
                galaxy_coordinates.append((i, j))
                galaxy_num += 1

    return space_map, galaxy_num, galaxy_coordinates

def getGalaxyPairs(number_of_galaxies):
    galaxy_pairs = []
    for i in range(0, num_of_galaxies):
        for j in range(i+1, num_of_galaxies):
            galaxy_pairs.append([i, j])

    return galaxy_pairs

def calculateGalaxyPairDistance(pair, coordinates):
    g1 = coordinates[pair[0]]
    g2 = coordinates[pair[1]]

    d = abs(g2[0]-g1[0]) + abs(g2[1] - g1[1])

    return d

    


with open("data.txt") as file:
    lines = file.readlines()

    space_map = []

    for line in lines:
        space_map_line = np.array(list(line.strip()))

        if(len(space_map) == 0):
            space_map = space_map_line
            continue

        space_map = np.vstack((space_map, space_map_line))

expanded_space_map = expandSpaceMap(space_map)
numbered_space_map, num_of_galaxies, galaxy_coordinates = numberTheGalaxies(expanded_space_map)
galaxy_pairs = getGalaxyPairs(num_of_galaxies)
print(f"Number of galaxy pairs: {len(galaxy_pairs)}")

solution = 0
for gp in galaxy_pairs:
    d = calculateGalaxyPairDistance(gp, galaxy_coordinates)
    solution += d

print(f"Anwser is: {solution}")

