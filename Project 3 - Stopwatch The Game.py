import simplegui

# global variables
count = 0
a = 0
b = 0
c = 0
d = 0
clock = ""
x = 0
y = 0
result = str(x) + '/' + str(y)	# x / y

# increasing counter by 1
def counter():
    global count
    count += 1
    
# formatting time function
def format(t):
    global a,b,c,d,clock
    a = t // 600
    b = (t // 100) % 6
    c = (t // 10) % 10
    d = t % 10
    # string representation of the formatted time
    clock = str(a) + ':' + str(b) + str(c) + '.' + str(d)
    return clock

# event handlers for buttons
def start():
    timer.start()
    
def stop():
    global x,y,result
    
    if (timer.is_running() == True):	# controller for if stopwatch is started first
        if ( d == 0 ):
            x += 1
        y += 1
    result = str(x) + '/' + str(y)
    timer.stop()
    
    
def reset():
    global count,x,y,result
    
    # to set the time 0:00.0
    count = 0
    format(count)
    x = 0
    y = 0
    result = str(x) + '/' + str(y)
    # to stop the timer
    timer.stop()
    
# event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, counter)

# draw handler
def draw(canvas):
    canvas.draw_text(format(count), [125, 125], 25, "White")
    canvas.draw_text(result, [225,50], 25, "Red")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)	# register draw handler
frame.add_button("Start", start, 75)	# register buttons
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", reset, 75)

# start frame
frame.start()
