user_input = int(input())

result = ''

if -100 <= user_input <= 100 and user_input !=0:
    result = 'Yes'
else:
    result = 'No'

print(result)