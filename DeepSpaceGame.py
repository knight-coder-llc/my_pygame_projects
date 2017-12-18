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
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

#build the stars array
starFall = []
for q in range(150):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    starFall.append([x,y])
    
#ship width
ship_width = 50
starship = pygame.image.load('spaceShip.png')
enemycraft = pygame.image.load('enemySpaceship.png')
#gamequite function for our quit buttons
def quitgame():
    pygame.quite()
    quit()

#move spaceship
def ship(x,y):
    gameScreen.blit(starship, (x,y))
    
#called message_display
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#function to create input buttons
def button(msg, x, y, w, h, ic, ac, action= None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameScreen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameScreen, ic, (x, y, w, h))
        #add text to button
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x+(w/2), y+(h/2))
    gameScreen.blit(textSurf, textRect)
   

#game intro function
def gameIntro():
    intro = True
    pygame.mixer.music.load('IntroMusic.wav')
    pygame.mixer.music.play(-1)
    #gameScreen.fill(black)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #fill intro screen with black color
        gameScreen.fill(black)
        
        #pygame.draw.rect(gameScreen, white,(screenWidth/2, screenHeight/2,50,50))
        #add some buttons to the screen using button function
        button("Play!",150,450,100,50,green,bright_green,gameLoop) #action will start the game loop
        button("Quit",550, 450,100,50,red,bright_red,quitgame)
        
        #drop stars
        for i in starFall:
            i[1]+= 1
            
            pygame.draw.circle(gameScreen, white, i, 2)
            if i[1] > 600:
                i[1] = random.randrange(-50, -5)
                i[0] = random.randrange(800)
        #draw ship to the screen        
        gameScreen.blit(starship, (screenWidth/2, screenHeight/2))        
        #gameScreen.blit(enemycraft, (screenWidth/2, 25)) 
        
        pygame.display.update()
        clock.tick(60)
        
def gameLoop():
    gameExit = False
    #stop the music in the intro loop and load opening battle music
    pygame.mixer.music.stop()
    pygame.mixer.music.load('OpenAttack.wav')
    pygame.mixer.music.play(-1)
    #starting position
    x = screenWidth/2
    y = screenHeight/2
    #initialize x and y change variables
    x_change = 0
    y_change = 0  
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
                #check for keys pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #checking for left arrow
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:                   
                    y_change = -5
                if event.key == pygame.K_DOWN:                    
                    y_change = 5
                #if event.key == pygame.K_p:
                    #pause = True
                    #paused()
            #check for keys pressed up
            if event.type == pygame.KEYUP:
                #if either left or right key is coming up change variable to 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    
        #new x position for ship
        x += x_change
        y += y_change
        
        #test boundaries for the corners of the screen first, and then test sides
        if x >= screenWidth - 50 and y >= screenHeight - 50:
            x = screenWidth - 50
            y = screenHeight - 50
            
        elif x >= screenWidth - 50 and y <= 0:
            x = screenWidth - 50
            y = 0
            
        elif x <= 0 and y >= screenHeight - 50:
            x = 0
            y = screenHeight - 50
            
        elif x <= 0 and y <= 0:
            x = 0
            y = 0
            
        elif x <= 0:
            x = 0
            
        elif x >= screenWidth - 50:
            x = screenWidth - 50
            
        elif y <= 0:
            y = 0
            
        elif y >= screenHeight - 50:
            y = screenHeight - 50
       
        #fill intro screen with black color
        gameScreen.fill(black)
        
        #drop stars
        for i in starFall:
            i[1]+= 8
            
            pygame.draw.circle(gameScreen, white, i, 2)
            if i[1] > 600:
                i[1] = random.randrange(-50, -5)
                i[0] = random.randrange(800)
        #draw ship to the screen        
        #move car function
        ship(x,y)        
        #gameScreen.blit(enemycraft, (screenWidth/2, 25)) 
        
        pygame.display.update()
        clock.tick(60)
    
gameIntro()
gameLoop()
pygame.quit()
quit()
