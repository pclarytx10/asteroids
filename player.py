import pygame
from circleshape import CircleShape
from constants import *
from shots import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0  

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Normalize the rotation to keep it within 0-360 degrees
        self.rotation %= 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_RADIUS * dt

    def shoot(self):
        if self.cooldown > 0:
            return     
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.cooldown = PLAYER_SHOOT_COOLDOWN

