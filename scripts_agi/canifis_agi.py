from screen_scraping import *
from movements import *
import time

mouse_movements = mouse_movements()

for _ in range(300):
    time.sleep(random.uniform(1, 1.50))
    reset_loop  = False
    #tree
    print('Beginning climing up tree')
    x,y = mouse_movements.relative_move('up')
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.10, 7.30))
    #until 2nd building
    while True:
        print('moving up')
        try:
            x,y = mouse_movements.relative_move('up', 0, -10)
            print(x, y)
            mouse_movements.move_mouse(x, y+7, 2)
            mouse_movements.perform_click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(4.50, 4.60))
    
    #until general store
    while True:
        print('moving left')
        try:
            x,y = mouse_movements.relative_move('left', -30,0)
            print(x, y)
            mouse_movements.move_mouse(x, y+7, 2)
            mouse_movements.perform_click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        time.sleep(random.uniform(7.80, 8.10))

    #fail check, when falling off there shouldnt be a marker to the left anymore
    print('checking for fall')
    x,y = mouse_movements.relative_move()
    center_x, center_y = mouse_movements.get_center()
    if abs(center_x-x) >= 200 and abs(center_y-y) >= 200:
        print('player has fallen off')
        reset_loop = True

    #fail action     
    if reset_loop == True:
        for _ in range(2):
            try:
                print('moving right')
                x,y = mouse_movements.relative_move('right', 200, 0)
                print(x, y)
                mouse_movements.move_mouse(x+40, y+10, 2)
                mouse_movements.perform_click()
            except Exception as e:
                print(f"An error occurred: {e}")
                break
            time.sleep(random.uniform(8.40, 8.60))
        time.sleep(random.uniform(3.40, 3.60))
        continue

    #Until line
    while True:
        try:
            print('moving down')
            x,y = mouse_movements.relative_move('down')
            print(x, y)
            mouse_movements.move_mouse(x, y+7, 2)
            mouse_movements.perform_click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(6.30, 6.40))

    #until final building
    while True:
        try:
            print('running acroos building')
            x,y = mouse_movements.relative_move('right', 40)
            print(x, y)
            mouse_movements.move_mouse(x, y+7, 2)
            mouse_movements.perform_click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(11.00, 11.20))

    #course finished
    print('Finishing course')
    x,y = mouse_movements.relative_move('up')
    print(x, y)
    mouse_movements.move_mouse(x, y-25, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(6.30, 6.50))

