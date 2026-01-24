import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pywinctl as gw
import time
import tkinter as tk
from tkinter import simpledialog

#WORLD 302
#in setting esc closes the current interface enabled

window_title = "RuneLite - litlGenocide"

windows = gw.getWindowsWithTitle(window_title)
window = windows[0]
rx = window.left
ry = window.top
width = window.width
height = window.height
    
mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

def small_break():
    if random.uniform(0, 100) <= 2:
        print('taking break')
        time.sleep(random.uniform(60, 600))

def check_distance():

    mx, my = pyautogui.position()
    points = mouse_movements.move_contours(color=[5, 250, 250])
    x, y = tuple(map(lambda s: s / len(points), map(sum, zip(*points)))) if points else (None, None)
    distance = ((mx-(x))**2 + (my-(y+3))**2)**.5

    return distance if distance else float('inf')
    

food_item = screenscrape.last_inventory()
medium_diary = True

if medium_diary == True:
    coin_limit = 100
else:
    coin_limit = 50


start_time = time.time()

counter = 0
while time.time() - start_time < 21600: 
    first_time = True
    while screenscrape.check_health() == False:

        points = mouse_movements.move_contours(color=[5, 250, 250])
        x, y = tuple(map(lambda s: s / len(points), map(sum, zip(*points)))) if points else (None, None)
        mouse_movements.move_mouse(x, y+2, 1)

        while check_distance() <= 20 and counter < coin_limit and screenscrape.check_health() == False:
            mouse_movements.perform_click()
            if first_time == True:
                time.sleep(random.uniform(1.4, 1.60))
                first_time = False
            else:
                time.sleep(random.uniform(.20, .65))

            counter += 1

        if counter >= coin_limit and screenscrape.check_health() == False:
            time.sleep(random.uniform(4.00, 4.20))
            mouse_movements.move_mouse(rx+width-210, ry+height-295, 3)
            mouse_movements.perform_click()
            counter = 0

    #for stun
    time.sleep(random.uniform(4, 4.5))

    if len(screenscrape.img_detection(input_img = food_item)) < 3:    

        x,y = mouse_movements.move_contours()[0]
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(9.00, 9.50)) 

        x,y = screenscrape.img_detection(food_item, threshold= .70)[0]
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()

        time.sleep(random.uniform(1.5, 1.70))
        pyautogui.press('esc')

    else:
        for _ in range(3):
            x,y = screenscrape.img_detection(food_item)[-1]
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(1.20, 1.50))
    small_break()
    coin_limit += random.randint(-2, 2)

