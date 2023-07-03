import random

import pygame

# Initializer pygame
pygame.init()

# Create console

console = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ovni.png")
pygame.display.set_icon(icon)


# player
image = pygame.image.load("rocket.png")
player_x = 368
player_y = 536
movement = 0

# player
image_enemy = pygame.image.load("alien.png")
enemy_x = random.randint(0,736)
enemy_y = random.randint(50,200)
movement_enemy_x = 0.3
movement_enemy_y = 30



def player(x, y):
    console.blit(image, (x, y))


def enemy(x, y):
    console.blit(image_enemy, (x, y))


play = True

while play:

    # RGB
    console.fill((205, 144, 228))

    # iteration events
    for event in pygame.event.get():

        # quit event
        if event.type == pygame.QUIT:
            play = False

        # Arrows event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = -0.3
            if event.key == pygame.K_RIGHT:
                movement = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement = 0

    # ubication modify
    player_x += movement

    if player_x <= 0:
        player_x = 0

    elif player_x >= 736:
        player_x = 736

    enemy_x += movement_enemy_x

    if enemy_x <= 0:
        movement_enemy_x = 0.3
        enemy_y += movement_enemy_y
    elif enemy_x >= 736:
        movement_enemy_x = -0.3
        enemy_y += movement_enemy_y

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # Update
    pygame.display.update()
