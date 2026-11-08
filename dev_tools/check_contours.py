from scripts__core.screen_scraping import *
from scripts__core.movements import *

window_title = "RuneLite - litlGenocide"
mouse_movements = mouse_movements(window_title)
screenscrape = screenscrape(window_title)

time.sleep(1)
screenscrape.find_contours(target_color='FFFF0000', color_t1= 20, color_t2= 20, color_t3= 20)