lst = []
number_of_input = int(input())
special_word = input()

for _ in range(number_of_input):
    user_input = input()
    lst.append(user_input)
print(lst)

for i in range(len(lst)- 1, - 1 , - 1):
    element = lst[i]
    if special_word not in element:
        lst.remove(element)

print(lst)