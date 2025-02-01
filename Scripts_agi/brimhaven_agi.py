from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import math
import mss
from ultralytics import YOLO
import time

mouse_movements = mouse_movements()

def movement_order(ticket_location):
    directions = []
    #1st row
    if ticket_location == (1,1):
        directions = ['up', 'left', 'up', 'left']
    elif ticket_location == (2,1):
        directions = ['up', 'left', 'up']
    elif ticket_location == (3,1):
        directions = ['up', 'up']
    elif ticket_location == (4,1):
        directions = ['right', 'up', 'up']

    #2nd row
    if ticket_location == (1,2):
        directions = ['up', 'left', 'left']
    elif ticket_location == (2,2):
        directions = ['up', 'left']
    elif ticket_location == (3,2):
        directions = ['up']
    elif ticket_location == (4,2):
        directions = ['right', 'up']
    elif ticket_location == (5,2):
        directions = ['right', 'up', 'right']

    #3rd row
    if ticket_location == (1,3):
        #directions = ['left', 'left']
        directions = ['stay']
    elif ticket_location == (2,3):
        directions = ['left']
    elif ticket_location == (3,3):
        directions = ['stay']
    elif ticket_location == (4,3):
        directions = ['right']
    elif ticket_location == (5,3):
        directions = ['right', 'right']

    #4th row
    if ticket_location == (1,4):
        #directions = ['left', 'left', 'down']
        directions = ['stay']
        
    elif ticket_location == (2,4):
        #directions = ['down', 'left']
        directions = ['stay']
    elif ticket_location == (3,4):
        directions = ['down']
    elif ticket_location == (4,4):
        directions = ['down','right']
    elif ticket_location == (5,4):
        directions = ['down','right', 'right']

    #5th row
    if ticket_location == (1,5):
        directions = ['down', 'left', 'down', 'left']
        #directions = ['stay']
    elif ticket_location == (2,5):
        directions = ['down', 'left', 'down']
        #directions = ['stay']
    elif ticket_location == (3,5):
        directions = ['down', 'left', 'down', 'right']
        #directions = ['stay']
    elif ticket_location == (4,5):
        directions = ['down', 'right', 'down']
    elif ticket_location == (5,5):
        directions = ['down','right', 'right', 'down']

    return directions

#screenshot of minimap
def screenshot_minimap():

    window_title = 'RuneLite - litlGenocide'
    window = gw.getWindowsWithTitle(window_title)[0]

    if not window:
        print(f"No window found with title '{window_title}'")
        exit()

    x, y, width, height = window.left, window.top, window.width, window.height

    #in osrs client this is the location to get the screen shot.
    screenshot = pyautogui.screenshot(region=(x+1305, y+50, width-1360, height-1000))
    #convert into np and resize it into even dimensions
    frame = np.array(screenshot)
    resized_frame = cv2.resize(frame, (128, 128))

    #get height and width of frames and draw lines and grids to sections off each section
    height, width = resized_frame.shape[:2]
    for x in range(0, width, 23):
        cv2.line(resized_frame, (x,0), (x, height), color = (255,255,255), thickness = 1)
    for y in range(0, height, 25):
        cv2.line(resized_frame, (0,y), (width, y), color = (255,255,255), thickness = 1)

    # # Display the resized frame
    # cv2.imshow('Resized Frame', resized_frame)

    # # Wait for a key press and close the window
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #Start to find yellow arrow
    lower_color = np.array([245, 245, 50])  # Lower bound (H, S, V)
    upper_color = np.array([255, 255, 110])  # Upper bound (H, S, V)

    # Create a mask for the desired color range
    mask = cv2.inRange(resized_frame, lower_color, upper_color)

    # cv2.imshow("Mask", mask)
    # cv2.waitKey(0)  # Wait for a key press to close the window
    # cv2.destroyAllWindows()

    # Find the coordinates of non-zero pixels in the mask
    coordinates = cv2.findNonZero(mask)

    if coordinates is not None:
        # Calculate the average x and y coordinates
        avg_x = int(np.mean(coordinates[:, 0, 0]))
        avg_y = int(np.mean(coordinates[:, 0, 1]))
        #get the x and y coords, divided by the grid dimensions rounded up to find area.
        return (math.ceil(avg_x/ 23), math.ceil(avg_y/ 25))
    else:
        return None

def dispenser_YOLO():

    window_title = 'RuneLite - litlGenocide'
    window = gw.getWindowsWithTitle(window_title)[0]

    if not window:
        print(f"No window found with title '{window_title}'")
        exit()

    client_dimensions = window.left, window.top, window.width, window.height

    dispenser_list = []

    with mss.mss() as sct:
        # Capture screen using mss    
        image = np.array(sct.grab(client_dimensions))

        # Convert to GpuMat and perform preprocessing using OpenCL
        gpu_image = cv2.UMat(image) # Use UMat for OpenCL processing
        gray_gpu_image = cv2.cvtColor(gpu_image, cv2.COLOR_BGR2GRAY)
        gray_image = gray_gpu_image.get()

        #resize image for faster processing
        original_height, original_width = image.shape[:2]
        #new_width and new height also used to find the closest tuple 
        new_width = int(original_width * 0.5)
        new_height = int(original_height * 0.5)
        resized_image = cv2.resize(gray_image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        #Apply adaptive histogram equalization for better contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced_image = clahe.apply(resized_image)
        enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_GRAY2BGR)
        
        # cv2.imshow("Game", enhanced_image)
        # cv2.waitKey(0)
        model = YOLO("C:\\Users\\Steven\\Runescape\\best_98.pt")
        results = model(enhanced_image)
        for box in results[0].boxes:
            conf = box.conf[0]  # Confidence score
            if conf >= 0.60:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

                # Translate coordinates back to the original image (by scaling them)
                original_x1, original_y1 = x1 * 2, y1 * 2
                original_x2, original_y2 = x2 * 2, y2 * 2
                # Calculate the center of the bounding box
                center_x = int((original_x1 + original_x2) / 2)
                #lower the center point by 15 pixels becasue of the camera angle.
                center_y = int((original_y1 + original_y2) / 2)+15

                dispenser_list.append((center_x, center_y))
        #         cv2.circle(image, (center_x, center_y+15), radius=3, color=(0, 255, 0), thickness=-1)

        #         label = box.cls[0]  # Class ID
        #         cv2.putText(enhanced_image, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # cv2.imshow("Detections", image)
        # cv2.waitKey(0)

        closest_dispenser = None
        min_difference = float(4000)
        for dispenser in dispenser_list:
            #-17 to offset the runlite bar on the right
            difference = ((dispenser[0] - new_width - 17) ** 2 + (dispenser[1] - new_height) ** 2) ** 0.5

            if difference < min_difference:
                min_difference = difference
                closest_dispenser = dispenser
        print(dispenser_list)
        print(f"The closest dispenser is: {closest_dispenser}")

    return closest_dispenser

def wait_times(obstacle):
    if obstacle == 'path':
        print('crossing path')
        time.sleep(random.uniform(4.50, 4.60))
    elif obstacle == 'darts':
        print('crossing darts')
        time.sleep(random.uniform(8.20, 8.40))
    elif obstacle == 'ledge':
        print('crossing ledge')
        time.sleep(random.uniform(7.10, 7.30))
    elif obstacle == 'pillars':
        print('crossing pillars')
        time.sleep(random.uniform(6.30, 6.50))
    elif obstacle == 'log':
        print('crossing log')
        time.sleep(random.uniform(7.20, 7.40))
    elif obstacle == 'low_wall':
        print('crossing low wall')
        time.sleep(random.uniform(5.50, 5.60))
    elif obstacle == 'bal_rope':
        print('crossing rope')
        time.sleep(random.uniform(8.10, 8.20))
    elif obstacle == 'hand_hold':
        print('crossing hand_hold')
        time.sleep(random.uniform(8, 8.10))
    elif obstacle == 'swing':
        print('crossing swing')
        time.sleep(random.uniform(4.60, 4.80))
    elif obstacle == 'monkey_bars':
        print('crossing monkey bars')
        time.sleep(random.uniform(9.50, 9.60))

def fail_check(direction, number):
    window_title = 'RuneLite - litlGenocide'
    window = gw.getWindowsWithTitle(window_title)[0]

    if not window:
        print(f"No window found with title '{window_title}'")
        exit()

    left, top, width, height = window.left, window.top, window.width, window.height
    center_x = ((left + width) // 2) - 17 
    center_y = ((top + height) // 2)

    print("center coords ", center_x, center_y)

    x, y = dispenser_YOLO()

    if direction == 'up':
        if y < center_y:
            print("Pass")
            return True
        else:
            print("fail")
            return False
    elif direction == 'down':
        if y > center_y:
            print("Pass")
            return True
        else:
            print("fail")
            return False
    elif direction == 'left':
        if x < center_x:
            print("Pass")
            return True
        else:
            print("fail")
            return False
    elif direction == 'right':
        if x > center_x:
            print("Pass")
            return True
        else:
            print("fail")
            return False

def up(index, avg_coords, reverse = False, fail_counter = 0):
    x, y = dispenser_YOLO()
    print(avg_coords, index, reverse)
    if (index == 1 and avg_coords == (3,1) and reverse == False 
        or index == 0 and avg_coords == (4,5) and reverse == True):
        mouse_movements.move_mouse(x, y-100)
        mouse_movements.perform_click()
        wait_times('bal_rope')
    elif index == 1 and (avg_coords == (4,1) or avg_coords == (5,2) or avg_coords == (4,2)) and reverse == False:
        mouse_movements.move_mouse(x, y-380)
        mouse_movements.perform_click()
        wait_times('darts')
    elif (index == 2 and avg_coords == (4,1) and reverse == False) or (index == 0 and avg_coords == (5,5) and reverse == True):
        mouse_movements.move_mouse(x, y-130)
        mouse_movements.perform_click()
        wait_times('log')
    elif index == 0 and avg_coords == (1,4) and reverse == True:
        mouse_movements.move_mouse(x-142, y-132)
        mouse_movements.perform_click()
        wait_times('hand_hold')
    elif ((index == 3 and avg_coords == (1,5)) or (index == 2 and avg_coords == (2,5)) 
        or (index == 1 and avg_coords == (2,4)) or (index == 0 and avg_coords == (3,4))
        or (index == 3 and avg_coords == (3,5))
        ) and reverse == True:
        if fail_counter >= 4:
            mouse_movements.move_mouse(x, y-320)
        else:
            mouse_movements.move_mouse(x, y-280)
        mouse_movements.perform_click()
        wait_times('low_wall')
    elif ((index == 1 and avg_coords == (4,4)) or (index == 2 and avg_coords == (4,5)) 
        or (index == 2 and avg_coords == (5,4)) or (index == 3 and avg_coords == (5,5))
        ) and reverse == True:
        if fail_counter >= 4:
            mouse_movements.move_mouse(x+20, y-320)
        else:
            mouse_movements.move_mouse(x+20, y-280)
        mouse_movements.perform_click()
        wait_times('low_wall')
    else:
        mouse_movements.move_mouse(x, y-380)
        mouse_movements.perform_click()
        wait_times('path')
    #recursive fail check to call upon itself again if it fails the obstacle
    if fail_check('up', y) == False:
        fail_counter +=1
        up(index, avg_coords, reverse, fail_counter)

def down(index, avg_coords, reverse = False):
    x, y = dispenser_YOLO()
    print(index, avg_coords, reverse)

    if (index == 0 and avg_coords == (3,1) and reverse == True
        or index == 2 and avg_coords == (4,5) and reverse == False):
        mouse_movements.move_mouse(x, y+130)
        mouse_movements.perform_click()
        wait_times('bal_rope')
    elif ((index == 0 and avg_coords == (4,1) and reverse == True) 
        or (index == 3 and avg_coords == (5,5) and reverse == False)):
        mouse_movements.move_mouse(x, y+160)
        mouse_movements.perform_click()
        wait_times('log')
    elif index == 1 and (avg_coords == (4,1) or avg_coords == (5,2)) and reverse == True:
        mouse_movements.move_mouse(x, y+400)
        mouse_movements.perform_click()
        time.sleep(1.5)
        wait_times('darts')
    elif index == 0 and avg_coords == (4,2) and reverse == True:
        mouse_movements.move_mouse(x, y+400)
        mouse_movements.perform_click()
        wait_times('darts')
    elif index == 2 and avg_coords == (1,4) and reverse == False:
        mouse_movements.move_mouse(x-152, y+81)
        mouse_movements.perform_click()
        wait_times('hand_hold')
    elif index == 0 and reverse == False:
        mouse_movements.move_mouse(x, y+345)
        mouse_movements.perform_click()
        wait_times('low_wall')
    else:
        mouse_movements.move_mouse(x, y+400)
        mouse_movements.perform_click()
        wait_times('path')

    if fail_check('down', y) == False:
        down(index, avg_coords, reverse)
        
def left(index, avg_coords, reverse = False):
    x, y = dispenser_YOLO()
    print(avg_coords, index, reverse)
    if index == 3 and avg_coords == (1,1) and reverse == False:
        mouse_movements.move_mouse(x-150, y)
        mouse_movements.perform_click()
        wait_times('ledge')
    elif index == 3 and avg_coords == (1,5) and reverse == False:
        mouse_movements.move_mouse(x-180, y-17)
        mouse_movements.perform_click()
        wait_times('ledge')
    elif index == 2 and (avg_coords == (4,1) or avg_coords == (5,2)) and reverse == True:
        mouse_movements.move_mouse(x-180, y+10)
        mouse_movements.perform_click()
        wait_times('pillars')
    elif (index == 1 and avg_coords == (5,3) or avg_coords == (4,2)) or (index == 0 and avg_coords == (4,3)) and reverse == True:
        mouse_movements.move_mouse(x-180, y+10)
        mouse_movements.perform_click()
        wait_times('pillars')
    elif index == 2 and avg_coords == (1,2) and reverse == False:
        mouse_movements.move_mouse(x-160, y+6)
        mouse_movements.perform_click()
        wait_times('log')
    elif index == 1 and (avg_coords == (1,3) or avg_coords == (1,4)) and reverse == False:
        mouse_movements.move_mouse(x-350, y+25)
        mouse_movements.perform_click()
        time.sleep(1.5)
        wait_times('swing')
    elif index == 0 and (avg_coords == (1,3) or avg_coords == (1,4) or avg_coords == (2,3)) and reverse == False:
        mouse_movements.move_mouse(x-440, y)
        mouse_movements.perform_click()
        time.sleep(1)
        wait_times('darts')
    elif ((index == 0 and avg_coords == (4,4))
          or (index == 1 and avg_coords in [(4, 5), (5, 4)])
          or (index == 2 and avg_coords == (5,5))
          ) and reverse == True:
        mouse_movements.move_mouse(x-440, y)
        mouse_movements.perform_click()
        time.sleep(1)
        wait_times('darts')
    elif index == 0 and avg_coords == (3,5) and reverse == True:
        mouse_movements.move_mouse(x-115, y-8)
        mouse_movements.perform_click()
        wait_times('monkey_bars')
    else:
        mouse_movements.move_mouse(x-440, y)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4, 4.1))

    if fail_check('left', x) == False:
        left(index, avg_coords, reverse)
        
def right(index, avg_coords, reverse = False):
    x, y = dispenser_YOLO()
    print(avg_coords, index, reverse)
    if index == 0 and reverse == False:
        mouse_movements.move_mouse(x+180, y+20)
        mouse_movements.perform_click()
        wait_times('pillars')
    elif index == 0 and (avg_coords == (1,1) or avg_coords == (1,5)) and reverse == True:
        mouse_movements.move_mouse(x+165, y-10)
        mouse_movements.perform_click()
        wait_times('ledge')
    elif index == 0 and avg_coords == (1,2) and reverse == True:
        mouse_movements.move_mouse(x+155, y+5)
        mouse_movements.perform_click()
        wait_times('log')
    elif ((index == 0 and avg_coords == (1, 3)) or (index == 1 and avg_coords == (1, 4))
          ) and reverse == True:
        mouse_movements.move_mouse(x+300, y-60)
        mouse_movements.perform_click()
        wait_times('swing')
    elif ((index == 1 and avg_coords == (1,3)) or (index == 2 and avg_coords == (1,4)) 
        or (index == 0 and avg_coords == (2,3))) and reverse == True:
        mouse_movements.move_mouse(x+440, y)
        mouse_movements.perform_click()
        time.sleep(1.5)
        wait_times('darts')
    elif (index == 1 and avg_coords == (4,4) or avg_coords == (4,5) or avg_coords == (5,4) or avg_coords == (5,5)
          )and reverse == False:
        mouse_movements.move_mouse(x+440, y)
        mouse_movements.perform_click()
        wait_times('darts')
    elif index == 3 and avg_coords == (3,5) and reverse == False:
        mouse_movements.move_mouse(x+125, y-60)
        mouse_movements.perform_click()
        wait_times('monkey_bars')
    else:
        mouse_movements.move_mouse(x+440, y)
        mouse_movements.perform_click()
        #edge case for very bottom 
        if (index == 2 and avg_coords == (5,5) and reverse == False):
            time.sleep(2)
        wait_times('path')

    if fail_check('right', x) == False:
        right(index, avg_coords, reverse)

def recursive_move(index, direction, window_title = 'RuneLite - litlGenocide'):
    #get the the client coords 
    window = gw.getWindowsWithTitle(window_title)[0]
    if not window:
        print(f"No window found with title '{window_title}'")
        exit()
    rx, ry, width, height = window.left, window.top, window.width, window.height

    if (index == 0 and direction == 'up'):
        mouse_movements.move_mouse(rx+680, ry+220)
        mouse_movements.perform_click()
        #failcheck

    pass

if __name__ == '__main__':
    print('starting')
    current_coords = ()
    for _ in range(355):
        # Find the average coordinates of yellow arrow
        avg_coords = screenshot_minimap()
        while (avg_coords is None or avg_coords == current_coords):
            avg_coords = screenshot_minimap()
            if avg_coords == current_coords:
                #if coordinates are the same prevents constant spamming
                time.sleep(2)
        print( "Ticket is at: ", avg_coords[0], avg_coords[1])
        current_coords = avg_coords
        #avg_coords = (3,4)
        #change to avg_coords reminder
        directions = movement_order(avg_coords)
        print(directions)
        #get reverse directions
        reverse_dict = {'up' : 'down', 'down' : 'up', 'left' : 'right', 'right' : 'left', 'stay' : 'stay'}
        reverse_directions = []
        for i in reversed(directions):
            reverse_directions.append(reverse_dict[i])

        print(reverse_directions)
        
        for index, action in enumerate(directions):
            print('Moving ', avg_coords, index, action)

            if action == 'up': 
                up(index, avg_coords)
            elif action == 'down': 
                down(index, avg_coords)
            elif action == 'left': 
                left(index, avg_coords)
            elif action == 'right': 
                right(index, avg_coords)
            elif action == 'stay': 
                pass
        
        #click on the dispenser
        x, y = dispenser_YOLO()
        mouse_movements.move_mouse(x, y)
        mouse_movements.perform_click()
        mouse_movements.move_mouse(400, 400)
        time.sleep(random.uniform(1.9, 2.1))

        for index, action in enumerate(reverse_directions):
            print('Moving back', index, ' ', action)

            if action == 'up': 
                up(index, avg_coords, reverse=True)
            elif action == 'down': 
                down(index, avg_coords, reverse=True)
            elif action == 'left': 
                left(index, avg_coords, reverse=True)
            elif action == 'right': 
                right(index, avg_coords, reverse=True)
            elif action == 'stay': 
                pass
        
        x, y = dispenser_YOLO()
        mouse_movements.move_mouse(x+70, y)
        mouse_movements.perform_click()
        time.sleep(random.uniform(3.30, 3.40))

        



