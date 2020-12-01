with open('input/2', 'r') as input_file:
    nums = [int(line) for line in input_file.readlines()]

for num1 in nums:
    for num2 in nums:
        if num1 == num2:
            continue

        num3 = 2020 - (num1 + num2)
        if num3 in nums:
            print(num1, num2, num3, num1 * num2 * num3)
            exit()
