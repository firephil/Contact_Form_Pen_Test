import json
import random
# Simple Script to read Strings from a file and convert them to json 
# and save them in a different file

# Read and Convert
with open('names.txt') as f:
    lines = f.readlines()
    res = [line.rstrip() for line in lines]
    
    # shuffle the list to mix girls names with boys names
    random.shuffle(res)
    names = json.JSONEncoder().encode(res)

# Write
with open('names.json', "w") as fout:
    fout.write(str(names))