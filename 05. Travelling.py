while True:
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())
    money = 0
    while True:
        user_input = float(input())
        money += user_input
        if money >= needed_money:
            print(f'Going to {destination}!')
            break