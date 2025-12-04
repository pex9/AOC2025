

file = open("3December/input.txt", "r")
lines = [line.strip() for line in file.readlines()]
file.close()
sum = 0
for line in lines:
    max = 0
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            elem = line[i] + line[j]
            if int(elem) > max:
                max = int(elem)
    sum = max + sum
print(sum)

