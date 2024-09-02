import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialize pygame
    pygame.init()

    # Create screen canvas
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create clock object to control fps
    clock = pygame.time.Clock()

    # Create update and draw Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add player to groups
    Player.containers = (updatable, drawable)

    # Add asteroids to groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add Asteroid field to updatable
    AsteroidField.containers = updatable

    # Instanciate AsteroidField
    asteroid_field = AsteroidField()

    # Instanciate player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # initialize delta time variable for frame control
    dt = 0

    # main game loop
    while True:

        # check for close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Control canvas display and updates
        for obj in updatable:
            obj.update(dt)
        
        screen.fill("black") # draw black screen
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip() # refresh screen

        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
