from screen_scraping import *
from movements import *
mouse_movements.perform_click()

time.sleep(3)

for x in range(1100):

    mouse_movements.perform_click()
    time.sleep(random.uniform(.50, .60))
    mouse_movements.perform_click()
    time.sleep(random.uniform(2.1, 2.2))