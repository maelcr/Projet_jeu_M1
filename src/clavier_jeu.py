


import keyboard
import os
import time

def handle_key_press(key, action):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(action)
    while keyboard.is_pressed(key):
        time.sleep(0.01)  # Adjust the delay as needed




