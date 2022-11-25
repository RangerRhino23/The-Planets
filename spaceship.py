from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import assets.APIs.player_movement_api as pma

app = Ursina()

def update():
    pma.player_movement(player)

def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        print(player.position)
    if key == 'f':
        EditorCamera()



#Temp
space_base = Entity(model='assets/models/space_base.obj', scale=0.50, collider='mesh', position=(-132,5,44), shader=lit_with_shadows_shader)

player = FirstPersonController(position=(-115,4,67))


pivot = Entity()
DirectionalLight(parent=pivot, position=(-151, 50, 148), shadows=True, rotation=(45, -45, 45))

app.run()

