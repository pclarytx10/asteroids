import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

#main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    game_clock = pygame.time.Clock()
    dt = 0

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))

        # Update player
        # player.update(dt)
        for obj in updatable:
            obj.update(dt)

        # Re-render the player each frame
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = game_clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()