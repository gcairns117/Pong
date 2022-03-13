import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 480
WHITE, BLACK = (255,255,255), (0,0,0)

#creating the paddles
class Paddle:
    COLOUR = WHITE
    SPEED = 5

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rect(window, self.COLOUR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.SPEED
        else:
            self.y += self.SPEED
        # Keeping paddles on screen
        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y