import pygame

pygame.init()

screen=pygame.display.set_mode((800, 800))

pygame.display.set_caption("mqssmbk")

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0 ,0)
GREEN=(0, 255,0)
BLUE=(0, 0, 255)

ok=True

x,y=500,300

while ok:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ok=False
    
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE] and y==300: 
        y=350
        x=530
    else: y=300
  
    screen.fill(BLACK) #color of screen

    pygame.draw.line(screen, WHITE, (400,300), (400,550), 5)   

    pygame.draw.line(screen, WHITE, (300,300), (400,400), 5)
    pygame.draw.line(screen, WHITE, (400,400), (x,y), 5)
  
    pygame.draw.line(screen, WHITE, (400,550), (300,650), 5)
    pygame.draw.line(screen, WHITE, (400,550), (500,650), 5)
  

    pygame.draw.circle(screen, WHITE, (400,300), 50)
    #...circle(surface, color, center, radius)
    
    pygame.display.flip() #for to show changes

pygame.quit()