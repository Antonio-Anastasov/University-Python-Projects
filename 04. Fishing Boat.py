budget = int(input())
season = input()
fisherman_count = int(input())

price = 0
total_price = 0

if season == 'Spring':
    price = 3000
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75
elif season == 'Winter':
    price = 2600
    if fisherman_count <= 6:
        price *= 0.9
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count >= 12:
        price *= 0.75


if fisherman_count % 2 == 0 and season != 'Autumn':
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
