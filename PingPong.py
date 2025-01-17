import pygame, sys, random

from Pong import player_score_text

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()

# Paddles
player = pygame.Rect(WIDTH-110, HEIGHT/2-50, 10, 100)
opponent = pygame.Rect(110, HEIGHT/2-50, 10, 100)
player_score, opponent_score = 0, 0
# Ball

ball = pygame.Rect(WIDTH/2-10, HEIGHT/2-10, 20, 20)
x_speed, y_speed = 1, 1

while True:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed,y_speed = random.choice([1,-1]), random.choice([1,-1])
    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
        x_speed = -1
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top - ball.width,opponent.bottom + ball.width):
         x_speed = 1

    ball.x += x_speed * 2
    ball.y += y_speed * 2

    if opponent.y < ball.y:
        opponent.top += 1
    if opponent.bottom > ball.y:
        opponent.bottom -= 1


    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")

    SCREEN.fill("black")

    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.circle(SCREEN, "white", ball.center, 10)

    SCREEN.blit(player_score_text, WIDTH/2+50, 50)
    SCREEN.blit(opponent_score_text, WIDTH/2-50, 50)


    pygame.display.update()
    CLOCK.tick(300)