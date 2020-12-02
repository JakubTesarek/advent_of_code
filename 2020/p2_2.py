import re

with open('input/2-1', 'r') as input_file:
    lines = input_file.readlines()

def validate_passwd(line):
    parts = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    contains1 = parts[3][int(parts[0]) - 1] == parts[2]
    contains2 = parts[3][int(parts[1]) - 1] == parts[2]
    return contains1 != contains2

print(sum([int(validate_passwd(l)) for l in lines]))