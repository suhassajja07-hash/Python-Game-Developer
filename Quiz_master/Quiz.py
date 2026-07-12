import pgzrun

WIDTH = 700
HEIGHT = 550
TITLE = "Ultimate Quiz"

marquee_box = Rect(0, 0, 700, 75)
question_box = Rect(30, 105, 480, 150)
timer_box = Rect(540, 105, 130, 150)
option_box_1 = Rect(30, 285, 225, 100)
option_box_2 = Rect(285, 285, 225, 100)
option_box_3 = Rect(30, 415, 225, 100)
option_box_4 = Rect(285, 415, 225, 100)
skip_box = Rect(540, 285, 130, 230)

option_boxes = [option_box_1, option_box_2, option_box_3, option_box_4]

timer = 15
score = 0
game_over = False

current_statement = []

statements = []

question_number = 0
total_questions = 0


def draw():
    screen.fill("gold")

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(350, 180),
            fontsize=60,
            color="red"
        )

        screen.draw.text(
            f"Final Score : {score}/{total_questions}",
            center=(350, 280),
            fontsize=45,
            color="blue"
        )
        return

    screen.draw.filled_rect(marquee_box, "red")
    screen.draw.filled_rect(question_box, "skyblue")
    screen.draw.filled_rect(timer_box, "green")

    for box in option_boxes:
        screen.draw.filled_rect(box, "purple")

    screen.draw.filled_rect(skip_box, "silver")

    screen.draw.textbox(
        f"Welcome to the Quiz Master. This is Q {question_number} of {total_questions}",
        marquee_box,
        color="white"
    )

    screen.draw.textbox("S\nK\nI\nP", skip_box, color="gold")

    screen.draw.textbox(
        str(timer),
        timer_box,
        color="gold",
        shadow=(0.5, 0.5),
        scolor="black"
    )

    screen.draw.text(
        f"Score: {score}",
        (540, 80),
        fontsize=30,
        color="black"
    )

    screen.draw.textbox(current_statement[0].strip(), question_box, color="gold")
    screen.draw.textbox(current_statement[1].strip(), option_box_1, color="gold")
    screen.draw.textbox(current_statement[2].strip(), option_box_2, color="gold")
    screen.draw.textbox(current_statement[3].strip(), option_box_3, color="gold")
    screen.draw.textbox(current_statement[4].strip(), option_box_4, color="gold")


def update():
    marquee_box.x=marquee_box.x-5
    if marquee_box.right<0:
        marquee_box.left=WIDTH





def update_timer():
    global timer

    if game_over:
        return

    if timer > 0:
        timer -= 1
    else:
        read_next_q()


def on_mouse_down(pos):
    global score

    if game_over:
        return

    if skip_box.collidepoint(pos):
        read_next_q()
        return

    for box in option_boxes:
        if box.collidepoint(pos):

            if option_boxes.index(box) + 1 == int(current_statement[5]):
                print("Correct!")
                score += 1

            read_next_q()
            break


def read_next_q():
    global current_statement
    global timer
    global question_number
    global game_over

    if len(statements) > 0:
        question_number += 1
        current_statement = statements.pop(0).split("|")
        timer = 15
    else:
        game_over = True


def read_question_file():
    global total_questions

    with open(r"Quiz_master\questions.txt", "r") as file:
        content = file.read()

    for line in content.split("\n"):
        if line.strip():
            statements.append(line)

    total_questions = len(statements)


read_question_file()
read_next_q()

clock.schedule_interval(update_timer, 1)

pgzrun.go()
