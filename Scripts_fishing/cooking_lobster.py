from screen_scraping import *
from movements import *
import threading
import pyautogui 

#Minimap location for me is 125 + 155 and 30 + 155
#Inventory location for me is 1210 + 190 and 720 +260
#make sure inventory is hidden

#screenscrape.read_text('here to continue')
#screenscrape.read_text('You cant carry any more')

def fishing_contours(bool = False, y_axis = False):
    #color of teal markers in runelite
    color = [0,253,242]
    teal_markers = screenscrape.find_contours(color, 2)
    #filter out the minimap contours
    filtered_markers = [(x,y) for x,y in teal_markers if not (1245 <= x <= 1400 and 30 <= y <= 185)]
    #Sort by x coordinates, else y coordinates
    if y_axis == False:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = bool)
    else:
        filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = bool)

    for x,y in filtered_markers:
        print(x,' ', y)
    return filtered_markers[0]

def fishing_area(bool = False):
    fish_spots = screenscrape.img_detection('osrs_lobster.png', .60)
    filtered_spots = sorted(fish_spots, key= lambda x: x[0], reverse = bool)
    print(filtered_spots)
    image = Image.open('osrs_lobster.png')
    width, height = image.size[0] // 2, image.size[1] // 2
    #make a new array, tuples are immutable 
    new_array = []
    for x,y in filtered_spots:
        new_spots = (x + width, y +height)
        new_array.append(new_spots)
    return new_array

#not that this cooking function requires compass orientation to the north.
def cooking():
    while screenscrape.read_text('You havent got anything to cook') == False:
        x,y = fishing_contours(False, True)
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(8)
        pyautogui.press('1')
        counter = 0
        while screenscrape.read_text('here to continue') == False and counter < 4:
            print('cooking')
            time.sleep(10)
            counter += 1
    return
        
###START###
for _ in range(50):
    while screenscrape.read_text('You cant carry any more') == False:
        x,y = fishing_contours(True)
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(5.90 ,6.20))
        x,y = fishing_area(True)[0]
        mouse_movements.move_mouse(x, y, 2)
        mouse_movements.perform_click()
        time.sleep(random.uniform(24.50, 25.10))
        while screenscrape.skill_text():
            print('Fishing')
            time.sleep(10)


    x,y = fishing_contours(True)
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.80, 10.10))

    x,y = fishing_contours()
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.50, 9.90))

    cooking()
    time.sleep(random.uniform(2.90, 3.10))

    x,y = fishing_contours()
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(7.00, 7.20))

    image1 = Image.open('cooked_lobster.png')
    width1, height1 = image1.size[0] // 2, image1.size[1] // 2
    x,y = screenscrape.img_detection('cooked_lobster.png', .90)[0]
    mouse_movements.move_mouse(x+width1, y+height1, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.80, 10.1))

    try:
        image2 = Image.open('burnt_lobster.png')
        width2, height2 = image2.size[0] // 2, image2.size[1] // 2
        x,y = screenscrape.img_detection('burnt_lobster.png', .90)[0]
        mouse_movements.move_mouse(x+width2, y+height2, 2)
        mouse_movements.perform_click()
        time.sleep(2)
    except:
        print("no burnt food!")
        pass

    x,y = fishing_contours(True)
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.90, 5.10))

    x,y = fishing_contours(True)
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(4.90, 5.10))

    x,y = fishing_contours(True)
    mouse_movements.move_mouse(x, y, 2)
    mouse_movements.perform_click()
    time.sleep(random.uniform(5.30, 5.40))

    




