"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved

# This constant controls the size of the GRect
SIZE = 10
count = 0
xx = 0
yy = 0
circlex = 0
circley = 0
m = []
window = GWindow(500, 500)

def main():
	onmouseclicked(draw)


def draw(event):
	global count, circlex, circley
	circ = GOval(SIZE, SIZE)
	count = count + 1
	xx = event.x
	yy = event.y
	print(xx,yy, count)
	if count%2 == 1:
		circlex = xx
		circley = yy
		window.add(circ, x=event.x-SIZE/2, y=event.y-SIZE/2)
	elif count%2 == 0:
		circ_obj = window.get_object_at(circlex, circley)
		window.remove(circ_obj)
		line = GLine(xx, yy, circlex, circley)
		window.add(line)



if __name__ == '__main__':
	main()
