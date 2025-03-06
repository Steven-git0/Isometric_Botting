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

while True:
    iteration = 0
    while screenscrape.read_text("full") == False:
    
        print(iteration)
        while screenscrape.skill_text() == True:
            time.sleep(random.uniform(10.00, 15.50))
 
        if iteration < 3:
            mouse_movements.move_mouse(.51161, .47447, 4)
            mouse_movements.perform_click()
            time.sleep(random.uniform(53, 7.50))
            iteration += 1
            mouse_movements.move_mouse(960, 540, 500)
        else:
            iteration = 0
            mouse_movements.move_mouse(.419476, .472472, 4)
            mouse_movements.perform_click()
            time.sleep(random.uniform(7, 7.50))

        if random.uniform(0.00, 100.00) <= 1:
                print('taking quick break')
                time.sleep(random.uniform(60.00, 600.00))
        
    x,y = mouse_movements.relative_move("up", offset = 150)
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.90, 12.40))

    deposit_inv = screenscrape.img_detection(input_img="osrs_images\deposit.png", threshold= .60)
    x, y = deposit_inv[0]
    mouse_movements.move_mouse(rx+x, ry+y, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.50, 1.00))

    mouse_movements.move_mouse(.75206, .90991, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.10, 5.70))

    mouse_movements.move_mouse(.457678, .781782, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7, 8.50))
