#!/usr/bin/python3

mapping = {'A': 'Z', 'K': 'Y', 'Q':'X', 'J': 'W', 'T': 'V'}

def returnHandType(hand):
    removed_duplicates = set(hand)
    if(len(removed_duplicates) == 1):
        return "Five"
    if(len(removed_duplicates) == 2):
        removed_duplicates = list(removed_duplicates)
        l1 = hand.count(removed_duplicates[0])
        l2 = hand.count(removed_duplicates[1])
        if(abs(l1-l2) == 3):
            return "Four"
        else:
            return  "Full"
    if(len(removed_duplicates) == 3):
        occurences = [hand.count(h) for h in removed_duplicates]
        if(3 in occurences):
            return "Three"
        else:
            return "Two pair"
    if(len(removed_duplicates) == 4):
        return "One pair"
    if(len(removed_duplicates) == 5):
        return "High"
    
# Order hands in ascending order
def orderHandList(hand_list):
    hand_list.sort(key=lambda x:x[0])

    return hand_list

def calculateScore(hand_list, rank=0):
    score = 0
    for i, hand in enumerate(hand_list):
        score += (rank + i + 1)*hand[1]
    rank += len(hand_list) 
    return score, rank


fives = []
fours = []
full_houses = []
threes = []
two_pairs = []
one_pair = []
high = []
with open("data.txt") as file:
    lines = file.readlines()
    hands = []
    for line in lines:
        line = line.split()
        hand = line[0]
        bid= int(line[1])
        
        hand_type = returnHandType(hand)
        hand = ''.join(map(lambda c: mapping.get(c, c), hand))
        match hand_type:
            case "Five":
                fives.append((hand, bid))
            case "Four":
                fours.append((hand, bid))
            case "Full":
                full_houses.append((hand, bid))
            case "Three":
                threes.append((hand, bid))
            case "Two pair":
                two_pairs.append((hand, bid))
            case "One pair":
                one_pair.append((hand, bid))
            case "High":
                high.append((hand, bid))

    orderHandList(fives)
    orderHandList(fours)
    orderHandList(full_houses)
    orderHandList(threes)
    orderHandList(two_pairs)
    orderHandList(one_pair)
    orderHandList(high)
    solution = 0

    score, rank = calculateScore(high)
    solution += score
    score, rank = calculateScore(one_pair, rank)
    solution += score
    score, rank = calculateScore(two_pairs, rank)
    solution += score
    score, rank = calculateScore(threes, rank)
    solution += score
    score, rank = calculateScore(full_houses, rank)
    solution += score
    score, rank = calculateScore(fours, rank)
    solution += score
    score, rank = calculateScore(fives, rank)
    solution += score

    print(f"Anwser is: {solution}")