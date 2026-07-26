import pgzrun 

WIDTH=700
HEIGHT=700

TITLE="Escape the maze"

maze=[Rect(25,25,20,650),
      Rect(150,655,525,20),
      Rect(655,25,20,650),
      Rect(45,25,300,20),
      Rect(445,25,215,20),

      ]

spaceship=Actor("spaceship")
spaceship.center=(95,670)


def draw():
    screen.fill("black")
    spaceship.draw()
    

    for wall in maze:
        screen.draw.filled_rect(wall,"blue")


def update():
    pass

pgzrun.go()

