import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
wall_width = 16
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
GAP_X, GAP_Y = 2, 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (212, 218, 212)
BLUE = (0, 97, 148)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

# Inicialização da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Inicialização da bola
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, 5]

# Inicialização da raquete
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Inicialização dos tijolos
bricks = []
for row in range(5):
    for col in range(WIDTH // BRICK_WIDTH):
        brick_x = col * BRICK_WIDTH
        brick_y = row * BRICK_HEIGHT
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7

    # Movimentação da bola
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Colisão da bola com as paredes
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Colisão da bola com a raquete
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]

    # Colisão da bola com os tijolos
    brick_hit = ball.collidelist(bricks)
    if brick_hit != -1:
        del bricks[brick_hit]
        ball_speed[1] = -ball_speed[1]

    # Verificar se o jogador perdeu
    if ball.bottom >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Desenhar na tela
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.draw.rect(screen, WHITE, paddle)

    pygame.draw.line(screen, GREY, [0, 9], [WIDTH, 9], 20)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT], 20)

    pygame.draw.line(screen, BLUE, [0, 585], [wall_width - 1, 585], wall_width - 5)
    pygame.draw.line(screen, BLUE, [WIDTH, 585], [WIDTH - 18, 585], wall_width - 5)

    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)