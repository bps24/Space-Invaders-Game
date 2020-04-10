import turtle
import os
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("backyyy111.gif")

turtle.register_shape("player111.gif")
turtle.register_shape("enemy111.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,280)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()





player = turtle.Turtle()
player.setposition(0,-250)
player.settiltangle(90)
player.color('blue')
player.shape('player111.gif')
player.penup()
player.speed(0)

playerspeed = 15




enemyspeed = 8
enemydrop = 30

numberofenemies = 5
enemies = []

for i in range(numberofenemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
    enemy.color('red')
    enemy.shape('enemy111.gif')
    enemy.penup()
    enemy.speed(0)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.settiltangle(90)
bullet.shapesize(0.5,0.5)

booler =True
bulletspeed = 45
bulletstate = 'ready'

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate =='ready':
        os.system("afplay shoot.wav&")
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y+10)
        bullet.showturtle()

def is_collision(t1,t2):
    d = ((t1.xcor()-t2.xcor())**2+(t1.ycor()-t2.ycor())**2)**0.5
    if d < 25:
        return True
    else:
        return False

def gameover():
    player.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    booler = False
    games = turtle.Turtle()
    games.speed(0)
    games.color('white')
    games.penup()
    games.setposition(0,0)
    gamestring = "Game Over\n Score: %s" % score
    games.write(gamestring, False, align='center', font=('Arial', 60, 'normal'))
    games.hideturtle()
    bullet.hideturtle()





turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while booler:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor()>270 or enemy.xcor()<-270:
            for enemy in enemies:
                y = enemy.ycor()
                y -= enemydrop
                enemy.sety(y)
            enemyspeed *=-1
            break

        if is_collision(bullet, enemy):
            bulletstate='ready'
            os.system("afplay invaderkilled.wav&")
            bullet.hideturtle()
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            score+=10
            score_string = "Score: %s" % str(score)
            score_pen.clear()
            score_pen.write(score_string, False, align='left', font=('Arial', 14, 'normal'))
            break

        if enemy.ycor()<-250:
            gameover()

    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = 'ready'

    

delay = input("press enter to finish")

