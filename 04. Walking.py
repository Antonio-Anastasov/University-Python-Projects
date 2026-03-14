GOAL = 10_000
steps_walked = 0

while steps_walked < GOAL:
    steps = input()

    if steps == "Going home":
        steps_walked += int(input())
        break

    steps_walked += int(steps)

if steps_walked >= GOAL:
    print("Goal reached! Good job!")
    print(f"{steps_walked - GOAL} steps over the goal!")
else:
    print(f"{GOAL - steps_walked} more steps to reach goal.")