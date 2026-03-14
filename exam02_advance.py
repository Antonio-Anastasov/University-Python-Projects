def main():
    N = int(input())

    grid = []
    pacman_pos = None
    stars_count = 0
    for i in range(N):
        row = list(input().strip())
        grid.append(row)
        if 'P' in row:
            pacman_pos = (i, row.index('P'))
        stars_count += row.count('*')

    health = 100
    frozen = False
    collected_stars = 0

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    while True:
        command = input().strip()
        if command == "end":
            break

        dx, dy = directions[command]
        new_row = (pacman_pos[0] + dx) % N
        new_col = (pacman_pos[1] + dy) % N

        grid[pacman_pos[0]][pacman_pos[1]] = '-'

        cell = grid[new_row][new_col]
        if cell == '*':
            collected_stars += 1
            stars_count -= 1
            if stars_count == 0:
                break
        elif cell == 'G':
            if not frozen:
                health -= 50
                if health <= 0:
                    health = 0
                    break
            else:
                frozen = False
        elif cell == 'F':
            frozen = True

        pacman_pos = (new_row, new_col)
        grid[new_row][new_col] = 'P'

    if health <= 0:
        print(f"Game over! Pacman last coordinates [{pacman_pos[0]},{pacman_pos[1]}]")
    elif stars_count == 0:
        print("Pacman wins! All the stars are collected.")
    else:
        print("Pacman failed to collect all the stars.")

    print(f"Health: {health}")

    if stars_count > 0:
        print(f"Uncollected stars: {stars_count}")

    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    main()