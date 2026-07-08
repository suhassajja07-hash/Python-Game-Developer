import pgzrun

file = open(r"numbers\numbers.txt", "r")
content = file.read()
file.close()

total = 0

for number in content.split():
    total = total + int(number)

WIDTH = 400
HEIGHT = 200

def draw():
    screen.clear()
    screen.draw.text("Sum = " + str(total), (120, 90), color="white")

pgzrun.go()