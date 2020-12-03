with open('input/3-1', 'r') as input_file:
    mapa = input_file.readlines()

width = len(mapa[0]) - 1
height = len(mapa)

def next_pos(x, y):
    return (x + slope[0]) % width, y + slope[1]

def count_trees(slope):
    x, y, trees = 0, 0, 0
    while y < height:
        terrain = mapa[y][x]
        if terrain == '#':
            trees += 1
        x, y = next_pos(x, y)

    return trees

res = 1
for slope in [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]:
    res *= count_trees(slope)

print(res)