import pygame
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)
import program

WIDTH, HEIGHT = program.WINDOW_WIDTH, program.WINDOW_HEIGHT
WHITE, BLACK, YELLOW = (255,255,255), (0,0,0), (255,255,0)
SCORE_FONT = pygame.font.SysFont("Arial Unicode MS", 40)
WINNING_SCORE = program.WINNING_SCORE

# drawing game window
def draw(window, paddles, ball, left_score, right_score):
    window.fill(BLACK)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    window.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    window.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(window)
    
    for i in range(5, HEIGHT, HEIGHT//20):
        pygame.draw.line(window, WHITE, (WIDTH//2, i), (WIDTH//2, i+15), 5)

    ball.draw(window)
    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[K_w]:                   
        left_paddle.move(up=True)
    if keys[K_s]:
        left_paddle.move(up=False)
    
    if keys[K_UP]:
        right_paddle.move(up=True)
    if keys[K_DOWN]:
        right_paddle.move(up=False)

def handle_collision(pongball, left_paddle, right_paddle):
    # collision with floor and ceiling
    if pongball.y + pongball.radius >= HEIGHT:
        pongball.y_speed *= -1
    elif pongball.y - pongball.radius <= 0:
        pongball.y_speed *= -1

    def y_collision(paddle, pongball):
        middle_y = paddle.y + paddle.height/2
        difference_in_y = middle_y - pongball.y
        reduction_factor = (paddle.height/2) / pongball.MAX_SPEED
        y_speed = difference_in_y / reduction_factor
        pongball.y_speed = -1 * y_speed

    #collision with paddles
    if pongball.x_speed < 0:
        if pongball.y >= left_paddle.y and pongball.y <= left_paddle.y + left_paddle.height:
            if pongball.x - pongball.radius <= left_paddle.x + left_paddle.width:
                pongball.x_speed *= -1

                y_collision(left_paddle, pongball)

    else:
        if pongball.y >= right_paddle.y and pongball.y <= right_paddle.y + right_paddle.height:
            if pongball.x + pongball.radius >= right_paddle.x:
                pongball.x_speed *= -1

                y_collision(right_paddle, pongball)

def pointScored(ball, left_score, right_score, left_paddle, right_paddle):
    if ball.x < 0:
        right_score +=1
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()
        return left_score, right_score
    elif ball.x > WIDTH:
        left_score +=1
        ball.reset()
        left_paddle.reset()
        right_paddle.reset()
        return left_score, right_score
    else:
        return left_score, right_score

def checkScore(window, left_score, right_score, ball, left_paddle, right_paddle):
    won = False
    if left_score >= WINNING_SCORE:
        won = True
        win_text = "Left Player Wins!"
        text = SCORE_FONT.render(win_text, 1, YELLOW)
        window.blit(text,(WIDTH//4 - text.get_width()//2, 60))
    elif right_score >= WINNING_SCORE:
        won = True
        win_text = "Right Player Wins!"
        text = SCORE_FONT.render(win_text, 1, YELLOW)
        window.blit(text,(WIDTH * (3/4) - text.get_width()//2, 60))

    if won:
        left_paddle.reset()
        right_paddle.reset()
        ball.reset()

def restart(left_score, right_score, ball, left_paddle, right_paddle):
    left_paddle.reset()
    right_paddle.reset()
    ball.reset()
    left_score = right_score = 0
    return left_score, right_score
