exam_hour = int(input())
exam_minutes = int(input())
arrive_time_hours = int(input())
arrive_time_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
students_time_in_minutes = arrive_time_hours * 60 + arrive_time_minutes

time_difference = exam_time_in_minutes - students_time_in_minutes

if time_difference > 30:
    print("Early")
elif time_difference < 0:
    print("Late")
else:
    print(f"On time")

hours = abs(time_difference) // 60
minutes = abs(time_difference) % 60

result = ''

if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_difference > 0:
    result += ' before the start'
elif time_difference < 0:
    result += ' after the start'

print(result)