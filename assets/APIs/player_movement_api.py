from ursina import *
#Setup "inport player_movement_api as pm"

#In update() put "pm.player_movment(player)"
def player_movement(player):
    camera.fov = 90
    camera.y = 0
    player.speed = 18
    #Sprint, Crouch, Zoom
    if held_keys['r']:
        player.speed = 23
    if held_keys['left shift']:
        camera.y = -0.25
        player.speed = 13
    if held_keys['c']:
        camera.fov = 60