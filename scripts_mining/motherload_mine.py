from core_scripts.screen_scraping import *
from core_scripts.movements import *
import pygetwindow as gw
import time
import tkinter as tk
from tkinter import simpledialog

# def inputs():
#     root = tk.Tk()
#     root.title("Motherload mine")
#     # Show the input popup
#     username = simpledialog.askstring("Userame", "Please enter your characters Username to find the Client:")

#     # Show an additional instructions popup
#     if username:
#         tk.messagebox.showinfo("Instructions", f"Hello {username}!\n\nPlease follow the steps below:\n1. Step one...\n2. Step two...\n3. Step three...")
#     return username

# username = input()
window_title = "RuneLite - litlGenocide"

window = gw.getWindowsWithTitle(window_title)[0]
if not window:
    print(f"No window found with title '{window_title}'")
    exit()
rx, ry, width, height = window.left, window.top, window.width, window.height

mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)
#4 for regular, 7 for large
sack_size = 7
#screenshot = pyautogui.screenshot(region=(width-235, height-310, 235, 310))
#screenshot.show()

while True:
    for i in range(sack_size):
        #start from the left
        if i > 0:
            mouse_movements.move_mouse(.048689, .700701, 4)
            mouse_movements.perform_click()
            time.sleep(random.uniform(8.50, 9.00))

            while screenscrape.skill_text("motherload") == True:
                    time.sleep(random.uniform(4.00, 7.00))
        
        while screenscrape.read_text("full") == False:
            #find the coordinates of the contour 
            contour_x, contour_y = mouse_movements.relative_move()
            #find the pickaxe picture closest to the contour
            pickaxe_coords = screenscrape.img_detection(input_img="osrs_images\OSRS_mining.png", threshold= .60)
            pickaxe_coords = sorted(pickaxe_coords, key = lambda p: ((p[0]-(contour_x*.660))**2 + (p[1]-(contour_y*1.240))**2)**.5)
            x,y = pickaxe_coords[0]
            mouse_movements.move_mouse(x, y, 4)
            mouse_movements.perform_click()
            time.sleep(random.uniform(7.00, 8.00))
            
            while screenscrape.skill_text("motherload") == True:
                time.sleep(random.uniform(4.00, 7.00))

            if random.uniform(0.00, 100.00) <= 3.50:
                print('taking quick break')
                time.sleep(random.uniform(60.00, 600.00))

        hammer_coords = screenscrape.img_detection(input_img="osrs_images\osrs_hammer.png", threshold= .50)
        #sort coords by lowest to highest incase invenotry is opened
        hammer_coords = sorted(hammer_coords, key=lambda t: t[1])
        if hammer_coords:
            x,y = hammer_coords[0]
            mouse_movements.move_mouse(x+5, y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(10.10, 12.60))

            x,y = mouse_movements.relative_move("right")
            mouse_movements.move_mouse(rx+x, ry+y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(9.60, 10.10))

        else:   
            x,y = mouse_movements.relative_move("right", offset = 150)
            mouse_movements.move_mouse(rx+x, ry+y, 2)
            mouse_movements.perform_click()
            time.sleep(random.uniform(9.90, 12.40))
        
        
    mouse_movements.move_mouse(.540824, .814815, 4)
    mouse_movements.perform_click()
    time.sleep(random.uniform(3.22, 3.44))
    mouse_movements.move_mouse(.435206, .669666, 4)
    time.sleep(random.uniform(1.00, 1.10))
    mouse_movements.perform_click()
    time.sleep(random.uniform(2.50, 3.00))

    for i in range(sack_size):

        mouse_movements.move_mouse(.692889, .380380, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.35, 4.75))

        #click bank icon
        x, y = screenscrape.npz_detection('image_identification/deposit_inv.npz')[0]
        mouse_movements.move_mouse(x, y, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(.50, 1.00))

        if i == sack_size-1:
            break

        mouse_movements.move_mouse(.233708, .668669, 3)
        mouse_movements.perform_click()
        time.sleep(random.uniform(4.80, 5.35))
    
    if random.uniform(0, 100) <= 1:
                print('taking quick break')
                time.sleep(random.uniform(10, 300.00))

    mouse_movements.move_mouse(.2037, .2732, 3)
    mouse_movements.perform_click()
    time.sleep(random.uniform(9.90, 10.50))
