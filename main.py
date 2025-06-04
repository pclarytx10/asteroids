# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

#main function
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)
    # player.containers = (updatable, drawable)
    
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