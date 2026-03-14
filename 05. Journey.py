budget = float(input())
season = input()
place_to_go = ''
place_to_stay = ''

if budget <= 100:
    place_to_go = 'Bulgaria'
    if season == 'summer':
        place_to_stay = 'Camp'
        budget *= 0.30
    elif season == 'winter':
        place_to_stay = 'Hotel'
        budget *= 0.70
elif budget <= 1000:
    place_to_go = 'Balkans'
    if season == 'summer':
        place_to_stay = 'Camp'
        budget *= 0.40
    elif season == 'winter':
        place_to_stay = 'Hotel'
        budget *= 0.80
elif budget > 1000:
    place_to_go = 'Europe'
    place_to_stay = 'Hotel'
    budget *= 0.90

print(f"Somewhere in {place_to_go}")
print(f'{place_to_stay} - {budget:.2f}')
