import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Constants
gravity = 700  # Gravity force
velocity = 0  # Initial vertical velocity
dt = clock.tick(60) / 1000  # Time delta

# Player hitbox (rectangle)
player_hitBox = pygame.Rect(600, 300, 20, 20)  # Initial position and size (x, y, width, height)

# Ground level
ground_level = 590

# Platforms 
platforms = [
    pygame.Rect(900, 500, 150, 20),  # Platform 1: (x, y, width, height)
    pygame.Rect(700, 400, 40, 20),  # Platform 2: (x, y, width, height)
    pygame.Rect(500, 300, 100, 20),  # Platform 3: (x, y, width, height)
    pygame.Rect(400, 200, 60, 20),  # Platform 4: (x, y, width, height)
    pygame.Rect(300, 100, 70, 20),  # Platform 5: (x, y, width, height)
]


while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the player hitbox based on keys pressed
    if keys[pygame.K_LEFT]:
        player_hitBox.x -= 200 * dt  # Move left
    if keys[pygame.K_RIGHT]:
        player_hitBox.x += 200 * dt  # Move right
    if keys[pygame.K_UP] and velocity == 0:
        velocity = -400  # Jump

    # Apply gravity
    velocity += gravity * dt  # Gravity adds to velocity every frame
    player_hitBox.y += velocity * dt  # Update player position

    # Check if the player hitbox hits the ground
    if player_hitBox.bottom >= ground_level:
        player_hitBox.bottom = ground_level  # Set the bottom of the hitbox to ground level
        velocity = 0  # Stop vertical movement
    
    # Prevent the player from going off the left edge of the screen
    if player_hitBox.left < 0:
        player_hitBox.left = 0  # Reset to left edge

    # Prevent the player from going off the right edge of the screen
    if player_hitBox.right > screen.get_width():
        player_hitBox.right = screen.get_width()  # Reset to right edge

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw player hitbox (rectangle) and ground (barrier)
    for platform in platforms: 
        pygame.draw.rect(screen, 'black', platform)

        if player_hitBox.colliderect(platform):
            if player_hitBox.bottom >= platform.top and velocity > 0:
                player_hitBox.bottom = platform.top
                velocity = 0

    pygame.draw.rect(screen, 'red', player_hitBox, 10)  # Draw the player hitbox
    pygame.draw.rect(screen, 'black', (0, ground_level, 1280, 20))  # Draw the ground

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Cap FPS
    dt = clock.tick(60) / 1000

pygame.quit()
