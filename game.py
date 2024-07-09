import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.Font(None, 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.speed = 5
        self.coins = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randint(0, SCREEN_WIDTH)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect(center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

# Create sprite groups
player = Player()
player_group = pygame.sprite.Group(player)

enemy_group = pygame.sprite.Group()
for _ in range(10):
    enemy_group.add(Enemy())

bullet_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
for _ in range(5):
    coin_group.add(Coin())

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullet_group.add(bullet)

    # Update
    player_group.update()
    enemy_group.update()
    bullet_group.update()
    coin_group.update()

    # Check collisions
    if pygame.sprite.spritecollideany(player, enemy_group):
        running = False
    for bullet in bullet_group:
        enemies_hit = pygame.sprite.spritecollide(bullet, enemy_group, True)
        for enemy in enemies_hit:
            bullet.kill()
            enemy_group.add(Enemy())

    coins_collected = pygame.sprite.spritecollide(player, coin_group, True)
    for coin in coins_collected:
        player.coins += 1
        coin_group.add(Coin())

    # Draw
    screen.fill(BLACK)
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)
    coin_group.draw(screen)

    # Display coin count
    coin_text = font.render(f"Coins: {player.coins}", True, WHITE)
    screen.blit(coin_text, (10, 10))

    # Item shop (basic implementation)
    if player.coins >= 10:
        player.coins -= 10
        player.speed += 1
        print("Speed upgraded!")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

