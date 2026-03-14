fruit = input()
day_of_week = input()
count = float(input())
result = 'error'

if day_of_week == 'Monday'\
    or day_of_week == 'Tuesday'\
    or day_of_week == 'Wednesday'\
    or day_of_week == 'Thursday'\
    or day_of_week == 'Friday':
    if fruit == 'banana':
        result = count * 2.50
    elif fruit == 'apple':
        result = count * 1.20
    elif fruit == 'orange':
        result = count * 0.85
    elif fruit == 'grapefruit':
        result = count * 1.45
    elif fruit == 'kiwi':
        result = count * 2.70
    elif fruit == 'pineapple':
        result = count * 5.5
    elif fruit == 'grapes':
        result = count * 3.85
elif day_of_week == 'Saturday'\
        or day_of_week == 'Sunday':
    if fruit == 'banana':
        result = count * 2.70
    elif fruit == 'apple':
        result = count * 1.25
    elif fruit == 'orange':
        result = count * 0.90
    elif fruit == 'grapefruit':
        result = count * 1.60
    elif fruit == 'kiwi':
        result = count * 3.00
    elif fruit == 'pineapple':
        result = count * 5.6
    elif fruit == 'grapes':
        result = count * 4.20
if result == 'error':
    print(result)
else:
    print(f'{result:.2f}')
