#Copper Mining Varrock Eastside, orientation North, 1400x 1000, zoom out max, then zoom in 3 mousewheels
import pyautogui 
import time
import numpy as np
import random
from Core_scripts.screen_scraping import *
from humancursor import SystemCursor
import pygetwindow as gw
import Core_scripts.screen_scraping as screen_scraping
cursor = SystemCursor()

#Time to mine, adjust depending on your pickaxe and mining level (lower if better pick axe)

class mouse_movements():
    def perform_click(self, m = 'l'):
        if m == 'r':
            print('clicking')
            pyautogui.mouseDown(pyautogui.position(), button='right')
            time.sleep(random.uniform(.08, .10))
            pyautogui.mouseUp(pyautogui.position(), button='right')
        else:
            print('clicking')
            pyautogui.mouseDown(pyautogui.position())
            time.sleep(random.uniform(.08, .10))
            pyautogui.mouseUp(pyautogui.position())
            

    def move_mouse(self, end_x, end_y, variance):
        
        end_x += random.uniform(-variance, variance) 
        end_y += random.uniform(-variance, variance)
        attempts = 0
        while attempts < 5:
            try:
                print('move to ', end_x, end_y)
                cursor.move_to([end_x, end_y], duration = random.uniform(.04, .06))
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                attempts += 1
        if attempts == 5:
             print("Max retries reached, operation failed.")

        #cursor.click_on([end_x, end_y])

    def click_image(self, img_name, element = 0, threshold = .90):
        image = Image.open(img_name)
        width, height = image.size[0] // 2, image.size[1] // 2
        try:
            x,y = screenscrape.img_detection(img_name, threshold)[element]
            mouse_movements.move_mouse(x+width, y+height, 2)
            mouse_movements.perform_click()
        except:
            return False
    
    def move_contours(self, x_axis = True, right2left = False, color = [5,195,195]):
        #color of teal markers in runelite is [0,253,242]
        #right to left is descending order as coords is 0, 0 at the top left
        #find the teal contours
        teal_markers = screenscrape.find_contours(color, color_t1 = 5, color_t2 = 60, color_t3 = 60)
        #filter out the minimap contours
        x_low, x_high, y_low, y_high = self.get_minimap()
        filtered_markers = [(x,y) for x,y in teal_markers if not (x_low <= x <= x_high and y_low <= y <= y_high)]
        #Sort by x coordinates, else y coordinates
        if x_axis == True:
            filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
        else:
            filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)

        for x,y in filtered_markers:
            print(x, y)
        return filtered_markers
    
    def relative_move(self, direction = None, x_offset = 0, y_offset = 0):
        center = self.get_center()
        center_x, center_y = center
        filtered_markers = self.move_contours()
        coordinates = filtered_markers
        center_x += x_offset
        center_y += y_offset
        #filter out a direction you dont want the player to go
        if direction == 'up':
            #remember top left is 0, 0 higher y is the lower it is.
            filtered_markers = [(x,y) for x, y in coordinates if y <= center_y]
        elif direction == 'down':
            filtered_markers = [(x,y) for x, y in coordinates if y >= center_y]
        elif direction == 'right':
            filtered_markers = [(x,y) for x, y in coordinates if x >= center_x]
        elif direction == 'left':
            filtered_markers = [(x,y) for x, y in coordinates if x <= center_x]
        else:
            print('no direction specified, moving to closest marker')

        sum_list = []
        #for every marker it finds it deducts the centre coords to find the lowest value
        #the lowest value will be the closest coordinate
        for x,y in filtered_markers:
            #the center + offset allows you change the effective center if you want another coord
            sum_list.append(abs(x - (center_x)) + abs(y- (center_y)))

        #get the index of the lowest value in the sum list
        min_index = sum_list.index(min(sum_list))

        return filtered_markers[min_index]
    
    def get_center(self, window_title = 'RuneLite - litlGenocide'):
        
        # Get the window object
        windows = gw.getWindowsWithTitle(window_title)
        if not windows:
            print(f"No window found with title '{window_title}'")
            exit()

        window = windows[0]  # Select the first matching window

        # Get window dimensions
        window_left = window.left
        window_top = window.top
        window_width = window.width
        window_height = window.height

        # Calculate the center of the window
        #-17 is specific the the runelite client to compensate for the bar on the right.
        center_x = (window_left + window_width // 2) - 17
        center_y = window_top + window_height // 2

        print(f"center at ({center_x}, {center_y})")

        return center_x, center_y
    
    def get_minimap(self, window_title = 'RuneLite - litlGenocide'):

        # Get the window object
        windows = gw.getWindowsWithTitle(window_title)
        if not windows:
            print(f"No window found with title '{window_title}'")
            exit()

        window = windows[0]  # Select the first matching window

        # Get window dimensions
        window_left = window.left
        window_top = window.top
        window_width = window.width
        window_height = window.height

        #osrs minimap size does not change and is always x-260 and y+ 230 fromt he top right corner
        return window_width - 260, window_width, window_top, window_top + 230