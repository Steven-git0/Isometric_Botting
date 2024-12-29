from screen_scraping import *
from movements import *
import threading
import pyautogui 
import time
import sys

#order from left to right(small to large), sort by x axis
def move_contours(x_axis = True, right2left = False):
    #color of teal markers in runelite
    color = [0,253,242]
    #find the teal contours
    teal_markers = screenscrape.find_contours(color, 2)
    #filter out the minimap contours
    filtered_markers = [(x,y) for x,y in teal_markers if not (1245 <= x <= 1400 and 30 <= y <= 185)]
    #Sort by x coordinates, else y coordinates
    if x_axis == True:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
        filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
    else:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)
        filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)

    for x,y in filtered_markers:
        print(x,' ', y)
    return filtered_markers

def checking_and_healing(threshold = 9):
    while screenscrape.check_health(threshold) == True:
        print('Need to heal')
        image1 = Image.open('cooked_lobster.png')
        width1, height1 = image1.size[0] // 2, image1.size[1] // 2
        try:
            x,y = screenscrape.img_detection('cooked_lobster.png', .90)[-1]
            mouse_movements.move_mouse(x + width1, y + height1, 2)
            mouse_movements.perform_click()
            time.sleep(1)
        except:
            print('No Food')
            break
        

def main_function():
    x,y = move_contours()[1]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.40, 4.60))

    while len(screenscrape.img_detection('bruma_root.png', x1 = 1210, y1 = 725, x2 = 180, y2 = 255)) < 20:

        if screenscrape.skill_text('wintertodt_sw') == False:
            x,y = move_contours()[1]
            mouse_movements.move_mouse(x, y, 2)
            mouse_movements.perform_click()
            time.sleep(2)
            print('going to chop wood')
        else:
            print('still chopping wood')

        time.sleep(2)
    
    while len(screenscrape.img_detection('bruma_kindling.png', x1 = 1210, y1 = 725, x2 = 180, y2 = 255)) < 20:
        checking_and_healing()

        if mouse_movements.click_image('bruma_root.png', element=-1) == False:
            break
        
        mouse_movements.click_image('osrs_knife.png')
        
        print('Fletching')
        time.sleep(1)
        while screenscrape.skill_text('wintertodt_sw') == True:
            time.sleep(random.uniform(1.00, 1.20))

    print('going to brazier')

    x,y = move_contours()[0]
    mouse_movements.move_mouse(x + 50, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.50, 3.60))


    while screenscrape.skill_text('wintertodt_nw') == False:
        checking_and_healing()
        x,y = move_contours()[0]
        mouse_movements.move_mouse(x, y, 2)

        if screenscrape.skill_text('wintertodt_sw') == False:
            print('feeding fire')
            mouse_movements.perform_click()

        time.sleep(random.uniform(1.00, 1.10))

    print('All done')

    x,y = move_contours(x_axis= False)[-1]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.50, 3.60))

    checking_and_healing(threshold = 4)
    time.sleep(random.uniform(2.90, 3.10))

    x,y = move_contours()[-1]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.00, 5.20))

    while True:
        try:
            if screenscrape.img_detection('supply_crate.png', .90):
                break     
        except:
            print(f"finding")
            time.sleep(4)
    
    
    x,y = move_contours()[3]
    mouse_movements.move_mouse(1000, 500, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.50, 3.70))

    x,y = move_contours(x_axis=False)[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.50, 7.60))

    #check if player clicked on the bank

    while not screenscrape.img_detection('bank_osrs.png'):
        print('no bank')
        x,y = move_contours()[1]
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(4)
        
    
    mouse_movements.click_image('supply_crate.png')
    
    if screenscrape.img_detection('cooked_lobster.png', x1 = 1210, y1 = 725, x2 = 180, y2 = 255):
        mouse_movements.click_image('cooked_lobster.png', element = -1)
        time.sleep(random.uniform(1.00, 1.20))
    

    mouse_movements.move_mouse(470, 135, 2)
    mouse_movements.perform_click(m = 'r')

    x,y = pyautogui.position()
    mouse_movements.move_mouse(x - 20, y + 53, 0)
    mouse_movements.perform_click()

    x,y = move_contours(x_axis=False)[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.50, 4.60))

    x,y = move_contours()[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.00, 5.20))

    x,y = move_contours()[0]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.00, 5.20))

    x,y = move_contours()[2]
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.00, 3.20))

    if screenscrape.img_detection('cooked_lobster.png') is not None:
        pass
    else:
        print('no food found, terminate')
        return False

    while screenscrape.skill_text('wintertodt_bar') == False:
        time.sleep(3)
    
    print('Finish')

    
# main_thread = threading.Thread(target = main_function)
# main_thread.start()
# main_thread.join()

for _ in range(80):
    if main_function() == False:
        break
