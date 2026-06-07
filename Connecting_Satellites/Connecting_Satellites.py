import pgzrun
import random

WIDTH=700
HEIGHT=700
TITLE="Connect the satellites"

num_of_satellites=7
satellites={}
lines=[]
current_satellite=1

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
        screen.draw.text(str(i),(satellites[i].x-25,satellites[i].y-25))
    for line in lines:
        screen.draw.line(line[0],line[1],"white")

def update():
    pass
    

def on_mouse_down(pos):
    global lines, current_satellite
    if satellites[current_satellite].collidepoint(pos):
        if current_satellite !=1:
            starting_point=satellites[current_satellite].pos
            endpoint=satellites[current_satellite-1].pos
            lines.append([starting_point,endpoint])
        current_satellite=current_satellite+1
    else:
        current_satellite=1
        lines=[]




pgzrun.go()
    