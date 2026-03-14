n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
max_eggs = float("-inf")
max_direction = ""
max_eggs_matrix = []

for direction, moves in possible_moves.items():
    eggs = 0
    current_eggs_matrix = []
    row = bunny[0] + moves[0]
    col = bunny[1] + moves[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        current_eggs_matrix.append([row, col])
        row += moves[0]
        col += moves[1]

    if eggs > max_eggs and current_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = current_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)