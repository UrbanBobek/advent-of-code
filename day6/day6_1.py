#!/usr/bin/python3

def numberOfWinningButtonPressDurations(race_time, record_distance):
    count = 0
    for i in range(1, race_time):
        press_duration = i
        remaining_time = race_time - press_duration
        traveled_distance = remaining_time*press_duration

        if(traveled_distance > record_distance):
            count+=1
    
    return count


with open("data.txt") as file:
    race_times = file.readline()
    race_times = race_times[race_times.find(":")+1:].split() 
    race_times = [int(rt) for rt in race_times]

    distances = file.readline()
    distances = distances[distances.find(":")+1:].split() 
    distances = [int(rt) for rt in distances]

    solution = 1
    for i in range(len(race_times)):
        solution *= numberOfWinningButtonPressDurations(race_times[i], distances[i])

    print(f"Anwser is: {solution}")