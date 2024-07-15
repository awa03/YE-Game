import pygame

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

enemy_pos = pygame.Vector2(screen_width, screen_height / 2)
player_pos = pygame.Vector2(screen_width / 2, screen_height / 2)
player_radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 0, 128))  

    pygame.draw.circle(screen, (0, 0, 255), player_pos, player_radius)  # Draw player

    # Check collision with enemy
    distance = player_pos.distance_to(enemy_pos)
    if distance < player_radius + 20:
        running = False  # Exit game when player and enemy collide

    direction = player_pos - enemy_pos
    direction.normalize_ip()
    enemy_pos += direction * 2

    pygame.draw.circle(screen, (255, 0, 0), enemy_pos, 20)  # Draw enemy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    player_pos.x = max(player_radius, min(player_pos.x, screen_width - player_radius))
    player_pos.y = max(player_radius, min(player_pos.y, screen_height - player_radius))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
