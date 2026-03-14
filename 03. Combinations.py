n = int(input())
counter = 0

for i in range(0, n + 1):
    for j in range(0, n + 1):
        for k in range(0, n + 1):
            if i + j + k == n:
                counter += 1

print(counter)