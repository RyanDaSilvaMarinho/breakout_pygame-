import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
BlACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
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
    screen.fill(BlACK)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.draw.rect(screen, WHITE, paddle)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)
