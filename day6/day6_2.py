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
    race_time = ""
    for rt in race_times:
        race_time += rt

    race_time = int(race_time) 

    record_times = file.readline()
    record_times = record_times[record_times.find(":")+1:].split() 
    record_time = ""
    for rt in record_times:
        record_time += rt

    record_time = int(record_time) 
    print(race_time)
    print(record_time)
    solution = numberOfWinningButtonPressDurations(race_time, record_time)

    print(f"Anwser is: {solution}")