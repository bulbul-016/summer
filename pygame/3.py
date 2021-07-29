import pygame

pygame.init()

screen=pygame.display.set_mode((800, 800))

pygame.display.set_caption("GAME")

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0 ,0)
GREEN=(0, 255,0)
BLUE=(0, 0, 255)

ok=True
color=BLACK
while ok:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ok=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                color=GREEN if color==BLACK else BLACK

  
    screen.fill(WHITE) #color of screen

    pygame.draw.rect(screen, color,(200,550,200,100))
    #...rect(surface, color, rect) 
   
    pygame.display.flip() #for to show changes

pygame.quit()