import pygame
import random
pygame.init()
pygame.font.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
v = 6
SIZE_BLOCK = 20
score_font = pygame.font.SysFont('Calibri', 28, True, False)

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Hungry lion')

no_eat_block = pygame.sprite.Group()
eat_block = pygame.sprite.Group()
all_list = pygame.sprite.Group()

class Block_red(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > 410:
            self.rect.y = random.randrange(-300, -20)
            self.rect.x = random.randrange(0, screen_width)

class Block_green(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += random.randrange(-1, 2)
        if self.rect.y > 410:
            self.rect.y = random.randrange(-300, -20)
            self.rect.x = random.randrange(0, screen_width)


class Player(Block_red):
    def update(self):
        pos = pygame.key.get_pressed()
        if pos[pygame.K_LEFT]:
            self.rect.x -= v
        elif pos[pygame.K_RIGHT]:
            self.rect.x += v
        elif pos[pygame.K_UP]:
            self.rect.y -= v
        elif pos[pygame.K_DOWN]:
            self.rect.y += v



for i in range(50):
    no_eaten_block = Block_red(RED, SIZE_BLOCK, SIZE_BLOCK)
    eaten_block = Block_green(GREEN, SIZE_BLOCK, SIZE_BLOCK)
    no_eaten_block.rect.x = random.randrange(screen_width)
    no_eaten_block.rect.y = random.randrange(screen_height)
    eaten_block.rect.x = random.randrange(screen_width)
    eaten_block.rect.y = random.randrange(screen_height)
    no_eat_block.add(no_eaten_block)
    eat_block.add(eaten_block)
    all_list.add(no_eaten_block)
    all_list.add(eaten_block)

player = Player(BLUE, SIZE_BLOCK, SIZE_BLOCK)
all_list.add(player)
done = False
clock = pygame.time.Clock()
score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = not done
    screen.fill(WHITE)
    render_score = score_font.render(f'SCORE: {score}', True, (12, 140, 50))
    screen.blit(render_score, (5, 5))
    all_list.update()

    blocks_hit_list = pygame.sprite.spritecollide(player, no_eat_block, True)
    blocks_hit_list2 = pygame.sprite.spritecollide(player, eat_block, True)

    for no_eaten_block in blocks_hit_list:
        score -= 1
    for no_eaten_block in blocks_hit_list2:
        score += 1

    all_list.draw(screen)
    clock.tick(30)
    pygame.display.update()

pygame.quit()
