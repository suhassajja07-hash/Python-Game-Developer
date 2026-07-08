import pgzrun
WIDTH=700
HEIGHT=550
TITLE="Ultimate Quiz"
marquee_box=Rect(0,0,700,75)
question_box=Rect(30,105,480,150)
timer_box=Rect(540,105,130,150)
option_box_1=Rect(30,285,225,100)
option_box_2=Rect(285,285,225,100)
option_box_3=Rect(30,415,225,100)
option_box_4=Rect(285,415,225,100)
skip_box=Rect(540,285,130,230)

timer=15
current_statement=""

option_boxes=[option_box_1,option_box_2,option_box_3,option_box_4]
statements=[]
def draw():
    screen.fill("gold")
    screen.draw.filled_rect(marquee_box,"red")
    screen.draw.filled_rect(question_box,"sky blue")
    screen.draw.filled_rect(timer_box,"green")
    for box in option_boxes:
        screen.draw.filled_rect(box,"purple")
    screen.draw.filled_rect(skip_box,"silver")
    screen.draw.textbox("S\nK\nI\nP",skip_box,color="gold")
    screen.draw.textbox(str(timer),timer_box,color="gold",shadow=(0.5,0.5),scolor="black")
    screen.draw.textbox(current_statement[0].strip(),question_box,color="gold")
    screen.draw.textbox(current_statement[1].strip(),option_box_1,color="gold")
    screen.draw.textbox(current_statement[2].strip(),option_box_2,color="gold")
    screen.draw.textbox(current_statement[3].strip(),option_box_3,color="gold")
    screen.draw.textbox(current_statement[4].strip(),option_box_4,color="gold")


def update():
    pass


def update_timer():
    global timer
    if timer>0:
        timer=timer-1 
    else:
        read_next_q()
    

def on_mouse_down(pos):
    if skip_box.collidepoint(pos):
        read_next_q()
    
    for box in option_boxes:
        if box.collidepoint(pos):
           
            if option_boxes.index(box)+1==int(current_statement[5]):
                print("You are correct!")
            
            read_next_q()


    
def read_next_q():
    global current_statement, timer
    current_statement=statements.pop(0).split("|")
    timer=15
    
        
def read_question_file():
    file=open(r"Quiz_master\questions.txt","r")
    content=file.read()
   
    for line in content.split("\n"):
        statements.append(line)
    file.close()
    print(statements)

read_question_file()
read_next_q()
clock.schedule_interval(update_timer,1)
pgzrun.go()

