import pygame

pygame.init()

screen=pygame.display.set_mode((800, 800))

pygame.display.set_caption("GAME")

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0 ,0)
GREEN=(0, 255,0)
BLUE=(0, 0, 255)
PI=3.14

ok=True

while ok:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ok=False
  
    screen.fill(WHITE) #color of screen

    pygame.draw.line(screen, RED, (400,0), (0,800), 10)    
    #...line(surface, color, start_pos, end_pos, width)

    pygame.draw.circle(screen, BLUE, (51,51), 50)
    #...circle(surface, color, center, radius)
    pygame.draw.circle(screen, BLUE, (160,56), 55, 5)
    #...circle(surface, color, center, radius, width)

    pygame.draw.rect(screen, GREEN,(200,550,200,100))
    #...rect(surface, color, rect) 
    pygame.draw.rect(screen, GREEN,(450,550,100,200), 6)
    #...rect(surface, color, rect, width)

    pygame.draw.ellipse(screen, BLACK, (410,20,200,40))
    #...ellipse(surface, color, rect)
    pygame.draw.ellipse(screen, BLACK, (630,20,150,50), 6)
    #...ellipse(surface, color, rect, width)
    
    pygame.draw.arc(screen, RED, (20, 200, 100, 100), 0, PI / 2, 10)
    pygame.draw.arc(screen, GREEN, (20, 200, 100, 100), PI / 2, PI, 10)
    pygame.draw.arc(screen, BLUE, (20, 200, 100, 100), PI, 3 * PI / 2, 10)
    pygame.draw.arc(screen, BLACK, (20, 200, 100, 100), 3 * PI / 2, 2 * PI, 10)
    
    pygame.display.flip() #for to show changes

pygame.quit()