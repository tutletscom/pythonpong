#Ping Pong Game

import turtle
import os #Mac, Linux 용
#import winsound #Windows 용

#화면창 크기
src_width = 800
src_height = 600

#키보드 입력에 의한 핑퐁바 이동 픽셀
bar_mov_pixel = 20
#핑퐁바 와 좌우벽의 간격
bar_gab = 50
#핑퐁바 폭
bar_width = 4

#핑퐁볼 이동 x, y 픽셀
ball_mov_pixel = 2

#핑퐁볼 반지름,핑퐁바의 두깨의 반
dot_radius = 10

#점수
score_a = 0
score_b = 0

# 게임 화면창 그리기
scr = turtle.Screen()
scr.title("Ping Pong")
scr.bgcolor("black")
scr.setup(width=src_width, height=src_height)  # w:-400 to 400, h:-300 to 300 
scr.tracer(0)

# 핑퐁 볼 그리기
ball = turtle.Turtle()
ball.speed(0)   #움직이는 속도
ball.shape("circle")
ball.color("red")
ball.penup()    #penup: 이동하는 선을 그리지 않음
ball.goto(0, 0)
ball.dx = ball_mov_pixel
ball.dy = ball_mov_pixel

# 핑퐁 바 그리기
def draw_bar(pos):
    bar = turtle.Turtle()
    bar.speed(0)
    bar.shape("square")
    bar.shapesize(stretch_wid=bar_width, stretch_len=1) #점을 늘려서 핑퐁바로 만들기
    bar.color("white")
    bar.penup()
    bar.goto(pos, 0)
    return bar

# 왼쪽 바
bar_a = draw_bar(-(src_width/2 - bar_gab) ) # -350

# 오른쪽 바
bar_b = draw_bar(src_width/2 - bar_gab ) # 350

# 점수판 그리기
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

## 핑퐁 바 움직이기 ##
def move_bar_a_up():
    bar_a.sety(bar_a.ycor() + bar_mov_pixel) #20픽셀 위로

def move_bar_a_down():
    bar_a.sety(bar_a.ycor() - bar_mov_pixel) #20픽셀 아래로

def move_bar_b_up():
    bar_b.sety(bar_b.ycor() + bar_mov_pixel) #20픽셀 위로

def move_bar_b_down():
    bar_b.sety(bar_b.ycor() - bar_mov_pixel) #20픽셀 아래로

## 키보드 입력받기 ##
scr.listen()
scr.onkeypress(move_bar_a_up, "w")
scr.onkeypress(move_bar_a_down, "s")
scr.onkeypress(move_bar_b_up, "Up")
scr.onkeypress(move_bar_b_down, "Down")

while True:
    ## 화면의 변화를 업데이트 해주기 ##
    scr.update()

    #핑퐁 볼을 대각선으로 움직이기
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #볼이 위아래 벽에 부딪혔을 경우 튕기기
    y_pos = src_height/2 - dot_radius #높이 300 - 10
    x_pos = src_width/2 - dot_radius #폭 400 - 10
    #위벽
    if ball.ycor() > y_pos: 
        ball.sety(y_pos)
        ball.dy *= -1     #y축 이동방향 전환
    #아래벽
    if ball.ycor() < -y_pos: 
        ball.sety(-y_pos)
        ball.dy *= -1
    #왼쪽벽
    if ball.xcor() > x_pos:
        ball.goto(0, 0)   #가운데로 이동
        ball.dx *= -1     #x축 이동방향 전환
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    #오른쪽벽
    if ball.xcor() < -x_pos:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    #bar_b 볼을 튕기기
    # 400 - 50(바와 벽의 간격) - 10(바의 폭/2) - 10(공의 반지름) = 330
    x_pos_bar_min = src_width/2 - bar_gab - dot_radius - dot_radius # 330
    x_pos_bar_max = src_width/2 - bar_gab # 400 - 50 = 350
    y_pos_bar = 40
    if ball.xcor() > x_pos_bar_min and ball.xcor() < x_pos_bar_max and ball.ycor() < (bar_b.ycor() + y_pos_bar) and ball.ycor() > (bar_b.ycor() - y_pos_bar):
        #x좌표 330~350까지를 부딪혔다고 판단하고, 330을 넘었을 경우 
        #표면에서 부딪힌 것처럼 보이기 위해서, x좌표 330로 볼을 이동
        ball.setx(x_pos_bar_min)  
        ball.dx *= -1 #x축 이동방향 전환
        os.system("afplay bounce.wav&") #Mac
        #os.system("aplay bounce.wav&") #Linux
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #Windows

    #bar_a 볼을 튕기기
    if ball.xcor() < -x_pos_bar_min and ball.xcor() > -x_pos_bar_max and ball.ycor() < (bar_a.ycor() + y_pos_bar) and ball.ycor() > (bar_a.ycor() - y_pos_bar):
        ball.setx(-x_pos_bar_min)
        ball.dx *= -1
        os.system("afplay bounce.wav&") #Mac
        #os.system("aplay bounce.wav&") #Linux
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) #Windows