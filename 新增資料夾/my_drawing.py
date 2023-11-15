###
#Title: Maze
#I want to create a maze like structure, with adjustable parameters regarding its components.
###

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

def main(h1=720, shrink=0.8, round = 20):
    #to align the sides: let h1 = w1*shrink + h1*shrink^2
    w1 = (h1*(1-shrink*shrink))/shrink

    #make rim automatically fit size of shape
    win_w = 20+w1+int(h1*shrink)+20
    win_h = 20+int(h1)+20
    print(win_w, win_h)
    window = GWindow(width=win_w, height=win_h, title="Fractal")
    rim = GRect(width=win_w-20, height=win_h-20, x=10, y=10)
    rim.filled = True
    rim.fill_color = 'black'
    window.add(rim)

    #set color pallet for shape
    pallet = ['red', 'orange', 'yellow', 'greenyellow', 'green', 'turquoise', 'blue', 'navy', 'purple', 'plum']

    #first rectangle
    x = 20
    y = 20
    ww = [w1]
    hh = [h1]
    component = GRect(width=ww[0], height=hh[0], x=x, y=y)
    component.filled = True
    component.fill_color = pallet[0]
    window.add(component)

    #consecutive rectangles
    for i in range(1, round, 1):
        width = hh[i-1] * shrink
        height = ww[i-1] * shrink
        ww.append(int(width))
        hh.append(int(height))
        if i%4 == 1:
            x += ww[i-1]
        elif i%4 == 2:
            x += ww[i-1]-ww[i]
            y += hh[i-1]
        elif i%4  == 3:
            x += -ww[i]
            y += hh[i-1] - hh[i]
        else:
            y += -hh[i]

        #check position and size of rectangle
        print(x, y)
        print(ww)
        print(hh)

        #print shape
        component = GRect(height=hh[i], width=ww[i], x=x, y=y)
        component.filled = True
        component.fill_color = pallet[(i%len(pallet))]
        window.add(component)

main(720, 0.9, 40)
#F(shrink) = width/height of triangle: [(0.3, 3.03), (0.4, 2.1), (0.5, 1.5), (0.6, 1.07), (0.7, 0.73), (0.8, 0.45), (0.9, 0.21)]
