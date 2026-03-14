PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINNIONS_PRICE = 8.20
TRUCK_PRICE = 2

excursion_price = float(input())

puzzle_curtain = int(input())
talking_dol_curtain = int(input())
teddy_bear_curtain = int(input())
minnions_curtain = int(input())
trucks_curtain = int(input())

total_toys_curtain = (
    puzzle_curtain +
    talking_dol_curtain +
    teddy_bear_curtain +
    minnions_curtain +
    trucks_curtain
)

total_toys_price = (
    puzzle_curtain * PUZZLE_PRICE +
    talking_dol_curtain * TALKING_DOLL_PRICE +
    teddy_bear_curtain * TEDDY_BEAR_PRICE +
    minnions_curtain * MINNIONS_PRICE +
    trucks_curtain * TRUCK_PRICE
)

if total_toys_curtain >= 50:
    total_toys_price *= 0.75

total_toys_price *= 0.90

if total_toys_price >= excursion_price:
    print(f'Yes! {total_toys_price - excursion_price:.2f} lv left.')
else:
    print(f'Not enough money! {excursion_price - total_toys_price:.2f} lv needed.')
