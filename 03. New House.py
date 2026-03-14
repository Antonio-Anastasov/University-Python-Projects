type_flower = input()
flowers_count = int(input())
budget = int(input())

total_price = 0

ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

if type_flower == 'Roses':
    total_price = flowers_count * ROSE_PRICE
    if flowers_count > 80:
        total_price *= 0.90
elif type_flower == 'Dahlias':
    total_price = flowers_count * DAHLIA_PRICE
    if flowers_count > 90:
        total_price *= 0.85
elif type_flower == 'Tulips':
    total_price = flowers_count * TULIP_PRICE
    if flowers_count > 80:
        total_price *= 0.85
elif type_flower == 'Narcissus':
    total_price = flowers_count * NARCISSUS_PRICE
    if flowers_count < 120:
        total_price *= 1.15
elif type_flower == 'Gladiolus':
    total_price = flowers_count * GLADIOLUS_PRICE
    if flowers_count < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {type_flower} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
