from Core_scripts.screen_scraping import *
from Core_scripts.movements import *
import time
#from max zoom out
mouse_movements = mouse_movements()
def check_fall():

    print('checking for fall')
    x,y = mouse_movements.relative_move()
    center_x, center_y = mouse_movements.get_center()
    #gap fall
    if abs(center_x-x) >= 400 and center_y - y <= 0:

        print('player has fallen off gap')
        x,y = mouse_movements.relative_move('down')
        print(x, y)
        mouse_movements.move_mouse(x, y +250, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(7.00, 7.50))
        return True
    #tightrope fall
    elif abs(center_x-x) >= 400 and center_y - y >= 0:

        print('player has fallen off tightrope')
        x,y = mouse_movements.relative_move('up', 400, 0)
        print(x, y)
        mouse_movements.move_mouse(x, y +250, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(7.00, 7.50))
        return True
    
    else:
        return False

for _ in range(300):
    reset_loop  = False
    while True:
        print('moving up')
        try:
            x,y = mouse_movements.relative_move('up', 0, 0)
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(random.uniform(10.40, 10.60))

        if check_fall() == True:
            reset_loop = True
            break

    #fail check
    if reset_loop == True:
        continue

    #tightropes
    counter = 0
    while True:
        try:
            print('moving down')
            x,y = mouse_movements.relative_move('down', -20, -85)
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            if counter < 2:
                time.sleep(random.uniform(10.50, 10.70))
            else:
                time.sleep(random.uniform(6.00, 6.20))
            counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        if counter < 3 and check_fall() == True:
            reset_loop = True
            break

    if reset_loop == True:
        continue
    

