# This file will handle all of the movements.

import pygame

def handle_user_movement_WASD(keys_pressed, obj, velocity):

    '''Take WASD controls and adjust pos of obj by velocity '''
    if keys_pressed[pygame.K_a]: # LEFT
        obj.x -= velocity
    if keys_pressed[pygame.K_d]:  # RIGHT
        obj.x += velocity
    if keys_pressed[pygame.K_w]: # UP
        obj.y -= velocity
    if keys_pressed[pygame.K_s]: # DOWN
        obj.y += velocity

def handle_user_movement_arrow(keys_pressed, obj, velocity):

    '''Take arrow controls and adjust pos of obj by velocity '''
    if keys_pressed[pygame.K_LEFT]: # LEFT
        obj.x -= velocity
    if keys_pressed[pygame.K_RIGHT]: # RIGHT
        obj.x += velocity
    if keys_pressed[pygame.K_UP]: # UP
        obj.y -= velocity
    if keys_pressed[pygame.K_DOWN]: # DOWN
        obj.y += velocity
