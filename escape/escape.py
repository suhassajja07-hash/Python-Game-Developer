import pgzrun 
import random

WIDTH=700
HEIGHT=750

TITLE="Escape the maze"

maze=[Rect(25,25,20,650),
      Rect(150,655,525,20),
      Rect(655,25,20,650),
      Rect(45,25,300,20),
      Rect(445,25,215,20),
      Rect(120,100,20,500),
      Rect(220,25,20,450),
      Rect(320,180,20,495),
      Rect(420,25,20,450),
      Rect(520,180,20,495),
      Rect(600,25,20,450),
      Rect(120,100,120,20),
      Rect(340,100,180,20),
      Rect(45,180,120,20),
      Rect(220,180,120,20),
      Rect(440,180,160,20),
      Rect(120,260,220,20),
      Rect(420,260,180,20),
      Rect(45,340,120,20),
      Rect(220,340,220,20),
      Rect(520,340,140,20),
      Rect(120,420,120,20),
      Rect(320,420,220,20),
      Rect(45,500,160,20),
      Rect(260,500,180,20),
      Rect(520,500,140,20),
      Rect(120,580,220,20),
      Rect(420,580,180,20),
      ]


gameover=False
score=0

spaceship=Actor("spaceship")
spaceship.center=(95,670)


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

        for wall in maze:
            if spaceship.colliderect(wall):
                gameover=True

        for dot in dots:
            if spaceship.colliderect(dot):
                dots.remove(dot)
                score=score+1



    

clock.schedule_interval(move,2)

pgzrun.go()

