import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 0, 0)
FOOD_COLOR = (255, 0, 0)
SCORE_FONT = pygame.font.SysFont("Arial", 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
score = 0
direction = (20, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -20)
            elif event.key == pygame.K_DOWN:
                direction = (0, 20)
            elif event.key == pygame.K_LEFT:
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (20, 0)

    head = snake[-1]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.append(new_head)

    if snake[-1] == food:
        score += 1
        food = (random.randint(0, WIDTH - 20) // 20 * 20, random.randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake.pop(0)

    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
        snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
        snake[-1] in snake[:-1]):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    screen.fill(BACKGROUND_COLOR)
    for pos in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], 20, 20))
    score_text = SCORE_FONT.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(10)
