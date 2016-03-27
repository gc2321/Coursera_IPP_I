# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
collide = 0
score1 = 0
score2 = 0
direction = random.randrange(1,3)

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [int(WIDTH/2), int(HEIGHT/2)]
ball_vel = [0, 0]
paddle1_pos = [PAD_WIDTH/2, (HEIGHT/2)-(PAD_HEIGHT/2)]
paddle2_pos = [WIDTH - (PAD_WIDTH/2), (HEIGHT/2)-(PAD_HEIGHT/2)]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel, direction # these are vectors stored as lists        
    if direction == 1:
        ball_vel[0]+=2
    else:
        ball_vel[0]-=2
    ball_vel[1]=-2
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, ball_pos, ball_vel, collide  # these are ints
    ball_pos = [int(WIDTH/2), int(HEIGHT/2)]
    ball_vel = [0, 0]
    spawn_ball()
    collide = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, collide, direction
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle([int(WIDTH/2), int(HEIGHT/2)],80, 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "YELLOW", "YELLOW")
    
    # update paddle's vertical position, keep paddle on the screen
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1]], [paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT], PAD_WIDTH, "RED")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1]], [paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT], PAD_WIDTH, "RED")
 
    # determine whether paddle and ball collide   
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT-BALL_RADIUS)):
        ball_vel[1] = - ball_vel[1]
        ball_vel[0] = ball_vel[0]*1.05
        ball_vel[1] = ball_vel[1]*1.05
        
    # draw scores
    canvas.draw_text(score(), [200, 35], 38, "Red")
    
    crash() 
    if (collide!=0):
        ball_vel[0] = - ball_vel[0]
        collide = 0
    
    if (ball_pos[0] <= BALL_RADIUS) or (ball_pos[0] >= (WIDTH-BALL_RADIUS)):
        if (ball_pos[0] <= BALL_RADIUS):
            score2 +=1
            direction = 1
        else:
            score1 +=1
            direction = 2
        new_game()
   
def crash():
    global collide
    if ((ball_pos[0] <= (BALL_RADIUS+PAD_WIDTH/2) and 
        ball_pos[1]> (paddle1_pos[1]-(BALL_RADIUS/3)) and
         ball_pos[1]<= (paddle1_pos[1]+PAD_HEIGHT+(BALL_RADIUS/3)))
        or (ball_pos[0] >= (WIDTH-BALL_RADIUS-PAD_WIDTH/2) and 
            ball_pos[1]> (paddle2_pos[1]-(BALL_RADIUS/3)) and
            ball_pos[1]<= (paddle2_pos[1]+PAD_HEIGHT+(BALL_RADIUS/3)))
        ):
        collide = 1
    return collide

def score():
    global score1, score2
    return str(score1)+"                  "+str(score2)

def restart():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()

def lock(a):    
    if a>=HEIGHT-PAD_HEIGHT:
        a=HEIGHT-PAD_HEIGHT
    elif a<=0:
        a=0    
    return a

def keydown(key):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_pos[1] =  lock(paddle1_pos[1] + 60)
    if key == simplegui.KEY_MAP['down']:
        paddle2_pos[1] = lock(paddle2_pos[1] + 60)
                
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_pos[1] =  lock(paddle1_pos[1] - 60)
    if key == simplegui.KEY_MAP['up']:
        paddle2_pos[1] = lock(paddle2_pos[1] - 60)
       
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 200)

# start frame
frame.start()
new_game()