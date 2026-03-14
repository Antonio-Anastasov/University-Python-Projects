n = int(input())

max_number = float('-inf')
sum_numbers = 0

for _ in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_numbers += number

if max_number == sum_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number -(sum_numbers - max_number))}')