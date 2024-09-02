from constants import *
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        # listen for close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw black screen
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip() # update frame

if __name__ == "__main__":
    main()
