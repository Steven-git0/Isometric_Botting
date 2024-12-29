from screen_scraping import *
from movements import *
import threading
import pyautogui 
import time
import sys

def move_contours(x_axis = True, right2left = False):
    #color of teal markers in runelite
    color = [0,253,242]
    #find the teal contours
    teal_markers = screenscrape.find_contours(color, 2)
    #filter out the minimap contours
    filtered_markers = [(x,y) for x,y in teal_markers if not (1245 <= x <= 1400 and 30 <= y <= 185)]
    #Sort by x coordinates, else y coordinates
    if x_axis == True:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
        filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
    else:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)
        filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)

    for x,y in filtered_markers:
        print(x,' ', y)
    return filtered_markers

while True:
    x,y = move_contours()[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()

    time.sleep(random.uniform(3.90, 4.20))

    mouse_movements.move_mouse(264, 928, 2)
    mouse_movements.perform_click()

    time.sleep(random.uniform(80.00, 81.20))