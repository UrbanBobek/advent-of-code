#!/usr/bin/python3

with open("data.txt") as file:
    lines = file.readlines()
    num_of_cards = len(lines)
    print(f"Number of cards: {num_of_cards}")

    score = 0
    card_count = [1]*num_of_cards
    for line in lines:
        line = line[:-1]

        card_number = int(line[line.find(" ") + 1 :line.find(":")]) 
        
        winning_numbers = line[line.find(":") + 1 :line.find("|")].split()
        winning_numbers = [int(n) for n in winning_numbers]

        played_numbers = line[line.find("|") + 1 : ].split()
        played_numbers = [int(n) for n in played_numbers]

        p = 0
        for wn in winning_numbers:
            for pn in played_numbers:
                if(wn == pn):
                    p += 1

        for i in range(card_number,card_number+p):
            card_count[i] += card_count[card_number-1]

        score = sum(card_count)

    print(f"Anwser is: {score}")
                



            

