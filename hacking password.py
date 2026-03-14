import random
import pyautogui

characters = "abcdefghijklmnopqrstuvwxyz0123456789"
characters_list = list(characters)

password = pyautogui.password("Enter a password: ")

guess_password = ""

while (guess_password != password):
    guess_password = random.choices(characters_list, k=len(password))

    print("<===============" + str(guess_password) + "===============>")

    if(guess_password == list(password)):
        print("Your Password is: " + "".join(guess_password))
        break