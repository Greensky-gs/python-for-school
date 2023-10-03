from p5 import *

W = 950
H = W * .8
penSize = 20
penMax = 100
penMin = 10
displayHelp = False
frmRate = 60
loaded = [False, 0, False];
strokedColor = color(255)

def setup() :
    createCanvas(W, H)
    background(0)
    frameRate(frmRate)

def mouseMoved():
    dx = mouseX != pmouseX
    dy = mouseY != pmouseY
    
    return dx or dy

def drawLoading():
    fill(255)
    textSize(40)
    textAlign(CENTER)
    
    titleX = W / 2
    titleY = 50
    text("Greensky-gs painter", titleX, titleY)
    
    textSize(20)
    text("Appuyez sur le bouton \"pause ATTN\" pour afficher la page d'aide", titleX, titleY + 200)

def colors():
    colrs = (
        ("Rouge", "r", color(255, 0, 0)),
        ("Vert", "v", color(0, 255, 0)),
        ("Bleu", "b", color(0, 0, 255)),
        ("Magenta", "m", color(255, 0, 255)),
        ("Cyan", "c", color(0, 255, 255)),
        ("Jaune", "j", color(255, 255, 0)),
        ("Noir", "n", color(0)),
        ("Blanc", "w", color(255))
    )
    
    longest = ("", "", color(0));
    for cl in colrs:
        if len(cl[0]) > len(longest[0]):
            longest = cl

    utils = {
        "longest": longest
    }
    def getColFromCode(code: str):
        filtered = list(filter(lambda x: x[1] == code, colrs))
        if len(filtered) == 0:
            return None;
        return filtered[0]
    return (colrs, getColFromCode, utils)
    
def draw():
    global displayHelp, loaded, strokedColor, penSize

    noStroke()
    
    if not loaded[0]:
        ellipsed = loaded[1]
        if ellipsed == frmRate * 5:
            loaded[0] = True
            background(0)
            fill(255)
        elif not loaded[2]:
            drawLoading()
            loaded[2] = True
        
        loaded[1]+=1
        return
    
    def drawHelp():
        [cols, getCode, utils] = colors()
        
        fill(getCode('w')[2])
        textSize(35)
        textAlign(CENTER)
        text("Page d'aide", W / 2, 50)
        textSize(30)
        text("Contrôles", 80, 150)
        
        textSize(20)
        textAlign(LEFT)
        text("""Effacer: maj
Pause: Pause ATTN
Dessiner une ligne: bouton droit
Dessiner un carré: molette
Dessiner un rond: bouton gauche""", 30, 210)
        
        textAlign(RIGHT)
        textSize(30)
        text("Couleurs", W - 100, 150)
        textSize(20)
        textAlign(LEFT)
        
        colorText = ""
        for col in cols:
            x = col[0] + ':'
            colorText += f"{x:15}{col[1]}\n"

        text(colorText, W - 210, 210)
        
        textSize(40)
        fill(getCode('r')[2])
        text("ATTENTION", W - 280, 450)
        textSize(20)
        fill(255)
        text("Pour choisir une couleur, vous devez d'abord cliquer avec la souris sur le code", W - 210, 490, 200, 200)
        
    if keyIsPressed and key == 'Pause':
        displayHelp = not displayHelp
        
    if displayHelp:
        drawHelp()
        return
    
    if keyIsPressed:
        [cols, getCode, utils] = colors()
        
        if not not getCode(key):
            fill(getCode(key)[2])
            strokedColor = getCode(key)[2]
        if key == 'Shift':
            background(0)
        
    if mouseMoved() and mouseIsPressed and mouseButton == RIGHT:
        stroke(strokedColor)
        line(mouseX, mouseY, pmouseX,pmouseY)
        noStroke()
    if mouseIsPressed:
        if mouseButton == CENTER:
            rect(mouseX, mouseY, penSize, penSize)
        if mouseButton == LEFT:
            ellipse(mouseX, mouseY, penSize, penSize)

run()
# Cliquez sur cet espace pour changer les couleurs
#
#
