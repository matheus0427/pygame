import pygame
import sys

pygame.init() 

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 7

player1 = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

score1 = 0
score2 = 0

font = pygame.font.Font(None, 74)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy


    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx *= -1

    
    if ball.left <= 0:
        score2 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = BALL_SPEED_X
        ball_dy = BALL_SPEED_Y
    if ball.right >= WIDTH:
        score1 += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = -BALL_SPEED_X
        ball_dy = BALL_SPEED_Y

    
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 10))

  
    pygame.display.flip()

    
    pygame.time.Clock().tick(60) 