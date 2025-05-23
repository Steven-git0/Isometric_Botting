#Copper Mining Varrock Eastside, orientation North, 1400x 1000, zoom out max, then zoom in 3 mousewheels
import pyautogui 
import time
import numpy as np
import random
from core_scripts.screen_scraping import *
from humancursor import SystemCursor
import pygetwindow as gw
cursor = SystemCursor()

#Time to mine, adjust depending on your pickaxe and mining level (lower if better pick axe)

class mouse_movements():

    def __init__(self, window_title): 
        self.screenscrape = screenscrape(window_title)
        window = gw.getWindowsWithTitle(window_title)[0]
        if not window:
            print(f"No window found with title '{window_title}'")
            exit()
        self.rx, self.ry, self.width, self.height = window.left, window.top, window.width, window.height

    def perform_click(self, m = 'l'):
        if m == 'r':
            print('clicking')
            pyautogui.mouseDown(pyautogui.position(), button='right')
            time.sleep(random.uniform(.10, .20))
            pyautogui.mouseUp(pyautogui.position(), button='right')
        else:
            print('clicking')
            pyautogui.mouseDown(pyautogui.position())
            time.sleep(random.uniform(.10, .20))
            pyautogui.mouseUp(pyautogui.position())
            

    def move_mouse(self, end_x, end_y, variance = 2):
        
        if end_x <= 1 and end_y <= 1:
            end_x = self.rx + (self.width*end_x) + random.uniform(-variance, variance)
            end_y = self.ry + (self.height*end_y) + random.uniform(-variance, variance)
        else:
            end_x += random.uniform(-variance, variance) 
            end_y += random.uniform(-variance, variance)
        attempts = 0
        while attempts < 5:
            try:
                print('move to ', end_x, end_y)
                cursor.move_to([end_x, end_y], duration = 0.01)
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("1 attempt failed, rounding to whole")
                end_x = round(end_x)
                end_y = round(end_y)

        if attempts == 5:
             print("Max retries reached, operation failed.")

        #cursor.click_on([end_x, end_y])

    def click_image(self, img_name, element = 0, threshold = .90):
        image = Image.open(img_name)
        width, height = image.size[0] // 2, image.size[1] // 2
        try:
            x,y = self.screenscrape.img_detection(img_name, threshold)[element]
            mouse_movements.move_mouse(x+width, y+height, 2)
            mouse_movements.perform_click()
        except:
            return False
    
    def move_contours(self, x_axis = True, right2left = False, color = [50,0,73]):
        #color of teal markers in runelite is [0,253,242]
        #right to left is descending order as coords is 0, 0 at the top left
        #find the teal contours
        markers = self.screenscrape.find_contours(target_color = color)
        #filter out the minimap contours
        filtered_markers = [(x,y) for x,y in markers if not (self.width-215 <= x <= self.width 
                                                             and 0 <= y <= 200)]
        #Sort by x coordinates, else y coordinates
        if x_axis == True:
            filtered_markers = sorted(filtered_markers, key= lambda x: x[0], reverse = right2left)
        else:
            filtered_markers = sorted(filtered_markers, key= lambda x: x[1], reverse = right2left)

        for x,y in filtered_markers:
            print(x, y)
        return filtered_markers
    
    def relative_move(self, direction = None, offset = 60):

        center_x, center_y = self.get_center()
        filtered_markers = self.move_contours()
        coordinates = filtered_markers
        #filter out a direction you dont want the player to go
        if direction == 'up':
            #remember top left is 0, 0 higher y is the lower it is. -80 to shift the cenmtre point as to not include center 
            filtered_markers = [(x,y) for x, y in coordinates if y <= center_y-offset]
            print("moving up")
        elif direction == 'down':
            filtered_markers = [(x,y) for x, y in coordinates if y >= center_y+offset]
            print("moving down")
        elif direction == 'right':
            filtered_markers = [(x,y) for x, y in coordinates if x >= center_x+offset]
            print("moving right")
        elif direction == 'left':
            filtered_markers = [(x,y) for x, y in coordinates if x <= center_x-offset]
            print("moving left")
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
        print(min_index)

        return filtered_markers[min_index]

    def get_center(self):
        # Calculate the center of the window
        #-17 is specific the the runelite client to compensate for the bar on the right.
        center_x = (self.width // 2) - 17
        center_y = (self.height // 2) + 20

        print(f"center at ({center_x}, {center_y})")

        return center_x, center_y
    
    def get_minimap(self):

        window_top = self.ry
        window_width = self.width

        #osrs minimap size does not change and is always x-260 and y+ 230 fromt he top right corner
        return window_width - 260, window_width, window_top, window_top + 230
    
    def login(self):
        
        mouse_movements.move_mouse(self, self.rx+self.width+17, self.ry + 38)
        mouse_movements.perform_click(self)
        mouse_movements.move_mouse(self, self.rx+ self.width - 63, self.ry + self.height - 30, 4)
        mouse_movements.perform_click(self)
        time.sleep(random.uniform(.80, 1.50))
        mouse_movements.move_mouse(self, self.rx + (self.width/2) + 65, self.ry + 290, 5)
        mouse_movements.perform_click(self)
        time.sleep(random.uniform(7.00, 9.00))   
        mouse_movements.move_mouse(self, self.rx+ (self.width/2) + 65, self.ry + 365, 5) 
        mouse_movements.perform_click(self)
    
    def random_movements(self):
        pass