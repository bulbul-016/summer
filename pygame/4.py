import pygame

pygame.init()

screen=pygame.display.set_mode((800, 800))

pygame.display.set_caption("GAME")

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0 ,0)
GREEN=(0, 255,0)
BLUE=(0, 0, 255)

x, y = 10 ,10

ok=True
color=BLACK
while ok:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ok=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                color=GREEN if color==BLACK else BLACK
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                x+=10
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                x-=10
            if event.key in [pygame.K_UP, pygame.K_w]:
                y-=10
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                y+=10

  
    screen.fill(WHITE) #color of screen

    pygame.draw.rect(screen, color,(x,y,200,100))
    #...rect(surface, color, rect) 
   
    pygame.display.flip() #for to show changes

pygame.quit()