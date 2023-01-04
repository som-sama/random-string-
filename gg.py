import json
import random
with open('input.json', 'r') as f:
    data  = json.load(f)

random_object = random.choice(data['teamnames'])

print("Your team name is: ", random_object)