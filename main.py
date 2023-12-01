import pygame

pygame.init()
WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
rect = pygame.Rect(WIN_WIDTH / 2, WIN_HEIGHT / 1.1, 100, 20)
VELOCITY = 1
direction = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction['UP'] = True
            elif event.key == pygame.K_DOWN:
                direction['DOWN'] = True
            elif event.key == pygame.K_RIGHT:
                direction['RIGHT'] = True
            elif event.key == pygame.K_LEFT:
                direction['LEFT'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction['UP'] = False
            elif event.key == pygame.K_DOWN:
                direction['DOWN'] = False
            elif event.key == pygame.K_RIGHT:
                direction['RIGHT'] = False
            elif event.key == pygame.K_LEFT:
                direction['LEFT'] = False

    if direction['UP']:
        rect.y -= VELOCITY
    if direction['DOWN']:
        rect.y += VELOCITY
    if direction['LEFT']:
        rect.x -= VELOCITY
    if direction['RIGHT']:
        rect.x += VELOCITY

    if rect.left > WIN_WIDTH:
        rect.right = WIN_WIDTH
    if rect.top > WIN_HEIGHT:
        rect.bottom = WIN_HEIGHT

    WIN.fill((0, 0, 0))  # fill the screen with black
    pygame.draw.rect(WIN, (255, 255, 255), rect)  # draw our rectangle
    pygame.display.update()  # update the display
