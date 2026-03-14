user_input = input()
sum = 0

for i in range(0, len(user_input)):
    temp_char = user_input[i]
    if temp_char == "a":
        sum += 1
    elif temp_char == "e":
        sum += 2
    elif temp_char == 'i':
        sum += 3
    elif temp_char == "o":
        sum += 4
    elif temp_char == "u":
        sum += 5

print(sum)
