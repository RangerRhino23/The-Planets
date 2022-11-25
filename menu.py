from ursina import *

app = Ursina()
background = Entity(model='quad', texture='assets/space.png', z=1, scale=(17,10))

def update():
    pass

def input(key):
    if key == 'q':
        quit()

def open_spaceship():
    os.startfile('spaceship.py')
    quit()

def quit_game():
    quit()

logo = Entity(model='quad', texture='assets/logo.png', scale_x=6, scale_y=3, y = 0.1)

start_button = Button(scale=(.875*.24, .05), x=(logo.x-0.035), y=(logo.y-0.25), text='Start Game', on_click=open_spaceship)
quit_button = Button(scale=(.875*.24, .05), x=(start_button.x), y=(start_button.y-0.08), text='Quit', on_click=quit_game)

app.run()