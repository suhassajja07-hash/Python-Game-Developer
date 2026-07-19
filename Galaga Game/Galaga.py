import pgzrun

WIDTH = 700
HEIGHT = 700
TITLE = "The Galaga Game"

game_state = "start"

score = 0

direction=1

end_message=""

ship = Actor("ship")
ship.pos = (WIDTH/2, HEIGHT-50)

bullets = []
enemies = []
y = 50

for i in range(5):
    row_of_enemy = []
    x = 50

    for e in range(5):
        enemy = Actor("enemy")
        enemy.y = y
        enemy.x = x

        row_of_enemy.append(enemy)

        x = x + 60

    enemies.append(row_of_enemy)
    y = y + 50

print(enemies)


def draw():
    screen.fill("skyblue")

    if game_state == "start":
        screen.draw.text(
            "WELCOME TO THE GALAGA GAME",
            center=(WIDTH/2, HEIGHT/2),
            fontsize=45,
            color="gold"
        )

        screen.draw.text(
            "Press any key to continue",
            center=(WIDTH/2, HEIGHT/2+50),
            fontsize=15,
            color="red"
        )


    elif game_state == "play":

        ship.draw()

        for row in enemies:
            for enemy in row:
                enemy.draw()

        for bullet in bullets:
            bullet.draw()

        screen.draw.text(
            "Score: " + str(score),
            topright=(680, 20),
            fontsize=30,
            color="black"
        )
    elif game_state=="over":
        screen.draw.text(end_message,center=(WIDTH/2,HEIGHT/2),fontsize=50,color="gold")



def on_key_down(key):
    global game_state

    if game_state == "start":
        game_state = "play"

    elif game_state == "play":

        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullet.x = ship.x
            bullet.y = ship.top

            bullets.append(bullet)


def update():
    global direction, score, end_message, game_state
    move_down=False

    if game_state == "play":

        if keyboard.left:
            ship.x = ship.x - 3

        elif keyboard.right:
            ship.x = ship.x + 3

        if ship.x <= 0:
            ship.x = WIDTH

        elif ship.x >= WIDTH:
            ship.x = 0

        for bullet in bullets:
            bullet.y = bullet.y - 5

            if bullet.y < 0:
                bullets.remove(bullet)


        if any(enemies):
            if enemies[0][-1].x>=WIDTH or enemies[0][0].x<=0:
                direction=direction*-1   
                move_down=True    
        else:
            game_state="over"
            end_message="Well done you have won!!!"

        for row in enemies:
            for enemy in row:
                if enemy.colliderect(ship):
                    game_state="over"
                    end_message="Sorry you have lost try again!!!"


        for row in enemies:
            for enemy in row:
                enemy.x=enemy.x+2*direction
                if move_down:
                    enemy.y=enemy.y+100


    for i in range(5):
        for enemy in enemies[i]:
            for bullet in bullets:
                if enemy.colliderect(bullet):
                    sounds.eep.play()
                    enemies[i].remove(enemy)
                    bullets.remove(bullet)
                    score=score+1



                

pgzrun.go()