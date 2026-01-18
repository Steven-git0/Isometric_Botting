from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time
import random

from PIL import Image
import imagehash

#For bank deposit icon = 7efecbc1c9c2fe00

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

img = Image.open('images/deposit.png')
width, height = img.size
print(f"Width: {width}, Height: {height}")

target_hash = imagehash.average_hash(img)

print(f"Target Hash: {target_hash}")

print(screenscrape.hash_detection(str(target_hash), width, height))