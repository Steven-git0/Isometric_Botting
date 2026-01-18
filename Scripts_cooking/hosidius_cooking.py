from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time
import random
from PIL import Image
import imagehash

#make sure last item in inventory is the item to be cooked
#item must be visible in the bank on the first page
#withdrawl the item you want to cook close the bank page
#stand to the north side of the bank chest

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

cook_item = screenscrape.last_inventory()
# while True:
        
#     mouse_movements.move_mouse(.540824, .814815, 4)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(3.22, 3.44))
#     mouse_movements.move_mouse(.435206, .669666, 4)
#     time.sleep(random.uniform(1.00, 1.10))
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(2.50, 3.00))
