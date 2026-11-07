from screen_scraping import *
from movements import *
import time
import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for audio to finish playing
        pygame.time.Clock().tick(10)

def checking_and_healing(threshold = 9):
    while screenscrape.check_health(threshold) == True:
        print('Need to heal')
        image1 = Image.open('osrs_images/cooked_tuna.png')
        width1, height1 = image1.size[0] // 2, image1.size[1] // 2
        try:
            x,y = screenscrape.img_detection('osrs_images/cooked_tuna.png', .90)[-1]
            mouse_movements.move_mouse(x + width1, y + height1, 2)
            mouse_movements.perform_click()
            time.sleep(1)
        except:
            print('No Food')
            break

audio_path = 'C:/Users/Steven/OneDrive/Documents/Runescape/mixkit-arabian-mystery-harp-notification-2489.wav'

while True:
    if screenscrape.read_text('defender') == True:
        play_audio(audio_path)
        time.sleep(7)
    checking_and_healing(threshold = 9)
    
    