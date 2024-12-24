import pyautogui
import pygetwindow as gw
import cv2
import numpy as np
import math
import mss
from ultralytics import YOLO


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
    elif ticket_location == (4,2):
        directions = ['right', 'up', 'right']

    #3rd row
    if ticket_location == (1,3):
        directions = ['left', 'left']
    elif ticket_location == (2,3):
        directions = ['left']
    elif ticket_location == (3,3):
        directions = ['stay']
    elif ticket_location == (4,3):
        directions = ['right']
    elif ticket_location == (4,3):
        directions = ['right', 'right']

    #4th row
    if ticket_location == (1,4):
        directions = ['left', 'left', 'down']
    elif ticket_location == (2,4):
        directions = ['left', 'down']
    elif ticket_location == (3,4):
        directions = ['down']
    elif ticket_location == (4,4):
        directions = ['down','right']
    elif ticket_location == (4,4):
        directions = ['down','right', 'right']

    #5th row
    if ticket_location == (1,5):
        directions = ['left', 'down', 'down', 'left']
    elif ticket_location == (2,5):
        directions = ['left', 'down', 'down']
    elif ticket_location == (3,5):
        directions = ['down', 'down']
    elif ticket_location == (4,5):
        directions = ['down', 'right', 'down']
    elif ticket_location == (4,5):
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



screenscrape()

# Find the average coordinates of green pixels
avg_coords = screenshot_minimap()
while (avg_coords is None):
    avg_coords = screenshot_minimap()
print(avg_coords)

print( "Ticket is at: ", avg_coords[0], avg_coords[1])
directions = movement_order(avg_coords)
print(directions)

reverse_dict = {'up' : 'down', 'down' : 'up', 'left' : 'right', 'right' : 'left', 'stay' : 'stay'}
reverse_directions = []

for i in reversed(directions):
    reverse_directions.append(reverse_dict[i])

print(reverse_directions)





