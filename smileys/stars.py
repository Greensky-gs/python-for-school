from p5 import *
from random import randint, uniform

WIDTH = 500
HEIGHT = 500

# Création d'une fonction d'accroche
def useState(defaultValue = None):
    hook = {
        "value": defaultValue
    }
    
    def getHook():
        return hook.get("value", defaultValue)
    def setHook(value):
        hook["value"] = value
    def reset():
        hook['value'] = defaultValue
        
    return [getHook, setHook, reset]

def setup() :
    createCanvas(WIDTH, HEIGHT)    # crée une zone de dessin aux dimensions données
    background(240)                # le fond est gris clair
    frameRate(3)
    
def draw():
    background(240)
    noStroke()
    
    # Root variables
    midX = WIDTH / 2
    midY = HEIGHT / 2
    holeColor = color(randint(120, 140), randint(40, 60), randint(10, 40))
    mouthRadius = 60
    eyesGap = 70
    
    # Partie tête
    def drawFace():
        w = randint(360, 400)
        s = randint(1, 3)
        
        for i, v in enumerate(range(randint(180, 200), randint(230, 250))):
            fill(v, v, 0)
            ellipse(midX, midY, w - i * s, w - i * s)
        
    
    # Partie bouche
    def drawMouth():
        y = midY + 100
        
        fill(holeColor)
        ellipse(midX, y, mouthRadius + randint(10, 16), mouthRadius)
    
    # Partie yeux
    def drawEyes():
        # Fonction d'une étoile
        def star(x, y, size, radius1 = 30, radius2= 70, npoints = 5):
            z = size / 140
            angle = TWO_PI / npoints
            half_angle = angle / 2.0
            random_angle = uniform(0, TWO_PI) # Génération d'une orientation aléatoire
    
            beginShape()
            a = 0
            while a < TWO_PI:
                sx = x + cos(a + random_angle) * radius2 * z
                sy = y + sin(a + random_angle) * radius2 * z
                vertex(sx, sy)
                sx = x + cos(a + half_angle + random_angle) * radius1 * z
                sy = y + sin(a + half_angle + random_angle) * radius1 * z
                vertex(sx, sy)
                a = a + angle
        
            endShape()

        # Dessine un oeil
        def drawEye(x):
            y = 190
            size = randint(60, 80)
            cl = color(randint(0, 255), randint(0, 255), randint(0, 255))
            
            fill(cl)
            star(x, y, size)
        
        for x in (midX - eyesGap, midX + eyesGap):
            drawEye(x)

    # Dessine le smiley
    drawFace() # Tête
    drawMouth() # Bouche
    drawEyes() # Yeux

run()
