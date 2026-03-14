n = int(input())
number = []

for _ in range(n):
    current_number = int(input())
    number.append(current_number)

command = input()

filtered_numbers = []

if command == 'even':
    for num in number:
        if num % 2 == 0:
            filtered_numbers.append(num)

if command == 'odd':
    for num in number:
        if num % 2 != 0:
            filtered_numbers.append(num)

if command == 'negative':
    for num in number:
        if num < 0:
            filtered_numbers.append(num)

if command == 'positive':
    for num in number:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)

