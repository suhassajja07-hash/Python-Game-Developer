import pgzrun 
import random

WIDTH=700
HEIGHT=600
TITLE="Shoot the alien"

alien=Actor("alien")
alien.x=random.randint(40,WIDTH-40)
alien.y=random.randint(40,HEIGHT-40)

message=TITLE

def draw():
    screen.fill("White")
    alien.draw()
    screen.draw.text(message,center=(WIDTH/2,30),color="blue",fontsize=40)


    

def on_mouse_down(pos):
    global message
    print(pos)
    if alien.collidepoint(pos):
        alien.x=random.randint(40,WIDTH-40)
        alien.y=random.randint(40,HEIGHT-40)
        message="Good Shot!!!"
    else:
        message="Unlucky you missed!"
        







pgzrun.go()


