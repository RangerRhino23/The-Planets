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
terrain = Entity(model=Terrain('heightmap_1', skip=8), scale=(500,10,500), texture='grass', collider='mesh', y=-3, shader=lit_with_shadows_shader)
base = Entity(model='assets/models/base.obj', scale=0.50, collider='mesh', position=(-132,5,44), shader=lit_with_shadows_shader)
water = Entity(model='cube', color=color.blue, scale=(500,1,500), y=-1.5)

player = FirstPersonController(position=(-130,4,120))


pivot = Entity()
DirectionalLight(parent=pivot, position=(-151, 10, 148), shadows=True, rotation=(45, -45, 45))

app.run()