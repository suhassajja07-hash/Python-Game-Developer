import pgzrun
WIDTH=700
HEIGHT=1000
TITLE="Ultimate Quiz"
marquee_box=Rect(0,0,700,50)


statements=[]
def draw():
    screen.fill("blue")
    screen.draw.filled_rect(marquee_box,"red")
        
def read_question_file():
    file=open(r"Quiz_master\questions.txt","r")
    content=file.read()
   
    for line in content.split("\n"):
        statements.append(line)
    file.close()
    print(statements)

read_question_file()

pgzrun.go()

