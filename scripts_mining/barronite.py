from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time
import tkinter as tk
from tkinter import simpledialog

# root = tk.Tk()
# root.title("Motherload mine")
# # Show the input popup
# username = simpledialog.askstring("Userame", "Please enter your characters Username to find the Client:")

# # Show an additional instructions popup
# if username:
#     tk.messagebox.showinfo("Instructions", f"Hello {username}!\n\nPlease follow the steps below:\n1. Step one...\n2. Step two...\n3. Step three...")


window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

def break_roll():
    if random.uniform(0.00, 100.00) <= .50:
                print('taking quick break')
                time.sleep(random.uniform(60.00, 600.00))
iterations = 3
while True:

    #range needs to be in multiples of 4
    for x in range(iterations):
    
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(4.00, 6.00))

        mouse_movements.move_mouse(.51505, .53619, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.00, 6.00))
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(4.00, 6.00))
            break_roll()

        mouse_movements.move_mouse(.41739, .60054, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.00, 6.00))
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(4.00, 6.00))

        mouse_movements.move_mouse(.46488, .54066, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(5.00, 7.00))
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(4.00, 6.00))
            break_roll()

        if x == iterations - 1:
            break
        
        mouse_movements.move_mouse(.60334, .40214, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.00, 6.00))
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(4.00, 6.00))

    mouse_movements.move_mouse(.92734, .51151, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(95.00, 102.00))
    break_roll()

    mouse_movements.move_mouse(.0382, .3974, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(18.50, 21.00))

    mouse_movements.move_mouse(.61723, .51151, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7, 8.50))
