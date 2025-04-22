from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time
import tkinter as tk
from tkinter import simpledialog

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)


location = 1
glove_time = 4.9
#4.8 for expert minging
while True:

    mouse_movements.move_mouse(.489973, .479113, 4)

    while screenscrape.read_text("full") == False:

        mouse_movements.perform_click()

        mouse_movements.move_mouse(.512032, .509162, 4) #move mouse to next objective
        time.sleep(random.uniform(glove_time, (glove_time + .40)))

        if random.uniform(0.00, 100.00) <= .40:
                print('taking quick break')
                time.sleep(random.uniform(55.00, 600.00))

        if screenscrape.read_text("full") == True:
             break
    
        mouse_movements.perform_click()

        mouse_movements.move_mouse(.489973, .477113, 4)
        time.sleep(random.uniform(glove_time, (glove_time + .40)))

        if random.uniform(0.00, 100.00) <= .40:
                print('taking quick break')
                time.sleep(random.uniform(55.00, 600.00))
                


    x,y = mouse_movements.relative_move("left", offset = 150)
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    if location == 1:
        time.sleep(random.uniform(5.50, 6.10))
    else:
         mouse_movements.move_mouse(.322097, .67968, 10)
         time.sleep(random.uniform(3.20, 3.70))

    deposit_inv = screenscrape.img_detection(input_img="osrs_images\deposit.png", threshold= .60)
    x, y = deposit_inv[0]
    mouse_movements.move_mouse(rx+x, ry+y, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.50, 1.00))

    if location == 1:
        mouse_movements.move_mouse(.697382, .377377, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(5.50, 6.10))
    elif location == 2:
        mouse_movements.move_mouse(.620974, .513514, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(3.10, 3.50))