odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    current_number = sum(ord(char) for char in input()) // i
    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

sum_odd = sum(odd_set)
sum_even = sum(even_set)
if sum_odd == sum_even:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd > sum_even:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
