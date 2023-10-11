from p5 import *
from math import *
from random import *

def smiley1(posX,posY, scl, *, WIDTH = 500, HEIGHT = 500):
    resetMatrix() #réinitialise les échelles et les translates
    translate(posX,posY) #déplace le repère
    scale(scl) #mets à l'échelle
    
    stroke(100,200,80)
    #Une couleur verte au hasard :
    fill(100,random(100,200),80)              #couleur du smiley 1
    ellipse(250,250,400,400)      #taille du  smiley
    #yeux
    noStroke()
    fill(25,50,10)            #couleur yeux
    ellipse(150,200,40,60)    #forme yeux
    ellipse(350,200,40,60)    #forme yeux
    #sourcils
    stroke(25,50,10)                   
    strokeWeight(4)
    noFill()
    x=random(50,100)               #courbure des sourcils aléatoire
    y=random(25,50)
    arc(100,150,x,y,radians(0),radians(100),OPEN)
    arc(400,150,x,y,radians(80),radians(180),OPEN)
    #paumettes
    noStroke()
    fill(100,175,80)
    ellipse(125,315,75,75)
    ellipse(375,315,75,75)
    #bouche
    stroke(25,50,10)
    strokeWeight(4+random(0,4))
    noFill()
    arc(250,315,135,40,radians(190),radians(350))
    arc(155,315,75,75,radians(300),radians(25))
    arc(345,315,75,75,radians(155),radians(240))
def smiley2(posX,posY,echelle):
    resetMatrix() #réinitialise les échelles et les translates
    translate(posX,posY) #déplace le repère
    scale(echelle) #mets à l'échelle
    
    strokeWeight(5)
    fill(240,200,50)
    ellipse(250,260,400,400)
    
    #oeil 1
    fill(0)
    ellipse(160,220,70,80)
    noStroke()
    fill(230)
    ellipse(145,205+random(-10,20),30,30)
    
    #oeil 2
    stroke(0)
    fill(0)
    ellipse(340,220,70,80)
    noStroke()
    fill(230)
    ellipse(325,205+random(-10,20),30,30)
    

    #oreilles (extérieur)
    fill(240,200,50)
    stroke(3)
    bezier(66,185,20,50,0,-20,165,80)
    bezier(434,185,480,50,500,-20,335,80)
    
    #oreilles (intérieur)
    strokeWeight(30)
    stroke(250,210,190)
    strokeJoin(ROUND)
    triangle(70,75,90,130,120,100)
    strokeWeight(30)
    stroke(250,210,190)
    strokeJoin(ROUND)
    triangle(430,75,410,130,380,100)
    
    #bouche
    stroke(0)
    noFill()
    strokeWeight(10)
    bezier(250,325,240,370,180,370,170,325)
    bezier(250,325,260,370,320,370,330,325)
    
    #nez
    strokeWeight(20)
    stroke(250,210,190)
    strokeJoin(ROUND)
    triangle(225,300,275,300,250,325)
    
    #moustaches
    strokeWeight(10)
    stroke(126)
    line(100,300,25,280+random(-20,20))
    line(100,320,20,320+random(-20,20))
    line(100,340,30,360+random(-20,20))
    line(400,300,475,280+random(-20,20))
    line(400,320,480,320+random(-20,20))
    line(400,340,470,360+random(-20,20))
def smiley3(posX,posY,echelle):
    resetMatrix() #réinitialise les échelles et les translates
    translate(posX,posY) #déplace le repère
    scale(echelle) #mets à l'échelle
    noStroke()
    
    #ce code sert à dessiner les cheveux de gauche
    fill(60,135,210)
    ellipse(90,110,80,80)
    ellipse(95,60,80,80)
    ellipse(145,50,50,50)
    ellipse(400,110,80,80)
    ellipse(405,60,80,80)
    ellipse(355,50,50,50)
    
    #ce code sert à dessiner le visage
    fill(255,229,204)
    ellipse(250,250, 400, 400)
    
    #ce code sert à dessiner les cheveux de droite
    fill(60,135,210)
    ellipse(100,95,50,50)
    ellipse(130,75,50,50)
    ellipse(390,95,50,50)
    ellipse(360,75,50,50)
    ellipse(355,50,50,50)
    
    #ce code sert à dessiner les yeux
    fill(90,49,7)
    taille=random(75,85)#utilisation d'une variable aléatoire
    ellipse(170,170,60,taille)
    ellipse(330,170,60,taille)
    
    #ce code sert à dessiner le sourire
    fill(200,0,0)
    arc(250,312,240,200,radians(random(0,20)),radians(random(160,180)),PIE)
    fill(255,229,204)
    arc(250,295,230,120,radians(0),radians(180),PIE)
    
    #ce code sert à dessiner le maquillage sur les joues 
    fill(255,153,153)
    ellipse(115,280,90,90)
    ellipse(385,280,90,90)
    
    #ce code sert à dessiner le nez
    fill(170,0,50)
    ellipse(250,260,80,80)

def afficheSmiley():
    global posSmileyX, posSmileyY, tailleSmiley, smileyIndex, smileys
    
    emoji = smileys[smileyIndex % len(smileys)]
    
    emoji(posSmileyX, posSmileyY, tailleSmiley)
def displayScore():
    global score
    resetMatrix()
    
    fill(255)
    textSize(30)
    textAlign(LEFT)
    text(f"Score: {score}", 20, 50)
def handleKonami():
    global konamiWaitFrames, konamiMode, konamiList, frmRate
    if konamiWaitFrames < frmRate * 1:
        konamiWaitFrames += 1
        return
    
    keys = ('u', 'u', 'd', 'd', 'l', 'r', 'l', 'r', 'b', 'a')
    if keyIsPressed:
        index = len(konamiList) if len(konamiList) > 0 else 0
        
        matching = key == keys[index]
        if matching:
            konamiList.append(key)
            if len(konamiList) == len(keys):
                konamiMode = not konamiMode
                konamiList = []
            else:
                konamiWaitFrames = 0
        else:
            konamiList = []
def compareCouleur(x,y,color):
    #renvoie True si la couleur en(x,y) est égale à la couleur passée
    couleur=get(int (x),int(y))
    # test print(couleur,end=" - ")
    if(couleur[0]==color[0] and couleur[1] == color[1] and couleur[2]==color[2]):
        return True
    else:
        return False

def testCollision():
    global posBalleX, posBalleY, score, tailleSmiley, smileyIndex, posSmileyX, posSmileyY
    
    centerX = posSmileyX + tailleSmiley * 200
    centerY = posSmileyY + tailleSmiley * 200

    dx = posBalleX - centerX
    dy = posBalleY - centerY
    d = sqrt(dx**2 + dy**2)
    
    if d <= 200 * tailleSmiley:
        score += 1
        tailleSmiley = random(0.1, 0.5)
        smileyIndex= int(random(len(smileys)))
def afficheRaquette():
    global posRaquetteX, posRaquetteY, tailleR,couleurRaquette, konamiMode, posBalleX, vitesseBalleY, selectedMode
    global WIDTH,HEIGHT
    fill(couleurRaquette)
    noStroke()
    posRaquetteX = mouseX - (tailleR / 2)
    limit = HEIGHT * .75
    
    if konamiMode or selectedMode == 1:
        posRaquetteX = posBalleX - (tailleR / 2 + random(-10, 10))
        posRaquetteY = HEIGHT - 5
    else:
        if mouseY > limit:
            posRaquetteY = mouseY
        else:
            posRaquetteY = limit
    rect(posRaquetteX, posRaquetteY, tailleR, 10)
def afficheBalle():
    global posBalleX, posBalleY, tailleBalle, ballCol
    fill(ballCol)
    ellipse(posBalleX, posBalleY, tailleBalle, tailleBalle)

def perdu():
    global WIDTH,HEIGHT, selectedMode
    
    textAlign(LEFT)
    fill(30, 30, 30, 70)
    rect(0, 0, WIDTH, HEIGHT)
    
    fill(color(0, 250, 0, 100))
    textSize(50)
    out = "Score:"+str(score)
    
    text("Perdu" if selectedMode == 0 else "Gagné",WIDTH/2,HEIGHT / 3)
    text(out, WIDTH/2 - (len(out) * 5), HEIGHT / 4 + 100)
    
    playAgain = "Rejouer"
    textSize(50)
    textAlign(CENTER)
    
    playAgainX = WIDTH / 2
    playAgainY = 4 * (HEIGHT / 5)
    
    textLength = len(playAgain) * 5
    
    def mouseHoverText():
        frX = playAgainX - textLength - 20
        frY = playAgainY - 20
        toX = playAgainX + textLength + 20
        toY = playAgainY + 20
        
        return mouseX > frX and mouseX < toX and mouseY > frY and mouseY < toY
    if mouseHoverText():
        fill(180, 5, 5, 100)
    else:
        fill(240, 20, 20, 100)
    text(playAgain, playAgainX, playAgainY)
    if mouseIsPressed and mouseHoverText():
        reset()

def reset():
    global score, smileyIndex, posSmileyX, posSmileyY, tailleSmiley, posBallX, posBalleY, posRaquetteX, posRaquetteY, tailleR
    global couleurRaquette, couleurRaquette, couleurBalle, vitesseBalleX, vitsseBalleY, tailleBalle, vitesseSmileyX, vitesseSmileyY
    global couleurFond, smileys, konamiList, frmRate, konamiWaitFrames, konamiMode, jouer, loadScreened, selectedMode
    
    jouer = True
    score = 0
    smileyIndex = 0
    posSmileyX = 50
    posSmileyY = 50
    tailleSmiley = 0.3
    posBalleX = WIDTH-50
    posBalleY = HEIGHT/2
    posRaquetteX = WIDTH/2
    posRaquetteY = HEIGHT-50
    tailleR = 100
    couleurRaquette = (255,0,0)
    couleurBalle = (0,255,0)
    vitesseBalleX = +5
    vitesseBalleY = -2
    tailleBalle = 15
    vitesseSmileyX = 4
    vitesseSmileyY = -4 
    couleurFond = (0,0,0)
    smileys = (smiley1, smiley2, smiley3)
    konamiList = []
    frmRate = 60
    konamiWaitFrames = 1 * frmRate
    konamiMode = False
    loadScreened= False
    selectedMode = None
    paused = False

def pause():
    global WIDTH, HEIGHT
    
    fill(30, 30, 30, 30)
    rect(0, 0, WIDTH, HEIGHT)
    
    fill(255, 255, 255)
    textAlign(CENTER)
    textSize(60)
    
    text("Pause", WIDTH / 2, HEIGHT / 3)
  def bougeBalle():
    global posBalleX, posBalleY, tailleBalle
    global vitesseBalleX, vitesseBalleY
    global posRaquetteX, posRaquetteY, tailleR
    global jouer,WIDTH,HEIGHT, selectedMode
    
    posBalleY = posBalleY + vitesseBalleY
    
    if selectedMode == 1:
        posBalleX = WIDTH if mouseX > WIDTH else 0 if mouseX < 0 else mouseX
    else:
        posBalleX = posBalleX + vitesseBalleX
        if (posBalleX > WIDTH-tailleBalle or posBalleX < tailleBalle):
            vitesseBalleX = -vitesseBalleX
    if (posBalleY < tailleBalle):
            vitesseBalleY = -vitesseBalleY
    
    # déplacement
    if (posBalleY > HEIGHT - 100):
        if balleTouchPad():
            #rebond sur raquette
            vitesseBalleY = -vitesseBalleY+(mouseX-pmouseX)/10
            vitesseBalleX=(posBalleX-posRaquetteX-tailleR /2) / tailleR*random(30,40)
        elif posBalleY >= HEIGHT:
            jouer = False #PERDU !
class Effect():
    def __init__(self, *, posX = int(random(0, WIDTH)), posY = int(random(0, HEIGHT)), size = 20, col = (255, 0, 0), shape = 'star'):
        self.x = posX
        self.y = posY
        self.size = size
        self.col = col
        self.shape = shape
        
    def shapes(self):
        return ('star', 'triangle', 'losange')
    def draw(self):
        resetMatrix()
        
        x = self.x
        y = self.y
        
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
    def useEffect():
        global tailleR, vitesseBalleX, vitesseBalleY, ballCol
        
        effects = ('fadeBall', 'increasePad', 'decreasePad', 'unfadeBall', 'increaseX', 'increaseY')
        effect = effects[int(random(0, len(effects)))]
        
        match effect:
            case 'increasePad':
                tailleR += 10
            case 'decreasePad':
                if tailleR > 10:
                    tailleR -= 10
                else:
                    tailleR = 3
            case 'increaseX':
                vitesseBalleX *= 1.2
            case 'increaseY':
                vitesseBalleY *= 1.2
            case 'fadeBall':
                ballCol = (ballCol[0], ballCol[1], ballCol[2], 120)
            case 'unfadeBall':
                ballCol = (ballCol[0], ballCol[1], ballCol[2], 255)
def balleTouchPad(*, balleY = None, balleX = None):
    global posBalleY, posBalleX, posRaquetteX, posRaquetteY, tailleR, HEIGHT
    x = posBalleX if not balleX else balleX
    y = posBalleY if not balleY else balleY
    
    if not posBalleY > HEIGHT - 100:
        return False
    return x > posRaquetteX and x < posRaquetteX + tailleR and y > posRaquetteY
def bougeSmiley():
    global posSmileyX, posSmileyY, tailleSmiley
    global vitesseSmileyX, vitesseSmileyY
    global WIDTH,HEIGHT
    
    posSmileyX = posSmileyX + vitesseSmileyX
    posSmileyY = posSmileyY + vitesseSmileyY
    
    if (posSmileyX > WIDTH or posSmileyX < 0):
        vitesseSmileyX = -vitesseSmileyX
    if (posSmileyY > HEIGHT / 2 or posSmileyY < 0):
        vitesseSmileyY = -vitesseSmileyY

#Définition des variables globales
WIDTH = 900
HEIGHT = 600
jouer = False
score = 0
smileyIndex = 0
posSmileyX = 50
posSmileyY = 50
tailleSmiley = 0.3
posBalleX = WIDTH-50
posBalleY = HEIGHT/2
posRaquetteX = WIDTH/2
posRaquetteY = HEIGHT-50
tailleR = 100
couleurRaquette = (255,0,0)
couleurBalle = (0,255,0)
vitesseBalleX = +5
vitesseBalleY = -2
tailleBalle = 15
vitesseSmileyX = 4
vitesseSmileyY = -4 
couleurFond = (0,0,0)
smileys = (smiley1, smiley2, smiley3)
konamiList = []
frmRate = 60
konamiWaitFrames = 1 * frmRate
konamiMode = False
loadScreened = False
selectedMode = None
paused = False
pauseWait = None
ballCol = (0, 250, 250)

def setup():
    global frmRate, jouer,score,WIDTH,HEIGHT
    jouer = True
    createCanvas(WIDTH, HEIGHT)    # crée une zone de dessin aux dimensions données 
    frameRate(frmRate) # à gérer

    
def loadScreen():
    global selectedMode, loadScreened
    
    background(0)
    
    textAlign(CENTER)
    textSize(45)
    fill(255, 0, 0, 200)
    text("CHOIX DU MODE DE JEU", WIDTH / 2, 100)
    
    textAlign(CENTER)
    textSize(30)
    middle = WIDTH / 2
    Y = HEIGHT / 1.5
    
    texts = ( ("Raquette", middle - WIDTH / 4, Y), ("Balle", middle + WIDTH / 4, Y) )
    
    def mouseHoverText(t, x, y):
        length = (len(t) * 10) / 2
        frX = x - length - 20
        toX = x + length + 20
        frY = y - 20
        toY = y + 20
        
        return mouseX > frX and mouseX < toX and mouseY > frY and mouseY < toY
    
    for i, val in enumerate(texts):
        t, x, y = val
        if mouseHoverText(t, x, y):
            fill(190, 190, 190, 200)
        else:
            fill(100, 100, 100, 195)
    
        text(t, x, y)
        
        if mouseIsPressed and mouseButton == LEFT and mouseHoverText(t, x, y):
            selectedMode = i
            loadScreened = True
def draw():
    global jouer, score, loadScreened, paused, pauseWait, frmRate
    # on doit entrer ceci pour 
    # utiliser les variables globales

    if not loadScreened:
        loadScreen()
        return
    
    if pauseWait:
        pauseWait.check(frmRate)
        
    if keyIsPressed and key == 'Pause' and jouer:        
        if pauseWait and pauseWait.ended():
            paused = not paused
            pauseWait = Wait(1)
        if not pauseWait:
            paused = not paused
            pauseWait = Wait(1)
    if paused:
        return pause()
    
    if(jouer):
        handleKonami()
        resetMatrix()
        background(0)
        afficheSmiley()
        resetMatrix()
        testCollision()
        afficheRaquette()
        afficheBalle()
        displayScore()
        bougeSmiley()
        bougeBalle()
    else:
        perdu()

run()

#
