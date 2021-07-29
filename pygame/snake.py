import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock()
FPS = 5

WHITE,BLACK = (255, 255, 255), (0, 0, 0)
BLUE, GREEN, RED = (0, 0, 255), (0, 255, 0), (255, 0, 0)
color = GREEN
block = 10
dx, dy = block, 0
radius = 10

fx, fy=random.randint(0, 500), random.randint(0, 500)
food_location = fx, fy

body = [[80, 100], [90, 100], [100, 100]]
# Init
# 1) [70, 100], [85, 100], [100, 100]
# Moving to the right
# 2) [85, 100], [100, 100], [115, 100]
# Moving to the right
# 2) [100, 100], [115, 100], [130, 100]
# Moving to the down
# 3) [100, 100], [115, 100], [115, 115]

# Main loop
ok = True
while ok:
  # Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ok = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx, dy = block, 0
      if event.key == pygame.K_LEFT:
        dx, dy = -block, 0
      if event.key == pygame.K_UP:
        dx, dy = 0, -block
      if event.key == pygame.K_DOWN:
        dx, dy = 0, block

  # Move our snake
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0] # x - point
    body[i][1] = body[i - 1][1] # y - point    

  body[0][0] += dx
  body[0][1] += dy

  if body[0][0] >= 500:
    body[0][0] = 0

  if body[0][1] >= 500:
    body[0][1] = 0
  
  for i in range(len(body) - 1, 0, -1):
    #if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
    if (fx in range(body[i][0], body[i-1][0])) and (fy in range(body[i][1], body[i-1][1])):
        body.append([0, 0])
        food_location = random.randint(0, 500), random.randint(0, 500)
  
  # Check for collision head of the snake with food location
  screen.fill(WHITE)

  # Draw food
  pygame.draw.circle(screen, GREEN, food_location, radius)

  # Draw snake
  for i, point in enumerate(body):
    color = RED if i == 0 else BLUE
    pygame.draw.circle(screen, color, point, radius)

  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()