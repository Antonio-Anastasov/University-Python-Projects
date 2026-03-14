number = int(input())
sum = 0

while True:
    user_input = int(input())
    sum += user_input
    if sum >= number:
        break

print(sum)
