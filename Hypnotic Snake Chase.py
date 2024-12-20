import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game: Follow the Cursor")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake settings
snake_length = 10
snake_speed = 5
cube_size = 20
snake_positions = [(WIDTH // 2, HEIGHT // 2)]
rotation_angle = 0

# Food settings
food_position = (random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
food_size = 15

# Function to draw the snake
def draw_snake(positions, angle):
    for i, pos in enumerate(positions):
        x, y = pos
        rotated_cube = pygame.Surface((cube_size, cube_size))
        rotated_cube.fill(random.choice([RED, GREEN, BLUE]))
        rotated_cube_rotated = pygame.transform.rotate(rotated_cube, angle + i * 10)
        screen.blit(rotated_cube_rotated, (x - cube_size // 2, y - cube_size // 2))

# Function to move the snake
def move_snake(snake_positions, target):
    head_x, head_y = snake_positions[0]
    target_x, target_y = target

    angle = math.atan2(target_y - head_y, target_x - head_x)
    dx = math.cos(angle) * snake_speed
    dy = math.sin(angle) * snake_speed

    new_head = (head_x + dx, head_y + dy)
    snake_positions = [new_head] + snake_positions[:-1]
    return snake_positions

# Function to check collision
def check_collision(pos1, pos2, size):
    return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1]) < size

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the cursor position
    cursor_position = pygame.mouse.get_pos()

    # Move the snake
    snake_positions = move_snake(snake_positions, cursor_position)

    # Check for food collision
    if check_collision(snake_positions[0], food_position, cube_size):
        food_position = (random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
        snake_positions.append(snake_positions[-1])

    # Draw food
    pygame.draw.circle(screen, WHITE, food_position, food_size)

    # Draw the snake
    draw_snake(snake_positions, rotation_angle)

    # Rotate the snake cubes
    rotation_angle += 5

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
