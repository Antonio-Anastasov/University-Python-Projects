user_input = int(input())
temp_int = int(input())
max_num = temp_int
min_num = temp_int

for i in range(user_input - 1):
    temp_int = int(input())
    if temp_int < min_num:
        min_num = temp_int
    if temp_int > max_num:
        max_num = temp_int

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')