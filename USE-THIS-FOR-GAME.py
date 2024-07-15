import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

enemy_pos = pygame.Vector2(screen.get_width(), screen.get_height() / 2)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 0, 128))  

    pygame.draw.circle(screen, (0, 0, 255), player_pos, 40)  # Use RGB tuple for color

    distance = player_pos.distance_to(enemy_pos)
    if distance < 60:
        running = False  # Exit game when player and enemy are close

    direction = player_pos - enemy_pos  # Vector from enemy to player
    direction.normalize_ip()  # Normalize the vector to have unit length
    enemy_pos += direction * 2  # Adjust the speed of the enemy here

    pygame.draw.circle(screen, (255, 0, 0), enemy_pos, 20)  # Use RGB tuple for color

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

