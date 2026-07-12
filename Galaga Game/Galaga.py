import pgzrun

WIDTH=700
HEIGHT=700
TITLE="The Galaga Game"

game_state="start"

ship=Actor("ship")
ship.pos=(WIDTH/2,HEIGHT-50)

def draw():
    screen.fill("sky blue")
    if game_state=="start":
        screen.draw.text("WELCOME TO THE GALAGA GAME",center=(WIDTH/2,HEIGHT/2),fontsize=45, color="gold")
        screen.draw.text("Press any key to continue",center=(WIDTH/2,HEIGHT/2+50),fontsize=15, color="red")

    elif game_state=="play":
        ship.draw()
        
        



def on_key_down(key):
    global game_state
    if game_state=="start":
        game_state="play"





pgzrun.go()