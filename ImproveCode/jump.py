import os
import time
import random
import numpy
import PIL
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

need_update = True

def get_screen_image():
    os.system('./adb shell screencap -p /sdcard/screen.png')
    os.system('./adb pull /sdcard/screen.png')

    return numpy.array(PIL.Image.open('screen.png'))


def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    px1 = random.randint(300, 400)
    py1 = random.randint(300, 400)
    px2 = random.randint(300, 400)
    py2 = random.randint(300, 400)

    os.system('./adb shell input swipe {} {} {} {} {}'.format(px1, py1, px2, py2, int(d*1.35)))

    global need_update
    need_update = True

    time.sleep(1)


def update_screen(frame):
    global need_update
    if need_update:
        axes_image.set_array(get_screen_image())
        need_update = False

    return axes_image,


def on_click(event, coor=[]):
    x, y = event.xdata, event.ydata
    coor.append((x, y))
    if len(coor) == 2:
        jump_to_next(coor.pop(), coor.pop())


figure = plt.figure()
axes_image = plt.imshow(get_screen_image(), animated=True)
figure.canvas.mpl_connect('button_press_event', on_click)
ani = FuncAnimation(figure, update_screen, interval=500, blit=True)
plt.show()

