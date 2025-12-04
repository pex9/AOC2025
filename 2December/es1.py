
def checkId(id):
    #check the id if numbers are repeated twice 
    check = False
    lenght = len(id)
    if lenght%2==0:
        half = lenght//2
        firstHalf = id[:half]
        secondHalf = id[half:]
        if firstHalf == secondHalf:
            check = True
    else:
        pass
    return check

file = open("2December/input.txt", "r")
lines = [line.strip() for line in file.readlines()]
file.close()
rangeIds = [line.split(",") for line in lines]
sum = 0
for r in rangeIds:
    for element in r:
        for i in range(int(element.split("-")[0]), int(element.split("-")[1]) + 1):
            if checkId(str(i)):
                sum += int(i)
print(sum)