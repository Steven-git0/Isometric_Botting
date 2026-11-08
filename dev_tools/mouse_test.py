import pyautogui
import pywinctl as gw
import time
import random
from Xlib import X, display
from Xlib.ext import shape
from scripts__core.screen_scraping import *
from scripts__core.movements import *

window_title = "RuneLite - litlGenocide"
mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

# Set up transparent click-through X11 overlay to draw a yellow mouse trail
d = display.Display()
s = d.screen()
sw, sh = s.width_in_pixels, s.height_in_pixels
yellow = s.default_colormap.alloc_named_color("yellow").pixel

overlay = s.root.create_window(
    0, 0, sw, sh, 0, s.root_depth,
    X.InputOutput, X.CopyFromParent,
    background_pixel=yellow,
    override_redirect=True,
)

bitmap = overlay.create_pixmap(sw, sh, 1)
gc_clear = bitmap.create_gc(foreground=0)
bitmap.fill_rectangle(gc_clear, 0, 0, sw, sh)
gc_draw = bitmap.create_gc(foreground=1, line_width=3)

# Make overlay completely click-through and initially invisible
overlay.shape_rectangles(shape.SO.Set, shape.SK.Input, 0, 0, 0, [])
overlay.shape_mask(shape.SO.Set, shape.SK.Bounding, 0, 0, bitmap)
overlay.map()
d.sync()

# Hook pyautogui.moveTo so each WindMouse step draws a yellow segment
_orig_moveTo = pyautogui.moveTo
last_pos = [pyautogui.position().x, pyautogui.position().y]

def _moveTo_with_trail(x, y, *args, **kwargs):
    _orig_moveTo(x, y, *args, **kwargs)
    nx, ny = int(x), int(y)
    bitmap.line(gc_draw, last_pos[0], last_pos[1], nx, ny)
    overlay.shape_mask(shape.SO.Set, shape.SK.Bounding, 0, 0, bitmap)
    d.flush()
    last_pos[0], last_pos[1] = nx, ny

pyautogui.moveTo = _moveTo_with_trail

try:
    start_time = time.perf_counter()
    mouse_movements.move_mouse(500, 300)
    elapsed = time.perf_counter() - start_time
    print(f"Mouse movement finished in {elapsed:.4f} seconds")
    time.sleep(5)
finally:
    pyautogui.moveTo = _orig_moveTo
    overlay.unmap()
    overlay.destroy()
    d.close()
