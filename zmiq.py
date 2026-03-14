product = input()
city = input()
count = float(input())
final_price = 0

if city == 'Sofia':
    if product == 'coffee':
        final_price = count * 0.50
    elif product == 'water':
        final_price = count * 0.80
    elif product == 'beer':
        final_price = count * 1.20
    elif product == 'sweets':
        final_price = count * 1.45
    elif product == 'peanuts':
        final_price = count * 1.60
elif city == 'Varna':
    if product == 'coffee':
        final_price = count * 0.45
    elif product == 'water':
        final_price = count * 0.70
    elif product == 'beer':
        final_price = count * 1.10
    elif product == 'sweets':
        final_price = count * 1.35
    elif product == 'peanuts':
        final_price = count * 1.55
elif city == 'Plovdiv':
    if product == 'coffee':
        final_price = count * 0.40
    elif product == 'water':
        final_price = count * 0.70
    elif product == 'beer':
        final_price = count * 1.15
    elif product == 'sweets':
        final_price = count * 1.30
    elif product == 'peanuts':
        final_price = count * 1.50

print(final_price)
