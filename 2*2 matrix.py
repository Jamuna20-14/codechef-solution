rows = 2
cols = 2

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input(f"Enter element [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

print(matrix)

o/p:
Enter element [0][0]: 10
Enter element [0][1]: 20
Enter element [1][0]: 30
Enter element [1][1]: 40
[[10, 20], [30, 40]]
