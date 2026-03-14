username = input()
password = input()

while True:
    user_input = input()
    if user_input == password:
        break

print(f'Welcome {username}!')
