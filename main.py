import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
wall_width = 16
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 20
GAP_X, GAP_Y = 2, 2
score = 0
chances = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (212, 218, 212)
BLUE = (0, 97, 148)
RED = (162, 8, 0)
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
        brick_y = row * BRICK_HEIGHT + 60
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

clock = pygame.time.Clock()

# Loop principal do jogo
while chances > 0:
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
        bounce_sound.play()
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
        bounce_sound.play()

    # Colisão da bola com a raquete
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]
        bounce_sound.play()
    # Colisão da bola com os tijolos
    brick_hit = ball.collidelist(bricks)
    if brick_hit != -1:
        brick_y = bricks[brick_hit].y
        row = (brick_y - 60) // BRICK_HEIGHT
        del bricks[brick_hit]
        ball_speed[1] = -ball_speed[1]
        scoring_sound.play()

        # Checagem de qual quadradinho foi acertado e a pontuação
        if row < 2:
            score += 7  # Vermelho
        elif 2 <= row < 4:
            score += 5  # Laranja
        elif 4 <= row < 6:
            score += 3  # Verde
        else:
            score += 1  # Amarelo

    # Verificar se o jogador perdeu
    if ball.bottom >= HEIGHT:
        chances -= 1

        ball.center = (WIDTH // 2, HEIGHT // 2)
        paddle.center = (WIDTH // 2, HEIGHT - 20)

        # Aguarde um curto período antes de continuar
        pygame.time.delay(500)

    screen.fill((0, 0, 0))  # Preencha a tela com a cor de fundo
    pygame.draw.rect(screen, (255, 255, 255), paddle)  # Desenhe a plataforma
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # Desenhar na tela
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.draw.rect(screen, WHITE, paddle)

    pygame.draw.line(screen, GREY, [0, 9], [WIDTH, 9], 20)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT], 20)

    pygame.draw.line(screen, BLUE, [0, 585], [wall_width - 1, 585], wall_width - 5)
    pygame.draw.line(screen, BLUE, [WIDTH, 585], [WIDTH - 18, 585], wall_width - 5)

    pygame.draw.line(screen, RED, [0, 78], [wall_width - 1, 78], 40)
    pygame.draw.line(screen, RED, [WIDTH, 78], [WIDTH - 18, 78], 40)

    pygame.draw.line(screen, ORANGE, [0, 118], [wall_width - 1, 118], 40)
    pygame.draw.line(screen, ORANGE, [WIDTH, 118], [WIDTH - 18, 118], 40)

    pygame.draw.line(screen, GREEN, [0, 158], [wall_width - 1, 158], 40)
    pygame.draw.line(screen, GREEN, [WIDTH, 158], [WIDTH - 18, 158], 40)

    pygame.draw.line(screen, YELLOW, [0, 198], [wall_width - 1, 198], 40)
    pygame.draw.line(screen, YELLOW, [WIDTH, 198], [WIDTH - 18, 198], 40)

    for brick in bricks:
        if brick.y / 25 <= 3.5:
            pygame.draw.rect(screen, RED, brick)
        elif brick.y / 25 <= 5.5:
            pygame.draw.rect(screen, ORANGE, brick)
        elif brick.y / 25 <= 6.5:
            pygame.draw.rect(screen, GREEN, brick)
        elif brick.y / 25 <= 8:
            pygame.draw.rect(screen, YELLOW, brick)

    # TODO: Desenhar a pontuação na tela
    score_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
    score_text = score_font.render(f'Score: {score}', True, WHITE)
    score_text_rect = score_text.get_rect()
    screen.blit(score_text, (65, 30))

    chances_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
    chances_text = chances_font.render(f'Chances: {chances}', True, WHITE)
    chances_text_rect = chances_text.get_rect()
    screen.blit(chances_text, (550, 30))

    pygame.display.flip()
    clock.tick(60)
