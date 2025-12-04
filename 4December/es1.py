file = open("4December/input.txt", "r")
lines = [line.strip() for line in file.readlines()]
file.close()

matrix = [list(line) for line in lines]

result = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "@":
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]):
                        if matrix[ni][nj] == "@":
                            count += 1
            if count < 4:
                result += 1

print(result)
