from screen_scraping import *
from movements import *
from PIL import Image
import time
import random
import threading
import pyautogui 
#Minimap location for me is 125+155 and 30+155
#Inventory location for me is 1210 + 190 and 720 +260


color = [0,253,242]
def fishing_contours():
    teal_markers = screenscrape.find_contours(color, 2)
    #filter out the minimap contours
    filtered_markers = [(x,y) for x,y in teal_markers if not (1245 <= x <= 1400 and 30 <= y <= 185)]
    filtered_markers = sorted(filtered_markers, key= lambda x: x[1])
    for x,y in filtered_markers:
        print(x,' ', y)
    return filtered_markers

for x in range(20):
#starting point is the ship
    y = None
    while(y is None):
        first_markers = fishing_contours()
        if first_markers:
            x, y = first_markers[0]
        print('finding')
    #move to ladder
    mouse_movements.move_mouse(x, y, 1)
    mouse_movements.perform_click()

    time.sleep(random.uniform(3.2, 4))
    #move to relative tile 
    mouse_movements.move_mouse(670, 598, 2)
    mouse_movements.perform_click()

    start_time = time.time()
    end_time = 315

    while time.time() - start_time <= end_time:
        #right side
        mouse_movements.move_mouse(893, 524, 1)
        time.sleep(5)
        #check for text
        while screenscrape.mouse_text().find('Chop Enormous') == -1 and time.time() - start_time <= end_time:
            time.sleep(1)
            print('finding green')
        if time.time() - start_time <= end_time:
            mouse_movements.perform_click()
            time.sleep(random.uniform(3.90, 4.10))
        if time.time() - start_time <= end_time:
            #in case if kraken whips
            mouse_movements.move_mouse(830, 527, 3)
            mouse_movements.perform_click()
            time.sleep(random.uniform(14.9, 15.10))
        if time.time() - start_time <= end_time:
            #find relative square again
            x, y = (fishing_contours())[0]
            mouse_movements.move_mouse(x, y, 1)
            mouse_movements.perform_click()
        
        #move mouse where kraken spawns and use timer to avoid other players
        mouse_movements.move_mouse(519, 526, 1)
        time.sleep(5)

        #check for text
        while screenscrape.mouse_text().find('Chop Enormous') == -1 and time.time() - start_time <= end_time:
            time.sleep(1)
            print('finding green')
        if time.time() - start_time <= end_time:
            mouse_movements.perform_click()
            time.sleep(random.uniform(3.90, 4.10))
        if time.time() - start_time <= end_time:
            #in case if kraken whips
            mouse_movements.move_mouse(574, 585, 3)
            mouse_movements.perform_click()
            time.sleep(random.uniform(14.9, 15.10))
        if time.time() - start_time <= end_time:
            #find relative square again
            x, y = (fishing_contours())[0]
            mouse_movements.move_mouse(x, y, 1)
            mouse_movements.perform_click()

    print('loop done')

    time.sleep(10)

    x, y = (fishing_contours())[0]

    mouse_movements.move_mouse(x, y, 1)
    mouse_movements.perform_click()
    time.sleep(6)

    image1 = Image.open('quick_bank.png')
    width1, height1 = image1.size[0] // 2, image1.size[1] // 2
    quickbank = screenscrape.img_detection('quick_bank.png', .90)
    x,y = quickbank[0]
    mouse_movements.move_mouse(x+width1, y+height1, 1)
    mouse_movements.perform_click()

    time.sleep(random.uniform(3.00, 4.20))
    x, y = (fishing_contours())[1]

    mouse_movements.move_mouse(x, y, 1)
    mouse_movements.perform_click()
    time.sleep(15)
