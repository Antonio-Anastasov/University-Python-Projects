screening_type = input()
rows = int(input())
columns = int(input())
income = 0

PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

total_tickets = rows * columns

if screening_type == 'Premiere':
    income = total_tickets * PREMIERE_PRICE
elif screening_type == 'Normal':
    income = total_tickets * NORMAL_PRICE
elif screening_type == 'Discount':
    income = total_tickets * DISCOUNT_PRICE

print(f'{income:.2f} leva')