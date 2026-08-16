import os 
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,50"

import pgzrun 
import random


WIDTH=700
HEIGHT=750

TITLE="Escape the maze"



exit=Rect(WIDTH-100,15,40,20 )

maze=[
    Rect(25, 25, 20, 650),
    Rect(45, 25, 535, 20),
    Rect(655, 25, 20, 650),
    Rect(120, 655, 545, 20),

    Rect(100, 130, 20, 300),
    Rect(100, 130, 200, 20),

    Rect(200, 250, 200, 20),
    Rect(380, 130, 20, 120),

    Rect(300, 250, 20, 200),
    Rect(300, 380, 180, 20),

    Rect(480, 200, 20, 250),
    Rect(480, 200, 120, 20),

    Rect(580, 300, 20, 200),
    

    Rect(150,550,300,20)
      ]

won=False
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




    if gameover==True:
        screen.fill("silver")
        if won==True:           
            screen.draw.text(f"You have won the game, your score is {score}",center=(WIDTH/2,HEIGHT/2),fontsize=50,color="navy")
        else:
            screen.draw.text(f"You have lost the game, your score is {score},",center=(WIDTH/2,HEIGHT/2),fontsize=50,color="navy")
            screen.draw.text(f"you did not collect enough orbs",center=(WIDTH/2,HEIGHT/2+30),fontsize=50,color="navy")
                

    else:
        screen.fill("black")
        spaceship.draw()
        spiked_line.draw()
    
    
        for dot in dots:
            dot.draw()
        
    
        for wall in maze:
            screen.draw.filled_rect(wall,"blue")


        screen.draw.textbox("EXIT",exit,color="red", center=(WIDTH-75,15))
        screen.draw.text(f"score:{score}",color="green", center=(50,20))

    





def move():
    spiked_line.y=spiked_line.y-8

def update():
    global gameover, score, won
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


        if spaceship.colliderect(spiked_line):
            gameover=True
        
        

        for dot in dots:
            if spaceship.colliderect(dot):
                dots.remove(dot)
                score=score+1


        if spaceship.colliderect(exit):
            if score>=15:
                won=True
            gameover=True


    

clock.schedule_interval(move,2)

pgzrun.go()

