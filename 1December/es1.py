file = open("1December/input.txt", "r")
lines = [line.strip() for line in file.readlines()]
file.close()

pos = 50       # posizione iniziale
password = 0   # quante volte arrivo a 0

for line in lines:
    direction = line[0]
    number = int(line[1:])

    if direction == "R":
        pos = (pos + number) % 100
    else:  # L
        pos = (pos - number) % 100

    if pos == 0:
        password += 1

print("The password is", password)
