import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_FREQ, PLAYER_SHOT_SPEED
from shot import Firing

class Player(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.rotation = 0

    # in the player class
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    self.move(dt)
    self.shoots()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)

  def move(self, dt):
    keys = pygame.key.get_pressed()
    forward = pygame.Vector2(0, 1).rotate(self.rotation)

    if keys[pygame.K_w]:
      self.position += forward * PLAYER_SPEED * dt
    if keys[pygame.K_s]:
      self.position -= forward * PLAYER_SPEED * dt
    
  def shoots(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      shoot = Firing(self.position.x * 1.10, self.position.y * 1.10)
      shoot.velocity = pygame.Vector2(0,1).rotate(self.rotation)