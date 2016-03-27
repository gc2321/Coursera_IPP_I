# Testing template for format function in "Stopwatch - The game"

import simplegui

count = 0
try1 = 0
win = 0
add_score = 0

def format(n):
    
    msec = n%10
    sec = (int(n/10))%60
    min = (int((n/(60*10))))%60
    hour = (int((n/(60*60*10))))%24
    
    return add_zero(hour)+":"+add_zero(min)+":"+add_zero(sec)+"."+str(msec)

def add_zero(val):
    if val<=9:
        return "0"+str(val)
    else:
        return str(val)

def score():
    global try1, win
    return str(win)+"/"+str(try1)
    
# handlers
def draw_handler (canvas):
    global count
    canvas.draw_text(format(count), [120, 100], 38, "White")
    canvas.draw_text(score(), [310, 35], 38, "Red")
    
def timer_handler():
    global count
    count +=1
       
# define an input field handler
def start():
    global add_score
    timer.start()
    add_score = 1
    
def stop():
    global count, try1, win, add_score
    timer.stop() 
 
    if add_score == 1:
        try1 +=1
        if count%10 == 0:
            win +=1
    
    add_score = 0
    
def reset():
    global count, win, try1
    count = 0  
    win = 0
    try1 = 0
        
# register event handlers
timer = simplegui.create_timer(100, timer_handler)  
        
# create frame

frame = simplegui.create_frame("Converter", 400, 200)
frame.add_button('Start', start, 200)
frame.add_button('Stop', stop, 200)
frame.add_button('Reset', reset, 200)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

###################################################
# Test code for the format function
# Please note that hour is added
# uncomment the following section to test the script
 
'''
print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)
'''



###################################################
# Output from test
# Please note that hour is added

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

