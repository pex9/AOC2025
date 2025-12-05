intervals = []

with open("5December/input.txt") as f:
    for line in f:
        if "-" in line:
            a,b = map(int, line.split("-"))
            intervals.append((a,b))

intervals.sort()

merged = []
current_start, current_end = intervals[0]
for start,end in intervals[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))

count = sum(end - start + 1 for start,end in merged)
print(count)
