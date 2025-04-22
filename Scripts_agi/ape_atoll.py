from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time

window_title = "RuneLite - litlGenocide"
mouse_movements= mouse_movements(window_title)
screenscrape = screenscrape(window_title)

def small_break():
    if random.uniform(0, 100) <= .15:
        print('taking break')
        time.sleep(random.uniform(1, 120))

for x in range(320):
    
    mouse_movements.move_mouse(.21124, .53854, 5)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.20, 4.50))
    small_break()
    
    mouse_movements.move_mouse(.38801, .66667, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.50, 5.75))
    small_break()
    
    mouse_movements.move_mouse(.48764, .53456, 5)
    mouse_movements.perform_click()
    time.sleep(random.uniform(2.70, 3.00))
    small_break()
    
    mouse_movements.move_mouse(.46292, .52152, 5)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.70, 5.05))
    small_break()
    
    mouse_movements.move_mouse(.46517, .5025, 5)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.80, 5.05))

    if screenscrape.color_check(.56629, .7027, desired_color = [100,0,0]):
        mouse_movements.move_mouse(.56629, .7027, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(2.90, 3.20))

        mouse_movements.move_mouse(.68989, .62262, 4)
        mouse_movements.perform_click()
        time.sleep(random.uniform(3.85, 4.15))

    else:
        mouse_movements.move_mouse(.78800, .87187, 5)
        mouse_movements.perform_click()
        time.sleep(random.uniform(5.90, 6.15))
        small_break()

    mouse_movements.move_mouse(.50936, .42743, 5)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.00, 9.20))
    small_break()

    if random.uniform(0, 100) <= 1.5:
        print('taking break')
        time.sleep(random.uniform(300, 900))