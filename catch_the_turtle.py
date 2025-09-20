import turtle
from random import randint
from random import shuffle

# ekran oluşturma

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Catch The Turtle")
screen.tracer(0) # animasyonları kapatır

# mesaj fonksiyonu

def write_top_message(message): # sürekli bunları yapıcağımız için mesaj fonksiyonu
    pen1.clear()
    pen1.penup()
    pen1.goto(0,380)
    pen1.pendown()
    pen1.write(message, font=style1, align="center")
    pen1.hideturtle()


# kalem 1

pen1 = turtle.Turtle()
pen1.pensize(3)
pen1.speed(0)

# sayaç

starting_game = 6
timer = 31
style1 = ("Courier",30,"bold")

def start_game():
    global starting_game
    starting_game -= 1
    if starting_game > 0:
        screen.reset()
        write_top_message(f"Game is about to start | Get ready {starting_game}")
        screen.ontimer(start_game,1000)
    else:
        countdown()
        goturtle()
def countdown():
    global timer
    timer -= 1
    if timer > 0:
        pen1.reset()
        write_top_message(f"Countdown : {timer}")
        screen.ontimer(countdown,1000)
    else:
        finish_game()
def finish_game():
    global timer
    if timer == 0:
        write_top_message(f"Time Is Up :)")
        screen.ontimer(finish_game, 1000)

def goturtle():
    global timer
    if timer > 0:
        turtlecatch()
        pen2.onclick(click)
        pen3.hideturtle()
        screen.update()
        screen.ontimer(goturtle,600)


# kaplumbağa oluşturma

coordinat_list = list(range(-350,360,30))
shuffle(coordinat_list)

pen2 = turtle.Turtle()
pen2.shape("turtle")


def turtlecatch():
    pen2.fillcolor("green")
    pen2.shapesize(2)
    pen2.penup()
    pen2.goto(coordinat_list[randint(0,len(coordinat_list)-1)],coordinat_list[randint(0,len(coordinat_list)-1)])

# click oluşturma

style2 = ("Courier",20,"bold")
written = 0

pen3 = turtle.Turtle()

def click(_x,_y):
    global written,timer
    if timer > 0:
        written += 1
        pen3.clear()
        pen3.penup()
        pen3.goto(-650,385)
        pen3.pendown()
        pen3.write(f"Your Score : {written}",font=style2,align="center")

screen.update()
start_game()
screen.mainloop()