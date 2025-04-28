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

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

start_time = time.time()
while time.time() - start_time < 21600: 

    while screenscrape.read_text("here") == False:
        x,y = screenscrape.npz_detection('image_identification/raw_monkfish.npz', threshold= .50)[-1]
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(20.00, 25.00))

        while screenscrape.skill_text() == True and screenscrape.read_text("here") == False:
            time.sleep(random.uniform(13.00, 17.00))
    
    x,y = mouse_movements.relative_move()
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.00, 8.00))

    mouse_movements.move_mouse(.25485, .7882, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.00, 6.00))

    x,y = screenscrape.npz_detection('image_identification/deposit_inv.npz')[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.50, 1.20))

    x,y = mouse_movements.relative_move()
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.00, 6.00))

