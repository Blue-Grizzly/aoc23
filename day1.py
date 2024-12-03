input = open("day1_input.txt", "r")
lines = input.readlines()
input.close()

total = 0

for line in lines:
    numbers = ''.join(filter(str.isdigit, line))
    first = numbers[0]
    last = numbers[-1]
    total += int(first + last)
    
print(total)
