import random
import math
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

fuente = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10
points = 0

fuente_final = pygame.font.Font("freesansbold.ttf", 40)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    console.blit(mi_fuente_final, (60,200))

# enemy
image_enemy = []
enemy_x = []
enemy_y = []
movement_enemy_x = []
movement_enemy_y = []
quantity = 6

for e in range(quantity):
    image_enemy.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    movement_enemy_x.append(0.5)
    movement_enemy_y.append(50)

# bullet
image_bullet = pygame.image.load("bala.png")
bullet_x = 0
bullet_y = 500
movement_bullet_x = 0
movement_bullet_y = 1
bullet_visible = False


def player(x, y):
    console.blit(image, (x, y))


def enemy(x, y, ene):
    console.blit(image_enemy[ene], (x, y))


def bullet(x, y):
    console.blit(image_bullet, (x + 16, y + 10))
    global bullet_visible
    bullet_visible = True


def coli(x1, y1, x2, y2):
    d = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if d < 27:
        return True
    else:
        return False

def show_points(x,y):
    texto = fuente.render(f"Points: {points}", True, (255, 255, 255))
    console.blit(texto, (x, y))


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
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movement = 0

    # ubication modify
    player_x += movement

    if player_x <= 0:
        player_x = 0

    elif player_x >= 736:
        player_x = 736

    for e in range(quantity):

        if enemy_y[e] > 500:
            for k in range(quantity):
                enemy_y[k] = 1000
            texto_final()
            break
        enemy_x[e] += movement_enemy_x[e]

        if enemy_x[e] <= 0:
            movement_enemy_x[e] = 0.3
            enemy_y[e] += movement_enemy_y[e]
        elif enemy_x[e] >= 736:
            movement_enemy_x[e] = -0.3
            enemy_y[e] += movement_enemy_y[e]

        colision = coli(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if colision:
            bullet_y = 500
            bullet_visible = False
            points += 1

            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(50, 200)

        enemy(enemy_x[e], enemy_y[e], e)

    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False

    if bullet_visible:
        bullet(bullet_x, bullet_y)
        bullet_y -= movement_bullet_y

    player(player_x, player_y)
    show_points(text_x, text_y)

    # Update
    pygame.display.update()
