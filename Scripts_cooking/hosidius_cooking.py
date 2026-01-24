import sys
import os

# Add the parent directory (Isometric_Botting) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core_scripts.screen_scraping import *
from core_scripts.movements import *                                                                                                                                                    
import time
import random
from PIL import Image
import imagehash
import pyautogui

#make sure last item in inventory is the item to be cooked
#item must be visible in the bank on the first page
#withdrawl the item you want to cook close the bank page
#stand to the north side of the bank chest
#disable level up interface in settings so it doesn't interrupt the script

window_title = "RuneLite - litlGenocide"

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)
cook_item = screenscrape.last_inventory()
counter = 0 
deposit_x, deposit_y = 0, 0
raw_x, raw_y = 0, 0

while counter < 280:
    #starting position above bank chest
    mouse_movements.move_mouse(.52977, .3521, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3, 3.4))

    #cook item
    pyautogui.press('1')
    time.sleep(random.uniform(68, 75))

    #random break
    if random.uniform(1.00, 10.00) > 9.2:
        print("taking a break")
        time.sleep(random.uniform(60, 600))

    #go back to bank chest
    mouse_movements.move_mouse(.43679, .70152, 4)
    mouse_movements.perform_click()
    if counter < 1:
        mouse_movements.move_mouse(.65, .65, 20)
    time.sleep(random.uniform(3, 3.35))

    #find the deposit button and raw food for the first time
    if counter < 1:
        deposit_x, deposit_y = screenscrape.hash_detection('7efecbc1c9c2fe00', 40, 40)
    
    #deposit inventory
    mouse_movements.move_mouse(deposit_x, deposit_y, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.5, 1.2))

    if counter < 1:
        raw_x, raw_y = screenscrape.img_detection(cook_item, threshold = .90)[0]
    #withdraw raw food
    mouse_movements.move_mouse(raw_x, raw_y, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.5, 2.1))
    
    #leave bank
    pyautogui.press('esc')
    counter += 1
