from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor with PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        
        # Initialize rotation
        self.rotation = 0

        # initialize timer
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        # Cooldown timer
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        self.position += pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_MOVE_SPEED * dt

    def shoot(self):
        # Cooldown check
        if self.timer > 0:
            return
        # Create a new shot
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

        
      