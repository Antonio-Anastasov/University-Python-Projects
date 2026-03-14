lst = []

for _ in range(3):
    data = input()
    lst.append(data)

lst[0], lst[2] = lst[2], lst[0]

print(lst)