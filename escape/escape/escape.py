import pgzrun 
import random

WIDTH=700
HEIGHT=750

TITLE="Escape the maze"

maze=[
    Rect(25, 25, 20, 650),
    Rect(45, 25, 550, 20),
    Rect(655, 25, 20, 650),
    Rect(115, 655, 550, 20),

    Rect(100, 100, 20, 300),
    Rect(100, 100, 200, 20),

    Rect(200, 200, 200, 20),
    Rect(380, 100, 20, 120),

    Rect(300, 200, 20, 250),
    Rect(300, 430, 180, 20),

    Rect(480, 200, 20, 250),
    Rect(480, 200, 120, 20),

    Rect(580, 300, 20, 200),
    Rect(500, 500, 100, 20)
      ]


gameover=False
score=0

spaceship=Actor("spaceship1")
spaceship.center=(85,670)


spiked_line=Actor("spiked_line")
spiked_line.center=(WIDTH/2,HEIGHT-10)


dots=[]

for i in range(30):
    dot=Actor("dot")
    dot.x=random.randint(25,675)
    dot.y=random.randint(25,675)

    for wall in maze:
        while dot.colliderect(wall):
            dot.x=random.randint(25,675)
            dot.y=random.randint(25,675)

    dots.append(dot)

def draw():
    screen.fill("black")
    spaceship.draw()
    spiked_line.draw()


    for dot in dots:
        dot.draw()
    

    for wall in maze:
        screen.draw.filled_rect(wall,"blue")

    if gameover==True:
        screen.fill("silver")
        screen.draw.text(f"Gameover, your score is {score}",center=(WIDTH/2,HEIGHT/2),fontsize=50,color="gold")




def move():
    spiked_line.y=spiked_line.y-5

def update():
    global gameover, score
    if not gameover:
        if keyboard.left:
            spaceship.x -= 3
        if keyboard.right:
            spaceship.x += 3
        if keyboard.up:
            spaceship.y -= 3
        if keyboard.down:
            spaceship.y += 3

        # for wall in maze:
        #    if spaceship.colliderect(wall):
        #        gameover=True

        for dot in dots:
            if spaceship.colliderect(dot):
                dots.remove(dot)
                score=score+1



    

clock.schedule_interval(move,2)

pgzrun.go()

