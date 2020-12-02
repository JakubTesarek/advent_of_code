with open('input/1-1', 'r') as input_file:
    nums = [int(line) for line in input_file.readlines()]

for num1 in nums:
    num2 = 2020 - num1
    if num2 in nums:
        print(num1, num2, num1 * num2)
        exit()
