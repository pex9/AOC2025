matrix = []
with open("7December/input.txt") as f:
    for line in f:
        matrix.append(list(line.strip()))
count_splits = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j] == "S" and i == 0):
            # first row go the laser down
            if (matrix[i+1][j] == "." and i+1 < len(matrix)):
                matrix[i+1][j] = "|"
            if (matrix[i+1][j] == "^" and i+1 < len(matrix) and j < len(matrix[i])):
                # need to change direction to left and right
                matrix[i+1][j+1] = "|"
                matrix[i+1][j-1] = "|"
                count_splits += 1
        if (matrix[i][j] == "|"):
            if (i+1 < len(matrix) and matrix[i+1][j] == "."):
                matrix[i+1][j] = "|"
            if (i+1 < len(matrix) and matrix[i+1][j] == "^"):
                # need to change direction to left and right
                if (j+1 < len(matrix[i])):
                    matrix[i+1][j+1] = "|"
                if (j-1 >= 0):
                    matrix[i+1][j-1] = "|"
                count_splits += 1
print(count_splits)
for row in matrix:
    print("".join(row))