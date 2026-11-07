import pytesseract
import numpy as np
import time
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import imagehash
from sklearn.cluster import DBSCAN
import re
import sys
import os
import platform
import pywinctl as gw
import pyautogui

if platform.system() == "Windows":
    # If the user is running the .exe, we need to handle paths differently
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
else:
    # On Mac/Linux, Tesseract is usually in the global PATH
    pass

class screenscrape:

    def __init__(self, window_title): 
        # 1. Get the list of windows first
        windows = gw.getWindowsWithTitle(window_title)
        window = windows[0]
        self.rx = window.left
        self.ry = window.top
        self.width = window.width
        self.height = window.height
    
    def read_text(self, target_text):

        # Capture a region of the screen and save it as an image file
        screenshot = pyautogui.screenshot(region=(self.rx+10, self.ry + self.height - 175, 515, 140))
        #screenshot.show()
        screenshot = screenshot.resize((3678, 1000), Image.LANCZOS)
        #screenshot.show()

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(screenshot)
        screenshot = np.array(enhancer.enhance(2.0))
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_image = clahe.apply(gray_image)
        
        # Use Tesseract to perform OCR
        text = pytesseract.image_to_string(enhanced_image)

        # Check if the target text is found in the OCR result
        if target_text in text:
            print(f"Found target text: {target_text}")
            return True
        else:
            print(f"No target text: {text}")
            return False
    
    def check_health(self, target_color = np.array([230, 180, 0]), color_t1 = 25, color_t2 = 25, color_t3 = 5):

        screenshot = pyautogui.screenshot(region=(self.rx + self.width - 217, self.ry + 50, 30, 30))
        image = np.array(screenshot) 
        #set the upper and lower bounds for the color, sometimes the color may be a few units off within the contour
        lower_bound = np.array([target_color[0] - color_t1, target_color[1] - color_t2, target_color[2] - color_t3])
        upper_bound = np.array([target_color[0] + color_t1, target_color[1] + color_t2, target_color[2] + color_t3])

        # Create a 'mask', matched color are black the rest in white, for a B&W image of only where the outlines are.
        mask = cv2.inRange(image, lower_bound, upper_bound) 

        if cv2.countNonZero(mask) > 0:
            print('low health')
            return True
        else:
            print('High health')
            return False
                
    #color_check only checks if the color is above each index value
    def color_check(self, x, y, desired_color):

        if x < 1 and y < 1:
            x = self.rx + (self.width*x)
            y = self.ry + (self.height*y)

        actual_color = pyautogui.pixel(int(x),int(y))

        for i, color in enumerate(desired_color):
            print(actual_color, desired_color)
            if actual_color[i] < desired_color[i]:
                return False
        
        return True
        
    def skill_text(self, activity = ''):
        green_color = np.array([0, 255, 0])
        screenshot = None
        #Wintertodt bottom left text box
        if activity == 'wintertodt_sw':
            screenshot = pyautogui.screenshot(region=(10, 770, 130, 85))
        #Wintertodt top left text box
        elif activity == 'wintertodt_nw':
            screenshot = pyautogui.screenshot(region=(self.rx +35, self.ry+115, 40, 30))
        elif activity == 'wintertodt_bar':
            red_color = np.array([204, 0, 0])
            screenshot = pyautogui.screenshot(region=(5, 50, 15, 15))
        elif activity == 'motherload':
            screenshot = pyautogui.screenshot(region=(self.rx+10, self.ry+60, 150, 100))
        #All other skill activities textbox
        else:
            screenshot = pyautogui.screenshot(region=(self.rx+10, self.ry+20, 150, 100))
    
        image = np.array(screenshot) 
        mask = cv2.inRange(image, green_color, green_color)

        if cv2.countNonZero(mask) > 0:
            return True
        else:
            print('Idle')
            return False
        
    def mouse_text(self, target_text):
        # Capture a region of the screen and save it as an image file
        x, y = pyautogui.position()
        screenshot = pyautogui.screenshot(region=(x, y+20, 140, 25))
        screenshot = screenshot.resize((500, 100), Image.LANCZOS)

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(screenshot)
        screenshot = np.array(enhancer.enhance(2.0))
        #use cv2 to convert into black and white to make blue letters readable
        gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_image = clahe.apply(gray_image)

        # Use Tesseract to perform OCR
        text = pytesseract.image_to_string(enhanced_image)
        print(text)

        if target_text in text:
            print('found mouse text')
            return True
        else:
            print('not found mouse text')
            return False
    
    def find_contours(self, target_color = [50,0,73], color_t1 = 5, color_t2 = 5, color_t3 = 5, area_tolerance = 20):

        #in osrs client this is the location to get the screen shot.
        screenshot = pyautogui.screenshot(region=(self.rx, self.ry, self.width, self.height))
        # Convert the screenshot to a NumPy array, then convert to hsv for better contour detection
        image = np.array(screenshot) 
        #set the upper and lower bounds for the color, sometimes the color may be a few units off within the contour
        lower_bound = np.array([target_color[0] - color_t1, target_color[1] - color_t2, target_color[2] - color_t3])
        upper_bound = np.array([target_color[0] + color_t1, target_color[1] + color_t2, target_color[2] + color_t3])

        # Create a 'mask', matched color are black the rest in white, for a B&W image of only where the outlines are.
        mask = cv2.inRange(image, lower_bound, upper_bound) 
        
        # dilated = cv2.dilate(mask, kernel=np.ones((2,2), np.uint8), iterations=1)
        # cv2.imshow('Dilated Image', dilated)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        #from the mask finds the continous black lines that makes a contour
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours
        #new array to return the coordinates
        squares = []
        if contours:
            # Get the coordinates of the center of the contours
            for c in contours:
                cx = int(c[:, 0, 0].mean())
                cy = int(c[:, 0, 1].mean())
                print("Found color at coordinates:", cx, cy)
            
                squares.append((self.rx+cx,self.ry+cy))
            
             #filter out the minimap contours
            filtered_contours = [(x,y) for x,y in squares if not (self.rx+self.width-215 <= x <= self.rx+self.width 
                                                             and self.ry+0 <= y <= self.ry+200)]

        else:
            print("Color not found on the screen.")

        return filtered_contours

    def group_nearby_coordinates(self, coordinates, eps=4):
        if not coordinates:
            return []

        # Convert coordinates to numpy array
        coords_array = np.array(coordinates)

        # Apply DBSCAN clustering
        clustering = DBSCAN(eps=eps, min_samples=1).fit(coords_array)

        # Group coordinates by clusters
        clusters = {}
        for idx, label in enumerate(clustering.labels_):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(coords_array[idx])

        # Compute the average of each cluster
        averaged_coordinates = [tuple(np.mean(points, axis=0).astype(int)) for points in clusters.values()]
        
        return averaged_coordinates
    
    def last_inventory(self):
        screenshot = pyautogui.screenshot(region=(self.rx+self.width-85, self.ry+self.height-70, 30, 20))
        screenshot.save('images/last_inv.png')
        return screenshot

    def img_detection(self, input_img, threshold = .75, alpha = 0.4, inventory = False):

        if isinstance(input_img, str):
            input_img = Image.open(input_img)

        if inventory == True:
            #not finshed
            screenshot = pyautogui.screenshot(region=(self.rx, self.ry, self.width, self.height))
        else:
            screenshot = pyautogui.screenshot(region=(self.rx, self.ry, self.width, self.height))

        try:
            haystack_color = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            needle_color = cv2.cvtColor(np.array(input_img.convert("RGB")), cv2.COLOR_RGB2BGR)

            # 2. Prepare edge maps for shape
            haystack_gray  = cv2.cvtColor(haystack_color, cv2.COLOR_BGR2GRAY)
            needle_gray  = cv2.cvtColor(needle_color, cv2.COLOR_BGR2GRAY)

            haystack_edges = cv2.Canny(haystack_gray, 50, 150)
            needle_edges = cv2.Canny(needle_gray, 50, 150)
            # (optional) thicken edges so small gaps don’t break the contour
            kernel = np.ones((3,3), np.uint8)

            haystack_edges = cv2.dilate(haystack_edges, kernel, iterations=1)
            needle_edges = cv2.dilate(needle_edges, kernel, iterations=1)

            # 3. Run two needle matches
            res_color = cv2.matchTemplate(haystack_color, needle_color, cv2.TM_CCOEFF_NORMED)
            res_shape = cv2.matchTemplate(haystack_edges, needle_edges, cv2.TM_CCOEFF_NORMED)

            # 4. Blend them: alpha * color_score + (1 - alpha) * shape_score
            result = cv2.addWeighted(res_color, alpha, res_shape, 1 - alpha, 0)

            # 5. Threshold and extract centers
            loc = np.where(result >= threshold)
            coords = list(zip(*loc[::-1]))
            width_adj, height_adj = needle_color.shape[1] // 2, needle_color.shape[0] // 2
            coords = [(self.rx + x + width_adj, self.ry + y + height_adj) for x,y in coords]
            grouped = self.group_nearby_coordinates(coords, eps=4)
        except IndexError as e:
            print('img not found')
            return False
        return grouped 
    
    
    def hash_detection(self, target_hash_str, target_w, target_h, threshold=5, step=2):
        """
        Scans the client area for a matching perceptual hash.
        """
        # 1. Capture the current client state
        screenshot = pyautogui.screenshot(region=(self.rx, self.ry, self.width, self.height))
        
        # 2. Convert the input string back to a Hash object
        needle_hash = imagehash.hex_to_hash(target_hash_str)
        
        found_coords = []
        
        # 3. Sliding Window Search
        for y in range(0, self.height - target_h, step):
            for x in range(0, self.width - target_w, step):
                
                crop = screenshot.crop((x, y, x + target_w, y + target_h))
                haystack_hash = imagehash.average_hash(crop)
                
                if (needle_hash - haystack_hash) <= threshold:
                    center_x = self.rx + x + (target_w // 2)
                    center_y = self.ry + y + (target_h // 2)
                    found_coords.append((center_x, center_y))

        # 4. Filter duplicates (Get the list of grouped matches)
        matches = self.group_nearby_coordinates(found_coords, eps=target_w // 2)
        
        # === FIXES FOR UNPACKING ===
        
        # If no matches found, return None, None
        # This prevents "TypeError: cannot unpack non-iterable bool object"
        if not matches:
            return None, None

        # Take the FIRST match from the list (since you are assigning to single x, y)
        first_match = matches[0]
        
        # Unwrap and cast numpy types to standard python integers
        final_x = int(first_match[0])
        final_y = int(first_match[1])

        return final_x, final_y


