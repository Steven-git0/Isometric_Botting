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
#disable level up interface in settings so it doesn't interrupt the script

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)