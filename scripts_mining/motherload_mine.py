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
screenscrape = screenscrape()
#4 for regular, 7 for large
sack_size = 7
#screenshot = pyautogui.screenshot(region=(width-235, height-310, 235, 310))
#screenshot.show()

while True:
    #The bag can hold 4 runs
    for i in range(sack_size):
        #start from the left
        x,y = mouse_movements.relative_move("left", offset = 130)
        mouse_movements.move_mouse(rx+x, ry+y-40, 4)
        mouse_movements.perform_click()
        time.sleep(random.uniform(7.60, 8.00))
        
        while screenscrape.read_text("full") == False:
            #find the coordinates of the contour 
            contour_x, contour_y = mouse_movements.relative_move()

            #find the pickaxe picture closest to the contour
            pickaxe_coords = screenscrape.img_detection(input_img="osrs_images\OSRS_mining.png", threshold= .60)
            pickaxe_coords = sorted(pickaxe_coords, key = lambda p: ((p[0]-contour_x)**2 + (p[1]-contour_y)**2)**.5)
            x,y = pickaxe_coords[0]
            mouse_movements.move_mouse(rx+x, ry+y, 3)
            mouse_movements.perform_click()
            time.sleep(random.uniform(3.00, 3.40))

            #find the pickaxe picture closest to the center
            center_x, center_y = mouse_movements.get_center()
            pickaxe_coords = screenscrape.img_detection(input_img="osrs_images\OSRS_mining.png", threshold= .60)
            pickaxe_coords = sorted(pickaxe_coords, key = lambda p: ((p[0]-center_x)**2 + (p[1]-center_y)**2)**.5)
            #overwrite the previous corrdinates as they are not needed anymore
            x,y = pickaxe_coords[0]
            print("before loop: ", x, " ", y)
            time.sleep(1.00)
            
            for _ in range(6):
                pickaxe_coords = screenscrape.img_detection(input_img="osrs_images\OSRS_mining.png", threshold= .60)
                pickaxe_coords = sorted(pickaxe_coords, key = lambda p: ((p[0]-center_x)**2 + (p[1]-center_y)**2)**.5)
                check_x, check_y = pickaxe_coords[0]
                print("Now: ", check_x, " ", check_y)
                distance = ((check_x-x)**2 + (check_y-y)**2)**.5
                print("distance: ", distance)
                if distance > 5 or screenscrape.read_text("full") == True :
                     break
                time.sleep(random.uniform(5.30, 5.80))


            if random.uniform(0.00, 100.00) <= 0.50:
                print('taking quick break')
                time.sleep(random.uniform(60.00, 600.00))

        hammer_coords = screenscrape.img_detection(input_img="osrs_images\osrs_hammer.png", threshold= .60)
        if hammer_coords:
            x,y = hammer_coords[0]
            mouse_movements.move_mouse(rx+x+5, ry+y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(10.10, 12.60))

            x,y = mouse_movements.relative_move("right")
            mouse_movements.move_mouse(rx+x, ry+y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(7.00, 7.50))

        else:   
            x,y = mouse_movements.relative_move("right", offset = 150)
            mouse_movements.move_mouse(rx+x, ry+y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(9.90, 12.40))
        
        
    mouse_movements.move_mouse(rx+690, ry+820, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(.25, .40))
    mouse_movements.move_mouse(rx+618, ry+667, 3)
    time.sleep(random.uniform(3.90, 4.20))
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.00, 3.50))

    for i in range(sack_size):

        mouse_movements.move_mouse(rx+926, ry+380, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.80, 5.35))


        #click bank icon
        deposit_inv = screenscrape.img_detection(input_img="osrs_images\deposit.png", threshold= .60)
        x, y = deposit_inv[0]
        mouse_movements.move_mouse(rx+x, ry+y, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(.50, 1.00))

        if i == sack_size-1:
            break

        mouse_movements.move_mouse(.23295, .66967, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.80, 5.35))
    
    if random.uniform(0, 100) <= 1:
                print('taking quick break')
                time.sleep(random.uniform(10, 300.00))

    mouse_movements.move_mouse(.2037, .2732, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.90, 11.50))
