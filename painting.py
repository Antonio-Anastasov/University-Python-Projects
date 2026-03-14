PROTECTIVE_NYLON = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

nylon += 2
paint += paint * 0.10

materials_price = \
    (nylon * PROTECTIVE_NYLON) + \
    (paint * PAINT_PRICE) + \
    ( thinner * THINNER_PRICE) + \
    BAGS_PRICE

price_of_one_hour = materials_price * 0.3
total_price = materials_price + (price_of_one_hour * work_hours)

print(total_price)
