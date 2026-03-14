pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

total_time_needed = pages // pages_per_hour
pages_per_day = total_time_needed // total_days

print(pages_per_day)
