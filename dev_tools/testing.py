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


x,y = screenscrape.npz_detection('image_identification/deposit_inv.npz')[-1]
mouse_movements.move_mouse(x, y, 2)
mouse_movements.perform_click()

# if screenscrape.mouse_text() == 'calcified':
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(50.00, 60.40))

#     if random.uniform(0, 100) <= 1:
#         print('taking break')
#         time.sleep(random.uniform(300, 400))


# def move_out():
    
#     x,y = mouse_movements.relative_move('left')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.62, 6.86))
#     print('done')
#     x,y = mouse_movements.relative_move('left')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.30, 6.38))
#     print('done')
#     x,y = mouse_movements.relative_move('left')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.53, 6.89))
#     print('done')


#     x,y = mouse_movements.relative_move('right')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.60, 6.90))
#     print('done')
#     x,y = mouse_movements.relative_move('right')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.21, 6.45))
#     print('done')

#     x,y = mouse_movements.relative_move('right')
#     mouse_movements.move_mouse(rx+x, ry+y, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(6.61, 6.84))
#     print('done')

# def cooking():
#     mouse_movements.move_mouse(rx+795, ry+387, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(4.60, 4.80))
#     print('done')

#     pyautogui.press('1')
#     time.sleep(random.uniform(40.00, 40.80))

#     mouse_movements.move_mouse(rx+652, ry+788, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(4.60, 4.80))

#     mouse_movements.move_mouse(rx+809, ry+860, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(1.60, 1.80))

#     mouse_movements.move_mouse(rx+809, ry+860, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(1.60, 1.80))

#     mouse_movements.move_mouse(rx+796, ry+63, 2)
#     mouse_movements.perform_click()
#     time.sleep(random.uniform(1.60, 1.80))


# while True:
#    time.sleep(random.uniform(590, 700))
#    print("aggrotimer reached")
#    time.sleep(random.uniform(40, 60))
#    move_out()
    
