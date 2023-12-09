#!/usr/bin/python3

def getDiffSequences(sequence, diff_sequences):
    ds = []
    for i in range(1, len(sequence)):
        ds.append(sequence[i] - sequence[i-1])
    
    diff_sequences.append(ds)

    # Check if all elements in List are zeros
    if all(num == 0 for num in ds) and len(ds) > 0:
        return diff_sequences
    else:
        getDiffSequences(ds, diff_sequences)

def calculateNextNumInSequence(sequence, diff_sequences):
    next_num = 0
    for i, ds in reversed(list(enumerate(diff_sequences))):
        next_num += ds[-1]

    return next_num + sequence[-1]

def calculatePrevNumInSequence(sequence, diff_sequences):
    prev_num = 0
    for i, ds in reversed(list(enumerate(diff_sequences))):
        prev_num = ds[0] - prev_num 

    return  sequence[0] - prev_num

with open("data.txt") as file:
    lines = file.readlines()

    solution = 0
    for line in lines:
        diff_sequences = []
        sequence = list(map(int, line.split()))
        getDiffSequences(sequence, diff_sequences)
        next_num = calculatePrevNumInSequence(sequence, diff_sequences)
        solution += next_num



    print(f"Anwser is: {solution}")