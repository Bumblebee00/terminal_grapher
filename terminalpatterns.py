'''Micheletta Merlin Mattia
Cartesian Grapher in terminal - draws graphs of the function in the
functions list, for the graph to not be squished you need
to set the font_dim variable, which is the ratio between height and
width of the letter box in your font'''
font_dim = 1.8

import numpy as np
import math
import os

# ----- utility -----
def point_to_index(point):
    x_i = int((point[0] + grid_dim[0]/2)/unit)
    y_i = int((grid_dim[1]/2 - point[1])/(unit*font_dim))
    return x_i, y_i

def top_h(x):
    return math.sqrt(-x**2 + 2*abs(x))
def bottom_h(x):
    return math.asin(abs(x)-1) - math.pi/2
# (   math.sin(100*x)*(top(x)-bottom(x)) + (top(x) + bottom(x))   )/2


# ----- variables -----
full_char = '█'
empty_char = ' '
# creat grid
unit = float(input('A character is equal to how many units? (1 very zoomed out, 0.1 quite normal view)'))
columns, rows = os.get_terminal_size()
canvas = np.zeros((rows, columns))
# is in cartesian dimensions
grid_dim = (columns * unit, rows * (unit*font_dim))


# ----- create functions list -----
functions = []
while True:
    f_string = input('Input a function written as in pyhon (you have math module) (es: (3*x)/math.sqrt(1+x**2)) (y= is implied, do not write) or ! to graph: ')
    if f_string == '!': break
    if f_string == 'heart':
        functions.append('top_h(x)')
        functions.append('bottom_h(x)')
        break
    functions.append(f_string)


# ----- graph functions list -----
for function in functions:
    for x in np.arange(-grid_dim[0] / 2, grid_dim[0] / 2, unit):
        try:
            point = (x, eval(function))
            if abs(point[1])<(grid_dim[1]/2):
                i = point_to_index(point)
                canvas[i[1]][i[0]] = 1
        except: pass
# print the string :)
for y in canvas:
    for p in y:
        print(empty_char if p == 0 else full_char, end = '')
    print()
