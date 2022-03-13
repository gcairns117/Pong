import pygame
import paddles, ball, pong_functions

# Keys to be used imported for easier access
from pygame.locals import (KEYDOWN, K_ESCAPE, K_SPACE, QUIT)

pygame.init()

# Create game window
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 480
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI Pong")
icon = pygame.image.load("AI.png")
pygame.display.set_icon(icon)

clock, FPS = pygame.time.Clock(), 60

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 8
WINNING_SCORE = 5

# Game loop
def main():
    running = True
    left_paddle = paddles.Paddle(10, WINDOW_HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = paddles.Paddle(WINDOW_WIDTH-10-PADDLE_WIDTH, WINDOW_HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    both_paddles = [left_paddle, right_paddle]
    pong_ball = ball.Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, BALL_RADIUS)
    left_score, right_score = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    if left_score == WINNING_SCORE or right_score == WINNING_SCORE:
                        left_score, right_score = pong_functions.restart(left_score, right_score, pong_ball, left_paddle, right_paddle)

        pong_functions.draw(WINDOW, both_paddles, pong_ball, left_score, right_score)
        pressed_keys = pygame.key.get_pressed()
        pong_functions.handle_paddle_movement(pressed_keys, left_paddle, right_paddle)
        pong_ball.move()
        pong_functions.handle_collision(pong_ball, left_paddle, right_paddle)
        left_score, right_score = pong_functions.pointScored(pong_ball, left_score, right_score, left_paddle, right_paddle)
        pong_functions.checkScore(WINDOW, left_score, right_score, pong_ball, left_paddle, right_paddle)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# If this is the module run, then call main() 
if __name__ == '__main__':
    main()