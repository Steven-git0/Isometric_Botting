import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import pyautogui
import numpy as np
import pygetwindow as gw
import time
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import pygetwindow as gw
from sklearn.cluster import DBSCAN


class screenscrape:

    def __init__(self, window_title): 
        window = gw.getWindowsWithTitle(window_title)[0]
        if not window:
            print(f"No window found with title '{window_title}'")
            exit()
        self.rx, self.ry, self.width, self.height = window.left, window.top, window.width, window.height
    
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
            print(f"Not target text: {text}")
            return False
    
    def check_health(self, threshold = 9):
        #x = 1220+30 y = 75+30
        missing_health = np.array([19,19,19])
        health_screenshot = pyautogui.screenshot(region=(1218, 75, 30, 30))
        image = np.array(health_screenshot)

        for y in range(image.shape[0]):
            row = image[y,:,:]
            if np.any(np.all(row == missing_health, axis=1)):  # Check if the target color exists in this row
                print(f"Color found in row {y}")
                if y >= threshold:
                    return True
        
    def skill_text(self, activity =''):
        #green_color = np.array([0, 255, 0])
        red_color = np.array([255, 0, 0])
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
        #All other skill activities textbox
        else:
            screenshot = pyautogui.screenshot(region=(self.rx+10, self.ry+20, 150, 100))
    
        screenshot.save("C:/Users/Steven/OneDrive/Documents/Runescape/screenshot_skilltext.png")
    
        image = np.array(screenshot) 
        mask = cv2.inRange(image, red_color, red_color)

        if cv2.countNonZero(mask) > 0:
            print('Idle')
            return False
        else:
            print('Action')
            return True
        
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
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
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

                squares.append((cx,cy))

        else:
            print("Color not found on the screen.")

        return squares

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

    def img_detection(self, input_img, threshold = .70, area = None):

        #add values to tuples to get the center coordinates 
        image = Image.open(input_img)
        width_adj, height_adj = image.size[0] // 2, image.size[1] // 2
        if area == 'experience':
            screenshot = pyautogui.screenshot(region=(self.rx + self.width-380, self.ry+30, 120, 35))
            screenshot.show()
        else:
            screenshot = pyautogui.screenshot(region=(self.rx, self.ry, self.width, self.height))
            #screenshot.show()
        screenshot_np = np.array(screenshot)

        # Convert RGB screenshot to Grayscale
        haystack_img = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
        # Load the input image (file path)
        needle_img = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)
        try:
            #testing display purposes
            # print(needle_img.dtype, haystack_img.dtype)
            result = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)
            #cv2.imshow('Results', result)
            #cv2.waitKey()
            #threshold % match accepted result
            loc = np.where(result >= threshold)
            # Zip the coordinates into a list of (x, y) tuples
            coordinates = list(zip(*loc[::-1]))
            #add the adjustments to get the centre location
            coordinates = [(x+width_adj, y+height_adj) for x, y in coordinates]
            #group to prevent duplicate images of the same location
            grouped_coordinates = self.group_nearby_coordinates(coordinates, eps=4)

            # Print the coordinates
            # for coord in grouped_coordinates:
            #     print("Match found at:", coord)

        except IndexError as e:
            print('img not found')
            return False

        return grouped_coordinates

