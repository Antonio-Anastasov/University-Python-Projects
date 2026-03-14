stacks = []
n = int(input())

for i in range(n):
    query = input().split()
    if query[0] == "1":
        stacks.append(int(query[1]))
    elif stacks:
        if query[0] == "2":
            stacks.pop()
        elif query[0] == "3":
            print(max(stacks))
        elif query[0] == "4":
            print(min(stacks))

while stacks:
    print(stacks.pop(), end="")
    if stacks:
        print(", ", end="")