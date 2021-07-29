import pygame

pygame.init()

screen=pygame.display.set_mode((400, 300))

pygame.display.set_caption("GAME")

ok=True

while ok:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ok=False

pygame.quit()