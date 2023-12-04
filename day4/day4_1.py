#!/usr/bin/python3

with open("data.txt") as file:
    lines = file.readlines()
    sum = 0
    for line in lines:
        line = line[:-1]

        winning_numbers = line[line.find(":") + 1 :line.find("|")].split()
        winning_numbers = [int(n) for n in winning_numbers]

        played_numbers = line[line.find("|") + 1 : ].split()
        played_numbers = [int(n) for n in played_numbers]

        p = 0
        for wn in winning_numbers:
            for pn in played_numbers:
                if(wn == pn):
                    p += 1
        if(p>0):
            sum += 2**(p-1)
    
    print(f"Anwser is: {sum}")
                



            

