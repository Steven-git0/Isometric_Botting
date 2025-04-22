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
    if random.uniform(0, 100) <= 3:
        print('taking break')
        time.sleep(random.uniform(1, 10))

start_time = time.time()

time.sleep(random.uniform(1, 2))

while time.time() - start_time < 21600: 
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.35, 4.00))
    small_break()

    if random.uniform(0, 100) <= 1:
                print('taking quick break')
                time.sleep(random.uniform(10, 300.00))