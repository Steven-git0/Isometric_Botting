from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time

window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements()


time.sleep(random.uniform(2.50, 2.50))


def fishing_area(bool = False):
    fish_spots = screenscrape.img_detection('C:/Users/Steven/Runescape/osrs_images/monk_fish.png', .60)
    filtered_spots = sorted(fish_spots, key= lambda x: x[0], reverse = bool)
    print(filtered_spots)
    image = Image.open('C:/Users/Steven/Runescape/osrs_images/monk_fish.png')
    width, height = image.size[0] // 2, image.size[1] // 2
    #make a new array, tuples are immutable 
    new_array = []
    for x,y in filtered_spots:
        new_spots = (x + width, y +height)
        new_array.append(new_spots)
    return new_array

print(fishing_area()[0])

x,y 