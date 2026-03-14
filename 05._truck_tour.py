from collections import deque

pumps_number = int(input())
pumps = deque()

for i in range(pumps_number):
    current_fuel, destination = input().split()
    pumps.append([int(current_fuel), int(destination)])

start_position = 0
stops = 0

while stops < pumps_number:
    fuel = 0
    for  y in range(pumps_number):
        fuel += pumps[y][0]
        destination = pumps[y][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)