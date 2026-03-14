from math import ceil
number_of_people = int(input())
capacity_of_people = int(input())

courses = number_of_people / capacity_of_people

print(ceil(courses))
