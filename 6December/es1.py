
operations = []
numbers = []
sum = 0
with open("6December/input.txt") as f:
    for line in f:
        if "+" in line or "-" in line or "*" in line or "/" in line:
            operations = line.split()
        else:
            number = line.split()
            numbers.append(number)
for i in range(len(operations)):
    partial_sum = 0
    if operations[i] == "+":
        for j in range(len(numbers)):
            partial_sum += int(numbers[j][i])
    elif operations[i] == "*":
        partial_sum = 1
        for j in range(len(numbers)):
            partial_sum *= int(numbers[j][i])
    sum += partial_sum
print(sum)