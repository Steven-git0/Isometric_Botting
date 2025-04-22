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


def bank_items():
    x,y = mouse_movements.relative_move('up')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.50, 7.70))
    print('done')
    x,y = mouse_movements.relative_move('up')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(6.00, 6.20))
    print('done')
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(8.60, 8.80))
    print('done')
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.10, 7.30))
    print('done')
    x,y = mouse_movements.relative_move('left')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(8.70, 8.90))
    print('done')

    #click deposit items
    mouse_movements.move_mouse(rx+560, ry+610, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(2.0, 2.0))
    print('done')

    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(8.70, 8.90))
    print('done')
    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.10, 7.30))
    print('done')

    x,y = mouse_movements.relative_move('right')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(8.60, 8.80))
    print('done')
    x,y = mouse_movements.relative_move('down')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(6.00, 6.20))
    print('done')

    x,y = mouse_movements.relative_move('down')
    mouse_movements.move_mouse(rx+x, ry+y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(8.00, 8.35))
    print('done')


while True:

    mouse_movements.move_mouse(rx+730, ry+502, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(40.00, 45.00))

    for x in range(50): #while screenscrape.read_text("inventory is too full") == False:
        print ( x, ' iteration')
        mouse_movements.move_mouse(rx+695, ry+502, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(40.00, 45.00))
        if screenscrape.read_text("inventory is too full"):
            break

        mouse_movements.move_mouse(rx+765, ry+502, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(40.00, 45.00))
        if screenscrape.read_text("inventory is too full"):
            break


    bank_items()
