#!/usr/bin/python
# -*- coding: utf-8 -*-

#****************************************************
#   Reimar Barnstorf www.7soft.de                   *
#****************************************************

# Python Imports
import os
import pygame
import sys
import time

pygame.init()
window = pygame.display.set_mode((320,240)) 
font0 = pygame.font.SysFont("droidsans", 21)
font1 = pygame.font.SysFont("droidsans", 83)
font2 = pygame.font.SysFont("freemono", 33)
font3 = pygame.font.SysFont("freemono", 26)
font2.set_italic(1)
font2.set_bold(1)
label0 = font0.render("www.7soft.de PYTHON-Uhr-Demo", 1, (255,0,0)) 
label3 = font3.render("C Reimar Barnstorf ", 1, (255,0,0))
rect1 = pygame.Rect(0, 62, 319, 70)
rect2 = pygame.Rect(0, 150, 319, 35)
os.system("tft_init")
#os.system("tft_clear")
#os.system("tft_pwm 80")
while True:
	try:
		window.fill(pygame.Color(0,0,0))		
		pygame.draw.rect(window, pygame.Color(60,0,0), rect1)
		pygame.draw.rect(window, pygame.Color(0,200,200), rect2)
		pygame.draw.line(window, pygame.Color(0,0,255), (0,210), (319,210))
		pygame.draw.line(window, pygame.Color(0,0,255), (0,239), (319,239))
		lt = time.localtime()
		label1 = font1.render(time.strftime("%H:%M:%S ", lt), 1, (255,255,0))
		window.blit(label1, (0,50))	
                label2 = font2.render(time.strftime("%a %d.%m.%Y ", lt), 1, (0,0,0))
                window.blit(label2, (0,150))
		window.blit(label0, (0,0))
		window.blit(label3, (10,210))
		pygame.image.save(window, "ram/temp.bmp")        	
		os.system("tft_bmp ram/temp.bmp")
        	time.sleep(1)
		
	except:
                sys.exit()

