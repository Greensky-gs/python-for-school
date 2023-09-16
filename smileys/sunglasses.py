from p5 import *

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

# Accroche pour les lunettes
[sunglasses, setSunglasses, resetSunglasses] = useState((500, 30, 0, 60))
# Accroche pour le sourire
[smile, setSmile, *_] = useState(int(random(190, 220)))

def setup() :
    createCanvas(WIDTH, HEIGHT)    # crée une zone de dessin aux dimensions données
    background(240)                # le fond est gris clair
    # noLoop()                       # A changer une fois que ton code est au point
    frameRate(60)

def draw():
    noStroke()
    background(240)

    # Root variables
    midX = WIDTH / 2
    midY = HEIGHT / 2
    gapSize = 70;
    eyeSize = 60
    eyeY = 180
    sunglassesGap = gapSize * 2 - eyeSize // 2
    sunGlassesY = eyeY - eyeSize / 2
    sunglassesToX = 122
    sunglassesBarColor = color(105, 105, 105)
    sunglassesColor = color(0, 0, 0)
    reflectMaxFrames = 90
    
    def holeColor():
        return color(131, 54, 28)
    
    def rnd(mx, mn):
        return int(random(mn, mx))
    
    # Dessine une forme selon la liste de coordonnées
    def drawVertex(values):
        beginShape()
        for value in values:
            vertex(value[0], value[1])
        endShape()
    
    # Dessin du visage
    def drawFace():
        fill(250, 250, 0)
                
        ellipse(midX, midY, 400, 400)
    def drawEyes():
        for i in range(2):
            first = i == 1
            gap = (-1 if first else 1) * gapSize
        
            x = midX + gap;
        
            # Dessin d'un oeil
            def drawEye():
                # couleur
                fill(holeColor())
                
                ellipse(x, eyeY, eyeSize, eyeSize)
                
            drawEye()
    
    # Dessin de la bouche
    def drawMouth():
        x = midX
        y = midY;
        gap = 80
        
        fill(holeColor())

        arc(x,y, 220, smile(), radians(20), radians(180), PIE)
        fill(250, 250, 0)
        arc(x, y, 240, 180, radians(0), radians(200), PIE)
        
    # Dessin des lunettes
    def drawSunglasses():
        data = sunglasses()
            
        x = data[0] - 2 if data[0] > sunglassesToX else data[0]
        setSunglasses((x, *data[1:]))
            
        if x == sunglassesToX and data[1] > 0:
            setSunglasses((*data[:1], data[1] - 1, *data[2:]))
        y = sunGlassesY
            
        # Barre
        fill(sunglassesBarColor)
        rect(x + 80, y + 10, sunglassesGap, 10)
            
        fill(sunglassesColor) # Couleur par défaut des verres
        if data[1] == 0:
            frames = data[2]
            percent = frames * 100 / reflectMaxFrames
            
            if percent <= 40:
                c = map(percent, 0, 40, 0, 255)
            elif percent <= 60:
                c = 255
            else:
                c = map(percent, 60, 100, 255, 0)
            
            colorValue = color(c)
            fill(colorValue)
            
            setSunglasses(( *data[:2], frames + 1, *data[3:] ))
            
            if percent == 100 and data[3] > 0:
                setSunglasses(( *data[:3], data[3] - 1 ))
            elif percent == 100 and data[3] == 0:
                resetSunglasses()
                setSmile(int(random(190, 220)))
        
        # Verre gauche
        drawVertex(((x, y), (x + 100, y), (x + 80, y + 60), (x + 20, y + 60)))
    
        # Verre droit
        distance = sunglassesGap - 60
        drawVertex((
            ( x + 100 + distance, y ),
            ( x + 200 + distance, y ),
            ( x + 180 + distance, y + 60 ),
            ( x + 120 + distance, y + 60 )
        ))
    
    # Dessin des éléments
    drawFace()
    drawEyes()
    drawMouth()
    drawSunglasses()

run()
