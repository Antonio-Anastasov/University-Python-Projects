n = int(input())

negative = []
positive = []

for num in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

count_positive = len(positive)
sum_negative = sum(negative)

print(positive)
print(negative)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')
