from Core_scripts.screen_scraping import *
from movements import *
import time

mouse_movements = mouse_movements()
reset_loop  = False

for _ in range(300):

    counter = 0
    while True:
        print('moving right')
        try:
            x,y = mouse_movements.relative_move('right', 20, 0)
            print('moving right')
            mouse_movements.move_mouse(x+5, y, 2)
            mouse_movements.perform_click()
            counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(8.50, 8.70))


    time.sleep(random.uniform(7, 8))
    reset_loop = False
    #fail check, when falling off there shouldnt be a marker to the left anymore
    print('checking for fall')
    x,y = mouse_movements.relative_move()
    center_x, center_y = mouse_movements.get_center()
    if abs(center_x-x) >= 400 and abs(center_y-y) <= 150:
        print('player has fallen off')
        reset_loop = True

    #fail action     
    if reset_loop == True:
        
        print('moving right')
        x,y = mouse_movements.relative_move('left', 200, -100)
        print(x, y)
        mouse_movements.move_mouse(x, y+30, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(8.40, 8.60))

        
        print('moving down')
        x,y = mouse_movements.relative_move('down', 0, 20)
        print(x, y)
        mouse_movements.move_mouse(x-150, y+50, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(5.40, 5.60))
        continue

    counter = 0
    while True:
        print('moving up')
        try:
            x,y = mouse_movements.relative_move('up', 0, 30)
            print(x, y)
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(random.uniform(5.50, 5.70))
        if counter >= 3:
            break


    #tightropes
    counter = 0
    for _ in range(3):
        try:
            print('moving left')
            x,y = mouse_movements.relative_move('left')
            print(x, y)
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        if counter <= 1:
            time.sleep(random.uniform(10.10, 10.30))
        else:
            time.sleep(random.uniform(5.00, 5.20))

    # #until final building
    down_shift = 0
    while True:
        try:
            print('running down after tightropes')
            x,y = mouse_movements.relative_move('down',-20, down_shift)
            print(x, y)
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            down_shift = 20
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(5.00, 5.10))
