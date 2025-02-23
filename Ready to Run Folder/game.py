import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invaders: Code Defender")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load assets
spaceship_img = pygame.image.load("spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (50, 50))

alien_img = pygame.image.load("alien.png")
alien_img = pygame.transform.scale(alien_img, (40, 40))

# Fonts
font = pygame.font.Font(None, 36)

# Classes
class Spaceship:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.width = 50
        self.height = 50
        self.speed = 5
        self.projectiles = []
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 300  # Milliseconds between shots

    def draw(self):
        screen.blit(spaceship_img, (self.x, self.y))

    def move(self, direction):
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < WIDTH - self.width:
            self.x += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            projectile = Projectile(self.x + self.width // 2, self.y)
            self.projectiles.append(projectile)
            self.last_shot = now


class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 7

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def move(self):
        self.y -= self.speed


class Alien:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = speed

    def draw(self):
        screen.blit(alien_img, (self.x, self.y))

    def move(self):
        self.y += self.speed

# Game setup
spaceship = Spaceship()
aliens = []

def spawn_aliens(count, speed):
    for _ in range(count):
        x = random.randint(0, WIDTH - 40)
        y = random.randint(-150, -40)
        alien = Alien(x, y, speed)
        aliens.append(alien)

spawn_aliens(5, 2)

score = 0
game_over = False
level = 1

# Main game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move("LEFT")
    if keys[pygame.K_RIGHT]:
        spaceship.move("RIGHT")
    if keys[pygame.K_SPACE]:
        spaceship.shoot()

    # Update and draw projectiles
    for projectile in spaceship.projectiles[:]:
        projectile.move()
        if projectile.y < 0:
            spaceship.projectiles.remove(projectile)
        projectile.draw()

    # Update and draw aliens
    for alien in aliens[:]:
        alien.move()
        if alien.y > HEIGHT:
            game_over = True
        alien.draw()

        # Collision detection
        for projectile in spaceship.projectiles[:]:
            if alien.x < projectile.x < alien.x + alien.width and alien.y < projectile.y < alien.y + alien.height:
                if projectile in spaceship.projectiles:
                    spaceship.projectiles.remove(projectile)
                if alien in aliens:
                    aliens.remove(alien)
                score += 10

    # Level up and increase difficulty
    if not aliens:
        level += 1
        spawn_aliens(5 + level, 2 + level // 2)

    # Draw spaceship
    spaceship.draw()

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Check for game over
    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            aliens = []
            spawn_aliens(5, 2)
            spaceship.projectiles = []
            score = 0
            level = 1
            game_over = False

    pygame.display.flip()
    clock.tick(60)
