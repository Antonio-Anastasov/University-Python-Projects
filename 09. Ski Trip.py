nights = int(input()) - 1
type_of_room = input()
review = input()

total_price = 0

if type_of_room == 'room for one person':
    total_price = 18

elif type_of_room == 'apartment':
    total_price = 25
    if nights < 10:
        total_price *= 0.70
    elif nights <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50

elif type_of_room == 'president apartment':
    total_price = 35
    if nights < 10:
        total_price *= 0.90
    elif nights <= 15:
        total_price = 0.85
    else:
        total_price *= 0.80

if review == 'positive':
    total_price *= 1.25
else:
    total_price *= 0.90

print(f'{total_price * nights:.2f}')
