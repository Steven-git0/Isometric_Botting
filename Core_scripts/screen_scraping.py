import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import pyautogui
import numpy as np
import time
import cv2
from PIL import Image, ImageEnhance, ImageFilter
import pygetwindow as gw

window_title = 'RuneLite - litlGenocide'

class screenscrape:
    #Read text for a defined region
    def read_text(target_text):
        # Capture a region of the screen and save it as an image file
        screenshot = pyautogui.screenshot(region=(1, 860, 525, 170))
        screenshot = screenshot.resize((6000, 2000), Image.LANCZOS)
        screenshot.save("screenshot.png")

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(screenshot)
        screenshot = enhancer.enhance(2.0)
        #use cv2 to convert into black and white to make blue letters readable
        image = cv2.imread('screenshot.png')
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_image = clahe.apply(gray_image)
        #save image as new file
        cv2.imwrite('processed_image.png', enhanced_image)

        # Load the saved screenshot image
        image = Image.open("processed_image.png")

        # Use Tesseract to perform OCR
        text = pytesseract.image_to_string(image)

        # Check if the target text is found in the OCR result
        if target_text in text:
            print(f"Found target text: {target_text}")
            return True
        else:
            print(f"Not target text: {text}")
            return False
    
    # def read_other(target, number = False):
    #     screenshot = pyautogui.screenshot(region=(35, 115, 40, 30))
    #     screenshot = screenshot.resize((80, 50), Image.LANCZOS)
    #     screenshot.save("screenshot.png")

    #     # Enhance contrast
    #     enhancer = ImageEnhance.Contrast(screenshot)
    #     screenshot = enhancer.enhance(2.0)
    #     #use cv2 to convert into black and white to make blue letters readable
    #     image = cv2.imread('screenshot.png')
    #     # Convert the image to grayscale
    #     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #     # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    #     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    #     enhanced_image = clahe.apply(gray_image)
    #     #save image as new file
    #     cv2.imwrite('processed_image.png', enhanced_image)

    #     # Load the saved screenshot image
    #     image = Image.open("processed_image.png")

    #     # Use Tesseract to perform OCR
    #     text = pytesseract.image_to_string(image)

    #     # Check if the target text is found in the OCR result
    #     if target in text:
    #         print(f"Found target text: {target_text}")
    #         return True
    #     else:
    #         print(f"Not target text: {text}")
    #         return False
    
    #set threshold to 5 upon finishing activity to heal full health
    def check_health(threshold = 9):
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
        
        
    def skill_text(activity =''):
        #green_color = np.array([0, 255, 0])
        red_color = np.array([255, 0, 0])
        screenshot = None
        #Wintertodt bottom left text box
        if activity == 'wintertodt_sw':
            screenshot = pyautogui.screenshot(region=(10, 770, 130, 85))
        #Wintertodt top left text box
        elif activity == 'wintertodt_nw':
            screenshot = pyautogui.screenshot(region=(35, 115, 40, 30))
        elif activity == 'wintertodt_bar':
            red_color = np.array([204, 0, 0])
            screenshot = pyautogui.screenshot(region=(5, 50, 15, 15))
        #All other skill activities textbox
        else:
            screenshot = pyautogui.screenshot(region=(20, 50, 115, 21))
    
        screenshot.save("C:/Users/Steven/OneDrive/Documents/Runescape/screenshot_skilltext.png")
    
        image = np.array(screenshot) 
        mask = cv2.inRange(image, red_color, red_color)

        if cv2.countNonZero(mask) > 0:
            print('Idle')
            return False
        else:
            print('Action')
            return True
        
    
    #check if text exist under mouse (for wood cutting)
    def mouse_text():
        # Capture a region of the screen and save it as an image file
        x, y = pyautogui.position()
        screenshot = pyautogui.screenshot(region=(x, y+20, 140, 25))
        screenshot.save("C:/Users/Steven/Runescape/osrs_images/rawshot.png")
        screenshot = screenshot.resize((400, 100), Image.LANCZOS)
        screenshot.save("C:/Users/Steven/Runescape/osrs_images/screenshot.png")

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(screenshot)
        screenshot = enhancer.enhance(2.0)
        #use cv2 to convert into black and white to make blue letters readable
        image = cv2.imread('screenshot.png')
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_image = clahe.apply(gray_image)
        #save image as new file
        cv2.imwrite('processed_image.png', enhanced_image)

        # Load the saved screenshot image
        image = Image.open("processed_image.png")

        # Use Tesseract to perform OCR
        text = pytesseract.image_to_string(image)
        print(text)
        
        return text

        # Check if the target text is found in the OCR result
    

    def find_contours(target_color, color_t1 = 5, color_t2 = 5, color_t3 = 5, area_tolerance = 20):

        window = gw.getWindowsWithTitle(window_title)[0]
        if not window:
            print(f"No window found with title '{window_title}'")
            exit()
        x, y, width, height = window.left, window.top, window.width, window.height

        #in osrs client this is the location to get the screen shot.
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save("C:/Users/Steven/Runescape/osrs_images/screenshot.png")
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

                duplicate_check = False

                # count = 0
                # for x,y in squares:
                #     if x - area_tolerance < cx < x + area_tolerance and y - area_tolerance < cy < y + area_tolerance:
                #         duplicate_check = True
                #         squares[count] = ((cx+x)//2, (cy+y)//2)
                #         count += 1
                #         break

                if duplicate_check == False:
                    squares.append((cx,cy))

        else:
            print("Color not found on the screen.")

        return squares


    def img_detection(input_img, threshold = .90, x1 = 1, y1 = 1, x2 = 1450, y2 = 1050):
        # Take a screenshot
        screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
        
        screenshot.save("C:/Users/Steven/OneDrive/Documents/Runescape/img_screenshot.png")

        haystack_img = cv2.imread('img_screenshot.png', cv2.IMREAD_GRAYSCALE)
        needle_img = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)
        try:
            #testing dispaly purposes
            # print(needle_img.dtype, haystack_img.dtype)
            result = cv2.matchTemplate(haystack_img, needle_img, cv2.TM_CCOEFF_NORMED)
            #cv2.imshow('Results', result)
            #cv2.waitKey()
            #threshold % match accepted result
            loc = np.where(result >= threshold)
            # Zip the coordinates into a list of (x, y) tuples
            coordinates = list(zip(*loc[::-1]))

            # Print the coordinates
            for coord in coordinates:
                print("Match found at:", coord)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        except IndexError as e:
            print('img not found')
            return False

        return coordinates

