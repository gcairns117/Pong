import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 480

class Ball:
    MAX_SPEED = 5
    WHITE, BLACK = (255,255,255), (0,0,0)

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_speed = self.MAX_SPEED
        self.y_speed = 0
    
    def draw(self, window):
        pygame.draw.circle(window, self.WHITE, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_speed = 0
        self.x_speed *= -1

    def stop(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_speed = 0
        self.x_speed = 0