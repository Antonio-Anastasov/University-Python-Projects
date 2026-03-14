user_input = int(input())

tank_capacity = 255

for added_water in range(user_input):
    litters_of_water = int(input())
    if tank_capacity - litters_of_water < 0:
        print('Insufficient capacity!')
        continue
    tank_capacity -= litters_of_water
print(255 - tank_capacity)