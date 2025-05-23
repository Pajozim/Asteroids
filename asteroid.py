import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      rot_angle = random.uniform(20, 50)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      vector_1 = self.velocity.rotate(rot_angle)
      vector_2 = self.velocity.rotate(-rot_angle)
      smaller_A1 = Asteroid(*self.position, new_radius)
      smaller_A1.velocity = vector_1 * 1.2
      smaller_A2 = Asteroid(*self.position, new_radius)
      smaller_A2.velocity = vector_2 * 1.3