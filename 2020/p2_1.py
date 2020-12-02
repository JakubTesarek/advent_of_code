import re

with open('input/2-1', 'r') as input_file:
    lines = input_file.readlines()

def validate_passwd(line):
    parts = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    return int(parts[0]) <= parts[3].count(parts[2]) <= int(parts[1])

print(sum([int(validate_passwd(l)) for l in lines]))