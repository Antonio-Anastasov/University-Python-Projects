num_1, num_2 = int(input()), int(input())

for number in range(num_1, num_2 + 1):
    even_sum, odd_sum = 0, 0

    for idx, digit in enumerate(str(number)):
        if idx % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")