user_input = int(input())
odd = 0
even = 0

for i in range(user_input):
    temp_int = int(input())
    if i % 2 == 0:
        odd += temp_int
    else:
        even += temp_int

if odd == even:
    print('Yes')
    print(f'Sum = {odd}')
else:
    diff = abs(odd - even)
    print('No')
    print(f'Diff = {diff}')