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

print(random.uniform(1, 10))
time.sleep(random.uniform(3.50, 3.75))


for x in range(300):
    #ladder
    mouse_movements.move_mouse(rx+1285, ry+620, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.80, 3.90))

    mouse_movements.move_mouse(rx+880, ry+925, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(18.75, 18.95))

    mouse_movements.move_mouse(rx+665, ry+630, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(1.93, 2.00))

    mouse_movements.move_mouse(rx+615, ry+625, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.50, 5.70))

    mouse_movements.move_mouse(rx+610, ry+520, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(18.45, 18.65))

    mouse_movements.move_mouse(rx+840, ry+430, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.10, 9.20))

    if random.uniform(0, 100) <= 1.5:
        time.sleep(random.uniform(300, 600))
