#Created by: Brian Kilburn
#12/13/2017
#Final Frontier

import pygame
import random

#start pygame
pygame.init()
#define screen resolution
screenWidth = 800
screenHeight = 600
#variable to hold the display
gameScreen = pygame.display.set_mode((screenWidth, screenHeight))
#set caption
pygame.display.set_caption("Deep Space")
#set up game clock
clock = pygame.time.Clock()
#setup colors to be used
black = (0,0,0)
white = (255,255,255)
dark_red = (128,0,0)
red = (255,0,0)
green = (0,200,0)

#build the stars array
starFall = []
for q in range(150):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    starFall.append([x,y])
    
#ship width
ship_width = 100
#game intro function
def gameIntro():
    intro = True
    pygame.mixer.music.load('IntroMusic.wav')
    pygame.mixer.music.play(-1)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #fill intro screen with black color
        gameScreen.fill(black)
        #drop stars
        for i in starFall:
            i[1]+= 1
            pygame.draw.circle(gameScreen, white, i, 4)
            if i[1] > 600:
                i[1] = random.randrange(-50, -5)
                i[0] = random.randrange(800)
                
        pygame.display.update()
        clock.tick(15)
        
def gameLoop():
    
    
    gameIntro()    
gameLoop()

