import turtle
import random
import os

# Set up the screen
wn = turtle.Screen()
wn.title("razbivach na meteori")
wn.bgcolor("cyan")
wn.setup(width=1920, height=1080)
wn.tracer(0)  # Turn off screen updates

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-1920, -1080)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("black")
player.shape("triangle")
player.shapesize(stretch_wid=5, stretch_len=6.5)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 20

# Create the weapons
weapons = []
for _ in range(3):
    weapon = turtle.Turtle()
    weapon.color("black")
    weapon.shape("circle")
    weapon.shapesize(stretch_wid=0.5, stretch_len=0.5)
    weapon.penup()
    weapon.speed(0)
    weapon.setheading(90)
    weapon.hideturtle()
    weapons.append(weapon)

weapon_speed = 30
weapon_state = "ready"  # ready to fire

# Create the meteors
meteors = []

# Function to move the player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -1982:
        x = -1080
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 1920:
        x = 1080
    player.setx(x)

# Function to move the player up and down
def move_up():
    y = player.ycor()
    y += player_speed
    if y > 1920:
        y = 1080
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= player_speed
    if y < -1920:
        y = -1080
    player.sety(y)

# Function to fire the weapons
def fire_weapon():
    global weapon_state
    if weapon_state == "ready":
        os.system("afplay laser.wav&")  # macOS
        for weapon in weapons:
            weapon_state = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            weapon.setposition(x, y)
            weapon.showturtle()
            x += (weapons.index(weapon) - 1) * 20
            weapon.setx(x)

# Function to spawn meteors
def spawn_meteor():
    meteor = turtle.Turtle()
    meteor.color("brown")
    meteor.shape("circle")
    meteor.shapesize(stretch_wid=1, stretch_len=1.5)
    meteor.penup()
    meteor.speed(0)
    x = random.randint(-1920, 1080)
    y = random.randint(300, 400)
    meteor.setposition(x, y)
    meteors.append(meteor)

# Function to update the score
def update_score():
    global score, high_score
    score += 10
    if score > high_score:
        high_score = score
    score_pen.clear()
    score_pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Function to display game over text
def game_over():
    game_over_pen.goto(0, 0)
    game_over_pen.write("Game Over", align="center", font=("Courier", 30, "normal"))
    play_again_btn.showturtle()

# Function to play again
def play_again(x, y):
    global score
    os.system("python3 script.py")  # Replace 'script.py' with the name of your Python script
    wn.bye()

# Bind movement functions to key presses
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(fire_weapon, "space")

# Bind movement functions to key releases (to allow continuous movement)
wn.onkeyrelease(move_left, "Left")
wn.onkeyrelease(move_right, "Right")
wn.onkeyrelease(move_up, "Up")
wn.onkeyrelease(move_down, "Down")

# Create the score display
score = 0
high_score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Create the game over text
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()

# Create the play again button
play_again_btn = turtle.Turtle()
play_again_btn.speed(0)
play_again_btn.color("red")
play_again_btn.penup()
play_again_btn.hideturtle()
play_again_btn.goto(0, -260)
play_again_btn.write("Play Again", align="center", font=("Courier", 24, "normal"))

# Register click event for play again button
wn.onclick(play_again)

# Main game loop
while True:
    wn.update()  # Update the screen

    # Move the weapons upwards
    if weapon_state == "fire":
        for weapon in weapons:
            y = weapon.ycor()
            y += weapon_speed
            weapon.sety(y)

    # Check if weapons have reached the top
    if all(weapon.ycor() > 1080 for weapon in weapons):
        for weapon in weapons:
            weapon.hideturtle()
        weapon_state = "ready"

    # Spawn meteors
    if len(meteors) < 20:  # Adjust this value as needed
        spawn_meteor()

    # Move the meteors downwards
    for meteor in meteors:
        y = meteor.ycor()
        y -= 0.1  # Adjust this value for meteor speed
        meteor.sety(y)

        # Check for collision with the player
        if meteor.distance(player) < 20:
            os.system("afplay explosion.wav&")  # macOS
            player.hideturtle()
            game_over()
            break

        # Check for collision with the weapons
        for weapon in weapons:
            if weapon.distance(meteor) < 20:
                os.system("afplay explosion.wav&")  # macOS
                weapon.hideturtle()
                weapon_state = "ready"
                x = random.randint(-200, 200)
                y = random.randint(300, 400)
                meteor.setposition(x, y)
                update_score()
                break
