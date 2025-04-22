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

def small_break():
    if random.uniform(0, 100) <= .20:
        print('taking break')
        time.sleep(random.uniform(1, 120))

start_time = time.time()
while time.time() - start_time < 21600: 

    mouse_movements.move_mouse(.22397, .87087, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(33.00, 36.50))
    small_break()

    mouse_movements.move_mouse(.46367, .63163, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(33.00, 36.00))
    small_break()

    mouse_movements.move_mouse(.42622, .40941, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5, 6))
    while screenscrape.skill_text() == True:
            time.sleep(random.uniform(2.00, 3.50))

    mouse_movements.move_mouse(.6397, .3023, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(6, 7))

    deposit_inv = screenscrape.img_detection(input_img="osrs_images\deposit.png", threshold= .60)
    x, y = deposit_inv[0]
    mouse_movements.move_mouse(rx+x, ry+y, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.50, 1.00))

    if random.uniform(0, 100) <= 1:
                print('taking quick break')
                time.sleep(random.uniform(10, 300.00))

