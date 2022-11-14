from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

def update():
    camera.fov = 90
    camera.y = 0
    player.speed = 15
    #Sprint, Crouch, Zoom
    if held_keys['r']:
        player.speed = 20
    if held_keys['left shift']:
        camera.y = -0.25
        player.speed = 10
    if held_keys['c']:
        camera.fov = 60

def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        EditorCamera()

terrain = Entity(model=Terrain('heightmap_1', skip=8), scale=(500,10,500), texture='grass', collider='mesh', y=-3)

player = FirstPersonController(y=1)

test = Entity(model='quad', texture='assets/screen.png', scale_y=5, y=3)
test.scale_x = (2*test.scale_y)


app.run()