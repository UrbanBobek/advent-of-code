#!/usr/bin/python3
import math

def findNumberOfSteps(key, navigation, instructions):
    step_count = 0
    current_key = key
    current_instruction_idx = 0
    steps = []
    prev_finish_key = ""
    while(True):
        next_key = navigation[current_key][instructions[current_instruction_idx]]
        current_key = next_key
        step_count += 1

        current_instruction_idx += 1
        if(current_instruction_idx >= len(instructions)):
            current_instruction_idx = 0
        
        if(next_key == prev_finish_key):
            break
        if(next_key[-1] == 'Z' and next_key != prev_finish_key):
            steps.append(step_count)
            prev_finish_key = next_key

    return(steps[0])

# Find largest common multiple
def find_lcm(numbers):
   lcm_value = numbers[0]
   for num in numbers[1:]:
       lcm_value = lcm_value * num // math.gcd(lcm_value, num)
   return lcm_value

with open("data.txt") as file:
    instructions = file.readline()[0:-1]
    instructions = [0 if c == 'L' else 1  for c in instructions]
    
    lines = file.readlines()
    navigation = {}
    start_keys = []
    for line in lines:
        if(len(line) <= 1):
            continue
        key = line[0:line.find('=')-1]
        left = line[line.find('(')+1:line.find(',')]
        right = line[line.find(',')+2:line.find(')')]

        navigation[key] = (left, right)

        if(key[-1] == 'A'):
            start_keys.append(key)
    
    print(start_keys)

    step_counts = []
    for sk in start_keys:
        step_counts.append(findNumberOfSteps(sk, navigation, instructions))

    solution = find_lcm(step_counts)
    
    print(f"Anwser is: {solution}")