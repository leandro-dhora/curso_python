import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('hip.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
while pygame.mixer.get_busy:
    time.sleep(1)