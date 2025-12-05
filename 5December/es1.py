file = open("5December/input.txt", "r")
vectorMin = []
vectorMax = []
count = 0
for line in file.readlines():
    if "-" in line:
        parts = line.strip().split("-")
        vectorMin.append(parts[0])
        vectorMax.append(parts[1])
    if line.strip() != "" and "-" not in line:
        # check
        for i in range(len(vectorMin)):
            if int(line.strip()) >= int(vectorMin[i]) and int(line.strip()) <= int(vectorMax[i]):
                count += 1
                break    
file.close()
print(count)