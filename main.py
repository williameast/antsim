#!/usr/bin/env python3

import os
import pygame
import movement

# Screen settings
WIDTH, HEIGHT = 900, 500        # Screen Height and width constants
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # set width and height

FPS = 60                        # frames per second rendered.
VEL = 5                         # speed of movement




# If we want to produce an object on the screen, such as a border.
# BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# Define Colours

WHITE = (225, 255, 255)
BLACK = (0,0,0)

# Define the size of ants

OBJ_WIDTH, OBJ_HEIGHT = 20,20  # the size of the objects we spawn.

ANT_IMAGE = pygame.image.load(
    os.path.join('assets', 'Ant.png')
)

# Determine the size of the ant PNG we load in.
ANT = pygame.transform.scale(ANT_IMAGE, (OBJ_WIDTH, OBJ_HEIGHT))

def draw_window(obj):              # draw objects
    WIN.fill(WHITE)
    # WIN.blit(LIL_GUY, (lil.x, lil.y))
    # WIN.blit(ENEMY, (enemy.x, enemy.y))
    # pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(ANT, (obj.x, obj.y))
    pygame.display.update()


def main():
    # lil = pygame.Rect(100, 300, OBJ_WIDTH, OBJ_HEIGHT)
    # enemy = pygame.Rect(100, 100, OBJ_WIDTH, OBJ_HEIGHT)
    # Draw a rectangle the size of the ant.
    # location.x location.y size.x size,y
    ant = pygame.Rect(100, 300, OBJ_WIDTH, OBJ_HEIGHT)

    # this "ticks" the internal clock, so the runspeed is uniform across
    # different machines.

    clock = pygame.time.Clock()

    # This is the truth condition for keeping the while loop open.
    run = True

    while run:
        clock.tick(FPS)         # keep framerate capped at 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Get the keys that are pressed.
        keys_pressed = pygame.key.get_pressed()

        movement.handle_user_movement_WASD(keys_pressed, ant, VEL)

        draw_window(obj=ant) # send lil and enemy objects to drawer
    pygame.quit()

if __name__  == "__main__":
    main()
