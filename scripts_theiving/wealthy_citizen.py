
window_title = "RuneLite - litlGenocide"
mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

def small_break():
    if random.uniform(0, 100) <= 2:
        print('taking break')
        time.sleep(random.uniform(60, 600))

def check_distance():

    mx, my = pyautogui.position()
    points = mouse_movements.move_contours(color=[5, 250, 250])
    x, y = tuple(map(lambda s: s / len(points), map(sum, zip(*points)))) if points else (None, None)
    distance = ((mx-(x))**2 + (my-(y+3))**2)**.5

    return distance if distance else float('inf')
    