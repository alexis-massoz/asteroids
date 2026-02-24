import pygame
import random
from circleshape import CircleShape
from constants import * 
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_new_velocity = self.velocity.rotate(angle)
        second_new_velocity = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = first_new_velocity * 1.2
        new_asteroid_2.velocity = second_new_velocity * 1.2