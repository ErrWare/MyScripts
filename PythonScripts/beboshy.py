import pyautogui as gui
from pyautogui import typewrite, keyDown as down, keyUp as up
from time import sleep

RESTART = 'r'
JUMP = 'z'
SHOOT = 'x'
RIGHT = 'right'
LEFT = 'left'

def left(x):
	down(LEFT)
	sleep(x)
	up(LEFT)

def right(x):
	down(RIGHT)
	sleep(x)
	up(RIGHT)

def START():
	resX, resY = gui.size()

	gui.moveTo(resX-30,resY/2 - 20)
	gui.click()
	sleep(0.5)
	down(RESTART)
	up(RESTART)

def END():
	up(RESTART)
	up(JUMP)
	up(SHOOT)
	up(RIGHT)
	up(LEFT)


END()
START()

#Tutorial -> starting area
right(5)
sleep(1.5)

#starting area -> down
	# INIT FALL
right(1.75)
sleep(1.75)
	# DODGE RIGHT
right(0.1)
sleep(0.1)
	# DODGE LEFT
left(0.03)
	# DODGE RIGHT
#sleep(0.03)
right(0.1)
left(0.02)

#down platform -> chest
down(LEFT)
down(JUMP)
#sleep(0.02)
up(JUMP)
sleep(0.4)
down(JUMP)	# double reset get

sleep(0.25)
up(JUMP)
up(LEFT)
sleep(0.005)
down(RIGHT)
down(JUMP)
sleep(1)




END()