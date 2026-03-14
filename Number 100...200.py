user_input = int(input())
result = ''

if user_input < 100:
    result = 'Less than 100'
elif user_input > 200:
    result = 'Greater than 200'
else:
    result = 'Between 100 and 200'

print(result)