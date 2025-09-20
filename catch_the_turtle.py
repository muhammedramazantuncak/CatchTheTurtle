import turtle
from random import shuffle
from random import randint


# ekran oluşturma

screen = turtle.Screen()
screen.tracer(0) # animasyonları kapatır
def screen_config():
    screen.bgcolor("#123524")
    screen.title("Catch The Turtle")
screen_config()
game_over = False

h = (screen.window_height() / 2)*0.9

# Font oluşturma

def style_maker(size):
    style_ex = ("Arial",size,"normal")
    return style_ex

# Font 1

style = style_maker(20)

# kalem oluşturma

def pen_maker():
    pen_ex = turtle.Turtle()
    pen_ex.color("white")
    pen_ex.pensize(3)
    pen_ex.penup()
    pen_ex.hideturtle()
    return pen_ex

#kalem 1

pen = pen_maker()

# mesaj fonksiyonu

def write_top_message(message): # sürekli bunları yapıcağımız için mesaj fonksiyonu
    pen.clear()
    pen.goto(0,h)
    pen.write(message, font=style, align="center")

# Oyuna Başlama Mesajı ve Geri Sayım

starting_game_timer = 6

def start_game():
    global starting_game_timer
    starting_game_timer -= 1
    if starting_game_timer > 0:
        t.hideturtle()
        write_top_message(f"Game is about to start | Get ready : {starting_game_timer}")
        screen.ontimer(start_game,1000)
    else:
        t.showturtle()
        go_turtle()
        game()
        t.onclick(click)  # bunu fonksiyonun dışında yazman lazım

# Oyun esnasında ekranda gösterilicek yazı

game_timer = 31

def game():
    global game_timer,game_over
    game_timer -= 1
    if game_timer > 0:
        write_top_message(f"Catch The Turtle : {game_timer}")
        screen.ontimer(game,1000)
    else:
        game_over = True
        t.hideturtle()
        screen.update()
        finish_game()

# Oyun bittiğinde gösterilicek yazı

def finish_game():
    global game_timer
    if game_timer == 0:
        write_top_message("Game Over")

# Kaplumbağa oluşturma

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.shapesize(1.6,1.6)
t.color("green")

# Kaplumbağayı rastgele yerlere götürme

coordinat_list = list(range(-300,300,20))
shuffle(coordinat_list)

def go_turtle():
    if not game_over:
        t.goto(coordinat_list[randint(0,len(coordinat_list)-1)],coordinat_list[randint(0,len(coordinat_list)-1)])
        screen.update()
        screen.ontimer(go_turtle,600)

# Kaplumbağaya Basma Ve Bastıkça Puan Kazanma

score = 0
c_style = style_maker(15)
c = pen_maker()

def click(_x,_y):
    global score,game_over
    if not game_over:
        score += 1
    c.clear()
    c.goto(-270, h)
    c.write(f"Your Score : {score}", font=c_style, align="center")

start_game()
screen.update()
screen.mainloop()