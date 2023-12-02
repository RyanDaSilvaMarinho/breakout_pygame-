import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
WALL_WIDTH = 16
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 20
GAP_X, GAP_Y = 2,2
WHITE = (255, 255, 255)
BlACK = (0, 0, 0)
GREY = (212, 218, 212)
BLUE = (0, 97, 148)
RED = (255, 0, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

# Efeitos sonoros
bounce_sound = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')


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
for row in range(8):
    for col in range(WIDTH // BRICK_WIDTH):
        brick_x = col * BRICK_WIDTH + 25
        brick_y = row * BRICK_HEIGHT + 40
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
    
     # Definir cores com base na linha de tijolos
        if row < 2:
            brick_color = RED
        elif 2 <= row < 4:
            brick_color = ORANGE
        elif 4 <= row < 6:
            brick_color = GREEN
        else:
            brick_color = YELLOW

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
        bounce_sound.play()

    # Colisão da bola com os tijolos
    brick_hit = ball.collidelist(bricks)
    if brick_hit != -1:
        del bricks[brick_hit]
        ball_speed[1] = -ball_speed[1]
        scoring_sound.play()

    # Verificar se o jogador perdeu
    if ball.bottom >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Desenhar na tela
    screen.fill(BlACK)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.draw.rect(screen, WHITE, paddle)

    pygame.draw.line(screen, GREY, [0, 9], [WIDTH, 9], 20)
    pygame.draw.line(screen, GREY, [(WALL_WIDTH / 2) - 1, 0], [(WALL_WIDTH / 2) - 1, HEIGHT], WALL_WIDTH)
    pygame.draw.line(screen, GREY, [(WIDTH - WALL_WIDTH / 2) - 1, 0], [(WIDTH - WALL_WIDTH / 2) - 1, HEIGHT], 20)

    pygame.draw.line(screen, BLUE, [0, 585], [WALL_WIDTH - 1, 585], WALL_WIDTH - 5)
    pygame.draw.line(screen, BLUE, [WIDTH, 585], [WIDTH - 18, 585], WALL_WIDTH - 5)

    for brick in bricks:
        if brick.y / 25 <= 3:
            pygame.draw.rect(screen, RED, brick)
        elif brick.y / 25 <= 4:
            pygame.draw.rect(screen, ORANGE, brick)
        elif brick.y / 25 <= 6:
            pygame.draw.rect(screen, GREEN, brick)
        elif brick.y / 25 <= 8:
            pygame.draw.rect(screen, YELLOW, brick)


    pygame.display.flip()
    clock.tick(60)

