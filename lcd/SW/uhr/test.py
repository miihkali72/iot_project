#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python Imports
import os
import pygame
import sys
import time

pygame.init()
window = pygame.display.set_mode((320,240)) 
window.fill(pygame.Color(255,0,0))
font1 = pygame.font.SysFont("monospace", 66)
rect1 = pygame.Rect(0, 50, 319, 68)
os.system("tft_init")
#os.system("tft_clear")
#os.system("tft_pwm 60")
window.fill(pygame.Color(0,0,0))
for fontname in pygame.font.get_fonts():
	print fontname
sys.exit()
i = 0
while True:
	try:
		#window.fill(pygame.Color(0,0,0))
		pygame.draw.rect(window, pygame.Color(60,0,0), rect1)
		i = i + 1
		label1 = font1.render(str(i), 1, (255,255,0))
		window.blit(label1, (0,50))	
		pygame.image.save(window, "/ram/temp.bmp")        	
		os.system("tft_bmp /ram/temp.bmp")
		
	except:
                sys.exit()

