import time
import pyautogui
import keyboard
from pynput import mouse

coords = []

def on_click(x, y, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
        coords.append((x, y))
        if len(coords) >= 2:
            return False  # stop listener after 2 clicks

# Record 2 coordinates
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("Captured coordinates:", coords)

# Main loop
while True:
    if keyboard.is_pressed('6'):
        pyautogui.click(coords[0][0], coords[0][1])
        time.sleep(0.7)
        pyautogui.click(coords[1][0], coords[1][1])
        time.sleep(0.7)
    elif keyboard.is_pressed('esc'):
        print("Exiting...")
        break
    else:
        time.sleep(0.1)  # avoid CPU spin