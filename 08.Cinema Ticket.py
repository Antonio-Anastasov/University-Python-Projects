day_of_week = input()
result = 0

if day_of_week == 'Wednesday'\
    or day_of_week == 'Thursday':
    result = 14
elif day_of_week == 'Saturday'\
    or day_of_week == 'Sunday':
    result = 16
else:
    result = 12
print(result)