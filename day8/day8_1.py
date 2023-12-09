#!/usr/bin/python3
with open("data.txt") as file:
    instructions = file.readline()[0:-1]
    instructions = [0 if c == 'L' else 1  for c in instructions]
    
    lines = file.readlines()
    navigation = {}
    for line in lines:
        if(len(line) <= 1):
            continue
        key = line[0:line.find('=')-1]
        left = line[line.find('(')+1:line.find(',')]
        right = line[line.find(',')+2:line.find(')')]

        navigation[key] = (left, right)
    
    print(navigation)

    step_count = 0
    current_key = "AAA"
    current_instruction_idx = 0
    while(current_key != "ZZZ"):
        next_key = navigation[current_key][instructions[current_instruction_idx]]
        current_key = next_key
        step_count += 1

        current_instruction_idx += 1
        if(current_instruction_idx >= len(instructions)):
            current_instruction_idx = 0




    solution = step_count
    print(f"Anwser is: {solution}")