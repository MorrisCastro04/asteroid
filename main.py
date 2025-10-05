import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    track_time = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shoots, updatable,  drawable)
    asteroid_field = AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        player.timer -= dt

        for asteroid in asteroids:
            for shot in shoots:
                if asteroid.collider(shot):
                    asteroid.kill()
                    shot.kill()
            if asteroid.collider(player):
                print("Game over")
                sys.exit()

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        
        dt = track_time.tick(60) / 1000


if __name__ == "__main__":
    main()
