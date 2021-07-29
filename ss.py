import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ok = True
game_over=False
block=10
clock = pygame.time.Clock()
FPS = 10

x, y = 10, 10
dx, dy = 0,0

slength=1
slist=[]

foodx=round(random.randrange(0, WIDTH-block)/10.0)*10.0
foody=round(random.randrange(0, HEIGHT-block)/10.0)*10.0

def score_snake(score):
    score_font=pygame.font.SysFont(None, 30)
    value=score_font.render("score: " + str(score), True, GREEN)
    screen.blit(value, [0,0])
    
def draw_snake(block, slist):
    for item in slist:
        pygame.draw.rect(screen,BLUE,[item[0], item[1], block, block])
def kedergi():
    pygame.draw.rect(screen, RED,[(WIDTH/3), HEIGHT/3, block,block*8])
    pygame.draw.rect(screen, RED,[(WIDTH/3), HEIGHT/3, block*20,block])
    pygame.draw.rect(screen, RED,[(WIDTH/3)+(20*block), HEIGHT/3-(7*block), block,block*8])


while ok:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx=block
                dy=0
            if event.key == pygame.K_LEFT:
                dx=-block
                dy=0
            if event.key == pygame.K_UP:
                dy=-block
                dx=0
            if event.key == pygame.K_DOWN:
                dy=block
                dx=0
    
    x += dx
    y += dy
    
            
    if x>=500 or x<=0 or y>=500 or y<=0:
        game_over=True
    
    screen.fill(WHITE)
    kedergi()
    pygame.draw.rect(screen, GREEN, (foodx, foody,10, 10))
    
    snake_head=[]
    snake_head.append(x)
    snake_head.append(y) 

    slist.append(snake_head)
    
    if len(slist) > slength:
        del slist[0]

    draw_snake(block, slist)
    score_snake(slength-1)

    pygame.display.flip()

    if x==foodx and y==foody:
        foodx=round(random.randrange(0, WIDTH-block)/10.0)*10.0
        foody=round(random.randrange(0, HEIGHT-block)/10.0)*10.0
        slength+=1
    while game_over:
        font_message=pygame.font.SysFont(None, 30)
        screen.fill(BLACK)
        messg=font_message.render("GAME OVER!", True, WHITE)
        screen.blit(messg, [200, 250])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    clock.tick(FPS)

pygame.quit()