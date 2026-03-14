snowballs_count = int(input())

max_weight = 0
max_time = 0
max_value = 0
max_quality = 0

for current_ball in range(snowballs_count):
    weight_of_snowballs = int(input())
    time_needed = int(input())
    quality_of_snowballs = int(input())
    value_of_snowball = (weight_of_snowballs / time_needed) ** quality_of_snowballs
    if value_of_snowball > max_value:
        max_value = value_of_snowball
        max_weight = weight_of_snowballs
        max_time = time_needed
        max_quality = quality_of_snowballs
print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")