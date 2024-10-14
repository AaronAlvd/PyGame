# Example file showing a fish appear at a random height,
# either left or right edge of screen, and move at a fixed rate
# across the screen 
import pygame
import sys

pygame.init()

size = width, height = 1280, 720
waterLevel = height * 0.25
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 60
dt = 0

running = True

fish = pygame.image.load("fish.png")
fish = pygame.transform.scale(fish, (200, 100))

fishRect = fish.get_rect()
fishRect.width = 200
fishRect.height = 100
fishRect.center = (0, waterLevel * 1.5)

fishYSpeed = 1
fishSpeed = [1, fishYSpeed]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Start fish movement
    fishRect = fishRect.move(fishSpeed)

    # If fish touches water level or bottom of screen, invert y speed
    if fishRect.centery == waterLevel + fishRect.height / 2 or fishRect.centery == height - fishRect.height / 2:
        fishYSpeed = -fishYSpeed
        fishSpeed[1] = fishYSpeed

    # If fish touches other side, start over
    if fishRect.centerx == width:
        fishRect.centerx = 0

    screen.fill("white")
    screen.blit(fish, fishRect)

    pygame.display.flip()
    
    # limit FPS
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics
    dt = clock.tick(fps) / 1000

pygame.quit()