"""import clavier


def listen_keyboard():
    if clavier.is_pressed("LEFT"):
        return "LEFT"

def listen_keyboard():
    if clavier.is_pressed("RIGHT"):
        return "RIGHT"


def listen_keyboard():
    if clavier.is_pressed("DOWN"):
        return "DOWN"
def listen_keyboard():
    if clavier.is_pressed("UP"):
        return "UP"
"""


import keyboard
import os
import time

def handle_key_press(key, action):
    """
    Handles key press events.

    Parameters:
    - key: The key to check for.
    - action: The action to perform when the key is pressed.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(action)
    while keyboard.is_pressed(key):
        time.sleep(0.01)  # Adjust the delay as needed


"""
while True:
    if keyboard.is_pressed("LEFT"):
        handle_key_press("LEFT", "L")
        current_position -= 1
        while keyboard.is_pressed("LEFT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("RIGHT"):
        handle_key_press("RIGHT", "R")
        current_position += 1
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("UP"):
        handle_key_press("UP", "U")
        while keyboard.is_pressed("UP"):
            time.sleep(0.01)

    elif keyboard.is_pressed("DOWN"):
        handle_key_press("DOWN", "D")
        while keyboard.is_pressed("DOWN"):
            time.sleep(0.01)

    elif keyboard.is_pressed("A"):
        handle_key_press("A", "Function A")
        current_position = 0  # Reset the position
        while keyboard.is_pressed("A"):
            time.sleep(0.01)

    # Add a delay to avoid constant checking (adjust as needed)
    time.sleep(0.1)
"""

