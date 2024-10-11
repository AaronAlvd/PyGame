# This example was taken straight from the pygame docs, feel free to play around with it.
# The best way to get familiar with a new language/library is to play around with code and
# frequently visit its official documentation: https://www.pygame.org/docs/

# this example will display a purple pygame window. You can draw whatever by using the docs ^

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = clock.tick(60) / 1000

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
barrier = pygame.Rect(50, 600, 1180, 20)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, 'red', player_pos, 10)
    pygame.draw.rect(screen, 'black', barrier)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 250 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 250 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 250 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 250 * dt

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
