hours = int(input())
day_of_week = input()
result = 'closed'

if 10 <= hours <= 18 and day_of_week != 'Sunday':
    result = 'open'

print(result)