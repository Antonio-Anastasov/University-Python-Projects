from math import ceil
series_name = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
free_time = break_lenght / 4

total_time = lunch_time + free_time + episode_lenght
time_left = break_lenght - total_time

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")