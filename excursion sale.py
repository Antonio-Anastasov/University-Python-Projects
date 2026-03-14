sea_excursions = int(input())
mountain_excursions = int(input())

# Пресмятане на първоначалната печалба
initial_profit = 0

# Продажба на екскурзии
while True:
    command = input()
    if command == "Stop":
        break

    if command == "sea":
        if sea_excursions > 0:
            sea_excursions -= 1
            initial_profit += 680
    elif command == "mountain":
        if mountain_excursions > 0:
            mountain_excursions -= 1
            initial_profit += 499

    if sea_excursions == 0 and mountain_excursions == 0:
        print("Good job! Everything is sold.")
        break
print(f"Profit: {initial_profit} leva.")