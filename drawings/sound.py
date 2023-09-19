from p5 import *

WIDTH = 600
HEIGHT = 400

bgC = 200
def setup() :
    createCanvas(WIDTH, HEIGHT)    # crée une zone de dessin aux dimensions données
    background(bgC)                # le fond est gris clair
    frameRate(400)                       # draw() ne sera appelée qu'une fois
    

lines = []
def appendArray(l, cl):
    lines.append((l, cl))
    if len(lines) >= HEIGHT:
        lines.pop(0)
    return lines
def last():
    if len(lines) == 0:
        return random(80, 140)
    return lines[len(lines) - 1][0]
def lastColor():
    if (len(lines) == 0):
        def rnd(mn, mx):
            return int(random(mn, mx))
        red = rnd(30, 255)
        green = rnd(100, 150)
        blue = rnd(150, 200)
        return (red, green, blue)
    return lines[len(lines) - 1][1]
def draw():
    noStroke()
    background(bgC)
    mid = int(WIDTH / 2)
    def rndColor():
        last = lastColor()
        def rnd(mn, mx, around):
            up = around + 10
            down = around - 10
            
            return int(random(down, up))
        red = rnd(0, 255, last[0])
        green = rnd(100, 150, last[1])
        blue = rnd(150, 200, last[2])
        return (red, green, blue)
    def drawLine(i, size, cl):
        stroke(color(cl))
        line(mid - size, i, mid + size, i)
    for i in range(len(lines)):
        size = lines[i][0]
        cl = lines[i][1]
        drawLine(i, size, cl)

    around = last()
    aroundDown = around - 10
    aroundUp = around + 10
    cl = rndColor();

    length = int(random(aroundDown, aroundUp))
    appendArray(length, cl)
run()
