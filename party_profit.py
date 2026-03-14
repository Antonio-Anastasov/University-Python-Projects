number_of_company = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_company -= 2
    if current_day % 15 == 0:
        number_of_company += 5
    if current_day % 3 == 0:
        coins -= 3 * number_of_company
    if current_day % 5 == 0:
        coins += 20 * number_of_company
        if current_day % 3 == 0:
            coins -= 2 * number_of_company
    coins += 50
    coins -= 2 * number_of_company
coins_per_companies = coins // number_of_company
print(f'{number_of_company} companions received {coins_per_companies} coins each.')