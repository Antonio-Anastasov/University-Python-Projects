budget = float(input())
people = int(input())
clothes_price = float(input())

decor = budget * 0.10

if people > 150:
    clothes_price *= 0.90

total_price = decor + people * clothes_price

if total_price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_price:.2f} leva left.')
else:
    print('Not enough money!')
    print(f"Wingard needs {total_price - budget:.2f} leva more.")