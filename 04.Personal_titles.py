age = float(input())
gender = input()
result = ''

if gender == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'

if gender == 'f':
    if age >= 16:
        result = 'Ms.'
    else:
        result = 'Miss'

print(result)