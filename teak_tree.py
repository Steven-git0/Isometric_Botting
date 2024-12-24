from Core_scripts.screen_scraping import *
from Core_scripts.movements import *
from PIL import Image
import time
import pyautogui 

#Woodcutting
for BOTS in range(10):
    while(screenscrape.read_text('is too full') == False):
        mouse_movements.move_mouse(668, 532, 3) 
        mouse_movements.perform_click()

        
        for x in range(15):
            if screenscrape.mouse_text() == False:
                break
            time.sleep(2)

        mouse_movements.move_mouse(738, 531, 3)
        mouse_movements.perform_click()

        if screenscrape.read_text('is too full') == True:
            break

        for x in range(15):
            if screenscrape.mouse_text() == False:
                break
            time.sleep(2)


    mouse_movements.move_mouse(659, 1005, 4)
    mouse_movements.perform_click()

    print('loop terminated')
    image1 = Image.open('tinderbox.png')
    width1, height1 = image1.size[0] // 2, image1.size[1] // 2
    tinderbox = screenscrape.img_detection('tinderbox.png', .95)
    print('tinderbox: ', tinderbox[0])

    #add values to get the center image coords, // because pixels cannot be floats
    image2 = Image.open('teak_logs.png')
    width2, height2 = image2.size[0] // 2, image2.size[1] // 2
    logs = screenscrape.img_detection('teak_logs.png', .95)


    for x in range(22):

        if x == 11:
            mouse_movements.move_mouse(749, 896, 4)
            mouse_movements.perform_click()
            time.sleep(3)


        xcoords1, ycoords1 = tinderbox[0]
        xcoords2, ycoords2 = logs[x]
        mouse_movements.move_mouse(xcoords1 + width1, ycoords1 + height1, 4)
        mouse_movements.perform_click()

        mouse_movements.move_mouse(xcoords2 + width2, ycoords2 + height2, 4)
        mouse_movements.perform_click()

        time.sleep(1.4)
