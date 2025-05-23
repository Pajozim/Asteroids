import pygame
import time
#from database import connect_database, database_version
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Firing


def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

  pygame.init()

  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  #groups
  g_updatable = pygame.sprite.Group()
  g_drawable = pygame.sprite.Group()
  g_asteroids = pygame.sprite.Group()
  g_shots = pygame.sprite.Group()

  Player.containers = (g_updatable, g_drawable)

  player = Player(x, y, PLAYER_RADIUS)

  Firing.containers = (g_shots, g_updatable, g_drawable)

  #--
  AsteroidField.containers = (g_updatable)

  AsteroidField()

  Asteroid.containers = (g_asteroids, g_updatable, g_drawable)

  #end of grouping

  while True:
    pygame.Surface.fill(screen, (0,0,0))
    for py_object in g_updatable:
      py_object.update(dt)
    for py_object in g_drawable:
      py_object.draw(screen)  # Drawing each object in the group
    for asteroid in g_asteroids:
      if asteroid.collision(player):
          print("Game Over!")
          time.sleep(3)
          return pygame.quit
      for shot in g_shots:
        if shot.collision(asteroid):
            shot.kill()
            asteroid.split()
    
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
  
    clock.tick(60)
    dt = clock.tick(60) / 1000
  
  #end of game loop


if __name__ == "__main__":
    main()