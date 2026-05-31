import pgzrun
import random

WIDTH=700
HEIGHT=700
TITLE="Connect the satellites"

num_of_satellites=7
satellites={}

for i in range(num_of_satellites):
    actor=Actor("satellite") 
    actor.x=random.randint(50,HEIGHT-50)
    actor.y=random.randint(50,HEIGHT-50)
    satellites[i+1]=actor
print(satellites)

def draw():
    screen.blit("background",(0,0))
    for i in satellites:
        satellites[i].draw()
        screen.draw.text(str(i),satellites[i].pos)


pgzrun.go()
    