import pygame
#from database import connect_database, database_version
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

  Player.containers = (g_updatable, g_drawable)

  player = Player(x, y, PLAYER_RADIUS)

  #--
  AsteroidField.containers = (g_updatable,)

  asteroid_field = AsteroidField()

  g_asteroids = pygame.sprite.Group()

  Asteroid.containers = (g_asteroids, g_updatable, g_drawable)

  #end of grouping

  while True:
    pygame.Surface.fill(screen, (0,0,0))
    for py_object in g_updatable:
      py_object.update(dt)
    for py_object in g_drawable:
      py_object.draw(screen)  # Drawing each object in the group
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
  
    clock.tick(60)
    dt = clock.tick(60) / 1000
  
  #end of game loop


if __name__ == "__main__":
    main()