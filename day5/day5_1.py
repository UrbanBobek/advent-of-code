#!/usr/bin/python3

class Maps:
    def __init__(self):
        self.seed_to_soil_map = []
        self.soil_to_fertilizer_map = []
        self.fertilizer_to_water_map = []
        self.water_to_light_map = []
        self.light_to_temperature_map = []
        self.temperature_to_humidity_map = []
        self.humidity_to_location_map = []

        self.current_map = [] 
    
    def getLocationFromSeedID(self, seed):

        soil_id = self.getNextIDFromMap(seed, self.seed_to_soil_map)
        fert_id = self.getNextIDFromMap(soil_id, self.soil_to_fertilizer_map)
        water_id = self.getNextIDFromMap(fert_id, self.fertilizer_to_water_map)
        light_id = self.getNextIDFromMap(water_id, self.water_to_light_map)
        temp_id = self.getNextIDFromMap(light_id, self.light_to_temperature_map)
        humid_id = self.getNextIDFromMap(temp_id, self.temperature_to_humidity_map)
        location = self.getNextIDFromMap(humid_id, self.humidity_to_location_map)
       # print(soil_id)
       # print(fert_id)
       # print(water_id)
       # print(light_id)
       # print(temp_id)
       # print(humid_id)
       # print(location)
        return location
        
    def getNextIDFromMap(self, id, mapping):
        for r in mapping:
            dest_start = r["destination range start"]
            source_start = r["source range start"]
            id_range = r["range"]
            #print(dest_start)
            #print(source_start)
            #print(id_range)

            if(id >= source_start and id < source_start + id_range):
                return id +  dest_start - source_start

        return id


with open("data.txt") as file:
    seeds_ids = file.readline()
    seeds_ids = seeds_ids[seeds_ids.find(":") + 1 :].split()
    seeds_ids = [int(s) for s in seeds_ids]

    print(seeds_ids)

    maps = Maps()

    lines = file.readlines()
    for line in lines:
        if("seed-to-soil" in line):
            maps.current_map = maps.seed_to_soil_map
            continue
        if("soil-to-fertilizer" in line):
            maps.current_map = maps.soil_to_fertilizer_map
            continue
        if("fertilizer-to-water" in line):
            maps.current_map = maps.fertilizer_to_water_map
            continue
        if("water-to-light" in line):
            maps.current_map = maps.water_to_light_map
            continue
        if("light-to-temperature" in line):
            maps.current_map = maps.light_to_temperature_map
            continue
        if("temperature-to-humidity" in line):
            maps.current_map = maps.temperature_to_humidity_map
            continue
        if("humidity-to-location" in line):
            maps.current_map = maps.humidity_to_location_map
            continue

        if(len(line) > 1):
            vals = line.split()
            vals = [int(v) for v in vals]
            ranges = {"destination range start": vals[0], "source range start": vals[1], "range": vals[2]}
            maps.current_map.append(ranges)

    location_numbers = [] 
    for seed in seeds_ids:
        location = maps.getLocationFromSeedID(seed)
        location_numbers.append(location)
        
    print(location_numbers)
    
    print(maps.seed_to_soil_map)
    print(maps.soil_to_fertilizer_map)
    print(maps.fertilizer_to_water_map)
    print(maps.water_to_light_map)
    print(maps.light_to_temperature_map)
    print(maps.temperature_to_humidity_map)
    print(maps.humidity_to_location_map)
    print(f"Anwser is: {min(location_numbers)}")