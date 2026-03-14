lenght = int(input())
width = int(input())
hight = int(input())
percent = float(input()) / 100

area = lenght * width * hight
area_in_liters = area * 0.001
needed_water = area_in_liters *(1 - percent)

print(needed_water)
