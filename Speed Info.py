user_input = float(input())
speed = ''

if user_input <= 10:
    speed = 'slow'
elif user_input <= 50:
    speed = 'average'
elif user_input <= 150:
    speed = 'fast'
elif user_input <= 1000:
    speed = 'ultra fast'
else:
    speed = 'extremely fast'

print(speed)
