min_number = int(input())

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    user_input = int(user_input)
    if user_input < min_number:
        min_number = user_input

print(min_number)