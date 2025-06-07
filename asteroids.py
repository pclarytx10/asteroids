import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, width=2):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width
        )
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the direction of the new asteroids
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius / 2

        for v in [a, b]:
            asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
            asteroid.velocity = v * 1.2


        