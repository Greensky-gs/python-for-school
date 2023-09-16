from p5 import *
from random import uniform

WIDTH = 500
HEIGHT = 500

# Génère une accroche 
def useState():
    hook = []
    
    def append(x):
        hook.append(x)
    def remove(index):
        hook.pop(index)
    def edit(index, value):
        hook[index] = value
    def clear():
        hook.clear()
    return [hook, append, remove, edit, clear]

maxFrames = 3
# Crée une accroche pour les confettis
[confettis, appendConfettis, removeConfettis, editConfettis, clearConfettis] = useState()

def setup() :
    createCanvas(WIDTH, HEIGHT)    # crée une zone de dessin aux dimensions données
    background(240)                # le fond est gris clair
    # noLoop()                       # A changer une fois que ton code est au point
    frameRate(1)

def draw():
    background(240)

    # Root variables
    midX = WIDTH / 2
    midY = HEIGHT / 2
    gapSize = 70;
    eyeSize = 30
    mouthRadius = 40;
    maxFrames = 3;
    pipeLength = 230
    
    # Root functions
    def holeColor():
        return color(131, 54, 28)
    def randomColor():
        def rnd():
            return int(random(0, 255))
        return (rnd(), rnd(), rnd())
    def percent(of, percent):
        return of * percent / 100
    def randomPos():
        while True:
            x = int(random(0, WIDTH))
            y = int(random(0, HEIGHT))
            distance = ((x - WIDTH/2) ** 2 + (y - HEIGHT/2) ** 2) ** 0.5
            if distance > 200:
                return (x, y)

    # Visage
    def drawFace():    
        noStroke()
        fill(255, 255, 0)
        ellipse(250, 250, 400, 400)
    
    # Yeux
    def drawEyes():
        for i in range(2):
            first = i == 1
            gap = (-1 if first else 1) * gapSize
        
            x = midX + gap;
            y = 170;
        
            # Dessin d'un oeil
            def drawEye():
                # couleur
                fill(holeColor())
            
                # Définition des coordonnées de passage
                frm = x + eyeSize
                to = x - eyeSize
                frmY = y + eyeSize
                toY = y - eyeSize
            
                # Trace la forme
                bezier(frm, frmY, x + 20, toY, x - 20, toY, to, frmY)
            drawEye()
    # Dessin de la bouche
    def drawMouth():
        x = midX
        y = HEIGHT / 3 * 2 - 15;
        
        fill(holeColor())
        ellipse(x, y, percent(mouthRadius, 110), mouthRadius)

    # Dessine les confettis
    def drawConfettis():
        # Donne une position aléatoire dans l'espace autour de l'émoji
        def generatePos():
            zones = [
                ((0, 100), (0, 100)),
                ((400, 500), (0, 100)),
                ((400, 500), (400, 500)),
                ((0, 100), (400, 500))
            ]
            zoneValues = []
            for zone in zones:
                x = int(random(zone[0][0], zone[0][1]))
                y = int(random(zone[1][0], zone[1][1]))
        
                zoneValues.append((x, y))
            return zoneValues[int(random(0, len(zones)))]

        # Donne une forme aléatoire
        def randomShape():
            shapes = ['star', 'triangle', 'losange']
            return shapes[int(random(0, len(shapes)))]

        # Dessine une forme
        def drawShape(shape, pos, size, cl):
            fill(cl)
            noStroke()
            x = pos[0]
            y = pos[1]

            # Définition des fonctions qui permettent de créer des formes

            # Fonction d'une étoile
            def star(radius1 = 30, radius2= 70, npoints = 5):
                z = size / 60
                angle = TWO_PI / npoints
                half_angle = angle/2.0
        
                beginShape()
                a = 0
                while a < TWO_PI:
                    sx = x + cos(a) * radius2 * z
                    sy = y + sin(a) * radius2 * z
                    vertex(sx, sy)
                    sx = x + cos(a+half_angle) * radius1 * z
                    sy = y + sin(a+half_angle) * radius1 * z
                    vertex(sx, sy)
                    a = a + angle
        
                endShape()
            
            # Fonction d'un triangle
            def triangleShape():
                rotated = radians(int(random(0, 360)))
                rotate(rotated)
                def randomSize(divide = False):
                    z = size // 2 if divide else size
                    return int(percent(z, int(random(80, 100))))

                triangle(x, y, x + randomSize(), y, x + randomSize(True), y + randomSize())
                rotate(rotated * -1)
            
            # Fonction d'un losange
            def diamond():
                rotated = radians(int(random(0, 360)))
                rotate(rotated)
                
                top = (x, y - size * 2)
                right = (x + size, y)
                bottom = (x, y + size * 2)
                left = (x - size, y)
                
                beginShape()
                
                for z in (top, right, bottom, left):
                    vertex(z[0], z[1])
                
                endShape()
                
                rotate(rotated * -1)

                
            # Récupération de la méthode appropriée
            shapes = {
                "star": star,
                "triangle": triangleShape,
                "losange": diamond
            }
            
            shapes.get(shape)()
        
        # Si aucun confettis n'est enregistré, création de nouveaux
        if len(confettis) == 0:
            for n in range(15):
                pos = generatePos()
                shape = randomShape();
                size = random(8, 10)
                cl = randomColor()
            
                drawShape(shape, pos, size, cl)
                appendConfettis((pos, size, shape, cl))
        else:
            # Déplacement des confettis existants
            for i in range(len(confettis)):
                cnf = confettis[i]

                pos = cnf[0]
                size = cnf[1]
                shape = cnf[2]
                cl = cnf[3]
                
                # Direction aléatoire
                def rndDir(x):
                    return x * (-1 if int(random(0, 100)) <= 50 else 1)
                def rnd():
                    return int(random(0, 10))
                
                x = pos[0] + rndDir(rnd())
                y = pos[1] + rndDir(rnd())
                
                drawShape(shape, pos, size, cl)
                editConfettis(i, ((x, y), size, shape, cl))
            
            # Réinitialisation des confettis quand l'animation est terminée
            if frameCount % maxFrames == maxFrames - 1:
                clearConfettis()
                
        
    # Dessine la langue de belle-mère
    def drawPipe():
        frameIndex = frameCount % maxFrames + 1
        fill(186, 140, 176)
        
        x = midX;
        y = HEIGHT / 3 * 2 - 15
        
        # Longueur proportionelle à l'avancée de l'animation
        length = int(percent(pipeLength, frameIndex * 100 / maxFrames))
        toX = midX + length
        toY = y + 2
                
        controlOne = (x + 30, y - 30)
        controlTwo = (x + 30, y + 30)
        
        # Dessine le tube
        beginShape()
        for n in ((x + 10, y), controlOne, (toX, toY), controlTwo):
            vertex(n[0], n[1])
        endShape()
        
        # Dessine l'embout
        fill(232, 52, 242)
        beginShape()
        for n in ((x - 3, y - 17), controlOne, controlTwo, (x - 3, y + 17)):
            vertex(n[0], n[1])
        endShape()
        
    # Dessine le smiley
    drawConfettis() # Génère les  confettis en premier pour qu'ils soient écrasés au besoin
    drawFace()
    drawEyes()
    drawMouth()
    drawConfettis()
    drawPipe()

run()
