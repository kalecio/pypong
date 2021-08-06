import turtle

wn = turtle.Screen()
wn.title("Pong by @kalecio")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)


# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.goto(0, 0)
ball.penup()

# Function
def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)

def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(player_a_up, "w")
wn.onkeypress(player_a_down, "s")
wn.onkeypress(player_b_up, "i")
wn.onkeypress(player_b_down, "k")

# Main game loop

while True:
    wn.update()
    