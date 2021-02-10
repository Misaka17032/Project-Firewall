import pygame
import os
def beep():
	os.system('osascript -e "set volume 10"')
	pygame.mixer.init()
	track = pygame.mixer.music.load("warn.mp3")  
	pygame.mixer.music.play()