from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

window = GWindow(width=300, height=300, title="Bounce")
X_START = 20
Y_START = 20
VX = 5
GRAVITY = 0.5
DELAY = 50
SIZE = 10
REDUCE = 0.95
ball = GOval(SIZE, SIZE)
count = 0

def main():
	window.add(ball, x=X_START-SIZE/2, y=Y_START-SIZE/2)
	onmouseclicked(drop)
		
def drop(event):
	global count
	while count < 3:
		pause(DELAY)
		if event:
			if ball.x-SIZE/2 <= window.width:
				if ball.y == Y_START-SIZE/2:
					vy = 0.3
				elif ball.y+SIZE < window.height:
					vy = vy + GRAVITY*(ball.x-20)/VX
				else:
					vy = -vy*REDUCE
				ball.move(VX, vy)
			else:
				ball.x = X_START
				ball.y = Y_START-SIZE/2
				count += 1
				break #break while loop

if __name__ == '__main__':
	main()