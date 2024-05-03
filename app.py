#import turtle module
import turtle

#initalize screen
wind=turtle.Screen()
#disaple resizeable 
wind.cv._rootwindow.resizable(False, False)
#screen title
wind.title("Ping Pong")
#screen color
wind.bgcolor("black")
#screen size
wind.setup(width=800,height=600)
# stop auto update screen
wind.tracer(0)



#palyer 1
player1=turtle.Turtle()#initalize turtle oblect
player1.speed(0)#speed of animation
player1.shape("square")#set the shape
player1.color("red")#shape color
player1.penup()#stop drawing lines
player1.goto(-350,0)#set the position
player1.shapesize(stretch_wid=6,stretch_len=1)#strech the shape
#palyer 2
player2=turtle.Turtle()#initalize turtle oblect
player2.speed(0)#speed of animation
player2.shape("square")#set the shape
player2.color("blue")#shape color
player2.penup()#stop drawing lines
player2.goto(350,0)#set the position
player2.shapesize(stretch_wid=6,stretch_len=1)#strech the shape
#ball
ball = turtle.Turtle()#initalize turtle oblect
ball.speed(0)#speed of animation
ball.color("white")
ball.goto(0,0)#set the position
ball.penup()#stop drawing lines
ball.shape("circle")#set the shape
ball.dx=0.3#evrey time ball move by 0.3 pixel in sreen in x axis
ball.dy=0.3#evrey time ball move by 0.3 pixel in sreen in y axis
#score
score1=0
score2=0 
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player1 : "+str(score1)+" || Player2 :"+str(score2),align="center",font=("Courier",24,"normal"))


#functions
#move player 1 to up
def player1_up():
    # get y location
    y=player1.ycor()
    # update y location
    if(y<290 ):
        y+=15

    # set y location
    player1.sety(y)

#move player 1 to down
def player1_down():
    # get y location
    y=player1.ycor()
    # update y location
    if( y>-290):
     y-=15
    # set y location
    player1.sety(y)

#move player 2 to up
def player2_up():
    # get y location
    y=player2.ycor()
    # update y location
    if(y<290 ):
        y+=15
    # set y location
    player2.sety(y)

#move player 2 to down
def player2_down():
    # get y location
    y=player2.ycor()
    # update y location
    if( y>-290):
        y-=15
    # set y location
    player2.sety(y)

#keyboard bindings
wind.listen()#start listen to keys
wind.onkeypress(player1_up,"w")#set w to player 1 up
wind.onkeypress(player1_down,"s")#set s to player 1 up
wind.onkeypress(player2_up,"Up")#set w to player 1 up
wind.onkeypress(player2_down,"Down")#set s to player 1 up


#game loop
try:
    while True:
        #update screen
         wind.update()

         #mova ball
         ball.setx(ball.xcor()+ball.dx)#change x coordinate
         ball.sety(ball.ycor()+ball.dy)#change y coordinate

        #border check
            #check right border
         if ball.xcor()>=390:
             ball.goto(0,0)#go to center
             score1+=1
             ball.dx*=-1#change x direction
             score.clear()
             score.write("Player1 : "+str(score1)+" || Player2 :"+str(score2),align="center",font=("Courier",24,"normal"))

             #check lift border
         if ball.xcor()<=-390:
             ball.goto(0,0)#go to center
             score2+=1
             ball.dx*=-1#change x  direction
             score.clear()
             score.write("Player1 : "+str(score1)+" || Player2 :"+str(score2),align="center",font=("Courier",24,"normal"))

            #cehck up and down border
         if ball.ycor()>=290 or ball.ycor()<=-290:
             ball.dy*=-1#change y direction
        
        #check ball collision
         if ball.ycor()<=(player1.ycor()+60) and ball.ycor()>= (player1.ycor()-60) and  ball.xcor()>= (player1.xcor()-10)and  ball.xcor()<= (player1.xcor()+10):
             ball.setx(player1.xcor()+11)#set ball position
             ball.dy*=1#change y direction
             ball.dx*=-1#change y direction


         if ball.ycor()<=(player2.ycor()+60) and ball.ycor()>= (player2.ycor()-60) and  ball.xcor()>= (player2.xcor()-10)and  ball.xcor()<= (player2.xcor()+10):
             ball.dy*=1#change y direction
             ball.setx(player2.xcor()-11)#set ball position
             ball.dx*=-1#change y direction
except:
    print("")

