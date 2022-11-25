from ursina import *

app = Ursina()
#Sky(texture='assets/menu.png')
sky = Entity(model='quad', texture='assets/space.png', z=1, scale=(17,10))

def update():
    pass

def input(key):
    if key == 'q':
        quit()

def select_level():
    pass

def quit_game():
    app.closeWindow()

logo = Entity(model='quad', texture='assets/earth.png', scale=(4,2), y = 0.1)

start_button = Button(scale=(.875*.24, .05), x=(logo.x-0.05), y=(logo.y-0.2), text='Start Game', on_click=select_level)
quit_button = Button(scale=(.875*.24, .05), x=(start_button.x), y=(start_button.y-0.06), text='Quit', on_click=quit_game)

app.run()