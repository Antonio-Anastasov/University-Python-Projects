from math import floor

tournaments = int(input())
starting_points = int(input())

win_tournaments = 0
gained_points = 0

for _ in range(tournaments):
    tournament_position = input()

    if tournament_position == 'W':
        gained_points += 2000
        win_tournaments += 1
    elif tournament_position == 'F':
        gained_points += 1200
    elif tournament_position == 'SF':
        gained_points += 720

print(f'Final points: {gained_points + starting_points}')
print(f'Average points: {floor(gained_points / tournaments)}')
print(f'{win_tournaments / tournaments * 100:.2f}%')
