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

# if screenscrape.mouse_text() == 'calcified':
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(50.00, 60.40))

#     if random.uniform(0, 100) <= 1:
#         print('taking break')
#         time.sleep(random.uniform(300, 400))


def move_out():
    
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.60, 7.80))
    print('done')
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.10, 7.30))
    print('done')
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.70, 7.90))
    print('done')


    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.70, 7.90))
    print('done')
    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.10, 7.30))
    print('done')

    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.60, 7.80))
    print('done')

def cooking():
    mouse_movements.move_mouse(rx+795, ry+387, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.60, 4.80))
    print('done')

    pyautogui.press('1')
    time.sleep(random.uniform(40.00, 40.80))

    mouse_movements.move_mouse(rx+652, ry+788, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.60, 4.80))

    mouse_movements.move_mouse(rx+809, ry+860, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(1.60, 1.80))

    mouse_movements.move_mouse(rx+809, ry+860, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(1.60, 1.80))

    mouse_movements.move_mouse(rx+796, ry+63, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(1.60, 1.80))

while True:
   time.sleep(600)
   print("aggrotimer reached")
   time.sleep(100)
   move_out()
    
