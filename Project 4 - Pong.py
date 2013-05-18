import simplegui
import random

# globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
way = True	# True for right, False for left direction
paddle1_pos = float(HEIGHT / 2)
paddle2_pos = float(HEIGHT / 2)
paddle1_vel = float(0)
paddle2_vel = float(0)
pad_acc = 5	# accelerator value for paddles

# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right:
        ball_vel = [random.randrange(2, 4) , -(random.randrange(1, 3))]
    else:
        ball_vel = [ -(random.randrange(2, 4)) , -(random.randrange(1, 3))]
        
# event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = float(HEIGHT / 2)
    paddle2_pos = float(HEIGHT / 2)
    paddle1_vel = float(0)
    paddle2_vel = float(0)
    way = True
    ball_init(way)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, way
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")	#midline
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")	#left gutter
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")	#right gutter
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 3, "White", "White")
    
    # collide and reflection of the ball from the top and bottom of wall
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # collision of ball with gutters
    
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):	# if it hits left wall
        # If ball position is between vertical range of paddles
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            # incrementing velocity of ball by 10%
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        # else it scores, respawns ball
        else:
            score2 += 1
            way = True
            ball_init(way)
            
    if (ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):	#if it hits right wall
        # If ball position is between vertical range of paddles
        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            # incrementing velocity of ball by 10%
            ball_vel[0] += ball_vel[0] * 0.10
            ball_vel[1] += ball_vel[1] * 0.10
        # else it scores, respawns ball
        else:
            score1 += 1
            way = False
            ball_init(way)
    
    # printing scores
    c.draw_text(str(score1), [150,100], 45, "Lime")
    c.draw_text(str(score2), [450,100], 45, "Lime")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += pad_acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += pad_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= pad_acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel += pad_acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= pad_acc


# create frame
frame = simplegui.create_frame("Pong by Mustafa Babil", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)

# start frame
frame.start()
new_game()