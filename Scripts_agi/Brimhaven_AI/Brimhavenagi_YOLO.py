import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import math
import mss
from ultralytics import YOLO

#Retired Code for AI image detection, it is currently too slow and requires hardware acceleration
#alternative meathod can be used with no hardware acceleration through runlite client 

def screenscrape():
    window_title = 'RuneLite - litlGenocide'
    window = gw.getWindowsWithTitle(window_title)[0]

    if not window:
        print(f"No window found with title '{window_title}'")
        exit()

    client_dimensions = window.left, window.top, window.width, window.height

    dispenser_list = []
    

    with mss.mss() as sct:
        image = np.array(sct.grab(client_dimensions))
        gpu_image = cv2.cuda_GpuMat()
        gpu_image.upload(image)
        graygpu_image = cv2.cuda.cvtColor(gpu_image, cv2.COLOR_BGR2GRAY)
        gray_image = graygpu_image.download()
        original_height, original_width = image.shape[:2]
        new_width = int(original_width * 0.5)
        new_height = int(original_height * 0.5)
        print("hello")

        # Best for downsampling
        resized_image = cv2.resize(gray_image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        # Optional: Apply adaptive histogram equalization for better contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced_image = clahe.apply(resized_image)
        enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_GRAY2BGR)
        
        # cv2.imshow("Game", enhanced_image)
        # cv2.waitKey(0)
    
        model = YOLO("C:\\Users\\Steven\\brimagi_tensorflow\\best_99.pt")
        results = model(enhanced_image)
        for box in results[0].boxes:
            conf = box.conf[0]  # Confidence score
            if conf >= 0.75:
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