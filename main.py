# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

#main function
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = game_clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()