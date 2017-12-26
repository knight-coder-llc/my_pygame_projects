#Created by: Brian Kilburn
#12/13/2017
#Final Frontier

import pygame
import random

#lets create a bullet class to track player and enemy attack
class bullet:
    #initialize position, size, and the color to indicate friend or foe
    def __init__(self, X, Y, color):
        self.x = X
        self.y = Y
        self.width = 4
        self.height = 10
        self.color = color
    #update the position of the bullet in the coordinate plane    
    def update(self, color, X, Y):
        
        #test if friendly fire or enemy and move in the direction necessary
        if color == blue:
            #check for enemy collision here
            self.y -= 8
        else:
            #detect if there is a collision
            if self.x + 3 >= X and self.x <= X + 50 and self.y >= Y and self.y <= Y + 50:                
                    die(X,Y)          
            self.y += 8
            
#let's create an enemy starship class to produce enemies for the player to combat
class enemyShip:
    #initialize
    def __init__(self):
        self.x = random.randrange(50, screenWidth - 50)
        self.y = random.randrange(-50, -5)
    
    #enemy entrance to battle (actually cannot do this here, it must be executed in the main)
    def _enemy(self,x,y):
       gameScreen.blit(enemycraft, (x,y))
       
    #update enemy positions
    def enemyUpdate(self):
        
        #bring the ship into the screen
        if(self.y < 0 ):
            self.y += 3
        
        rand = random.randrange(1,26)
        if rand == 25:
            self.x += random.randrange(-10, 11)
            self.y += random.randrange(-10, 11)
            
        #test boundaries for the corners of the screen first, and then test sides
        if self.x >= screenWidth - 50 and self.y >= screenHeight - 50:
            self.x = screenWidth - 50
            self.y = screenHeight - 50            
        elif self.x >= screenWidth - 50:
            self.x = screenWidth - 50                      
        elif self.x <= 0 and self.y >= screenHeight - 50:
            self.x = 0
            self.y = screenHeight - 50           
        elif self.x <= 0:
            self.x = 0                   
        elif self.x <= 0:
            self.x = 0            
        elif self.x >= screenWidth - 50:
            self.x = screenWidth - 50                               
        elif self.y >= screenHeight//4:
            self.y = screenHeight//4
                    
#start pygame
pygame.init()
#define screen resolution
screenWidth = 800
screenHeight = 600
#variable to hold the display
gameScreen = pygame.display.set_mode((screenWidth, screenHeight))
#set caption
pygame.display.set_caption("StarFall Voyager")
#set up game clock
clock = pygame.time.Clock()
#setup colors to be used
black = (0,0,0)
white = (255,255,255)
dark_red = (128,0,0)
blue = (0,0,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

#bullet list and enemy object list (if needed)
bulletList = []
enemySpritesList = []

#build the stars array
starFall = []
for q in range(150):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    starFall.append([x,y])

    
#ship width
ship_width = 50
starship = pygame.image.load('spaceShip.png').convert()
enemycraft = pygame.image.load('enemySpaceship.png').convert()
explode = pygame.image.load('flame.png').convert()
#gamequite function for our quit buttons
def quitgame():
    pygame.quit()
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
#end game function
def die(x,y):
    
    gameOver = True
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #fill intro screen with black color
        gameScreen.fill(black)
        gameScreen.blit(explode,(x,y))
        
        #add some buttons to the screen using button function
        button("Play!",150,450,100,50,green,bright_green,gameLoop)
        button("Quit",550, 450,100,50,red,bright_red,quitgame)
                
        #drop stars
        for i in starFall:
            i[1]+= 1
            
            pygame.draw.circle(gameScreen, white, i, 2)
            if i[1] > 600:
                i[1] = random.randrange(-50, -5)
                i[0] = random.randrange(800)
        
        pygame.display.update()
        clock.tick(60)
   
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
       
        #add some buttons to the screen using button function
        button("Play!",150,450,100,50,green,bright_green,gameLoop)
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
                if event.key == pygame.K_SPACE:
                   #create bullet object add soundfx
                   playerBullet = bullet(x,y,blue)
                   bulletBlast = pygame.mixer.Sound('playerAttack.wav')
                   bulletBlast.set_volume(0.2)
                   pygame.mixer.Channel(0).play(bulletBlast)
                   bulletList.append(playerBullet)
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
                
        #check if enemyships exist
        if len(enemySpritesList) == 0:
            numEnemies = random.randrange(1,21)
            #initialize enemy ship list
            for i in range(numEnemies):
                enemySpritesList.append(enemyShip())
                
        for i in enemySpritesList:
            i._enemy(i.x,i.y)
            rand = random.randrange(1,201)
            if rand == 100 and i.y >= 0:
                #create bullet object add soundfx
                playerBullet = bullet(i.x,i.y,bright_red)
                bulletBlast = pygame.mixer.Sound('playerAttack.wav')
                bulletBlast.set_volume(0.2)
                pygame.mixer.Channel(1).play(bulletBlast)
                bulletList.append(playerBullet)
                
                
            i.enemyUpdate()
                
        print(x)     
        #iterate the list for the bullets update and remove as necessary        
        for i in bulletList:  
               
            #test if bullet has reached edge of the screen and remove from the list
            if i.y < 0 or i.y > screenHeight:               
                bulletList.remove(i)
            
            else:
                pygame.draw.rect(gameScreen,i.color,(i.x + 3, i.y, i.width, i.height))
                pygame.draw.rect(gameScreen,i.color,(i.x + 40, i.y, i.width, i.height))
                i.update(i.color, x, y)
       
        #move ship function and draw to the screen      
        ship(x,y)        
        
        pygame.display.update()
        clock.tick(60)
    
gameIntro()
gameLoop()
pygame.quit()
quit()
