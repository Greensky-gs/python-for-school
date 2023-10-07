import random
import p5
import math

WIDTH = 800
HEIGHT = 800
bg = (230, 230, 230)
frmRate = 60

class Wait():
    def __init__(self, time: int):
        self.frames = 0
        self.time = time
        self._ended = False
    def check(self):
        if self.frames < (self.time * frmRate):
            self.frames += 1
        self._ended = self.frames >= self.time * frmRate
    
    def ended(self):
        return self._ended

class Game():
    def __init__(self):
        self.matrix = None
        self.revealed = None
        self.utils = {}
        self.bgRevealed = (250, 250, 250)
        self.unrevealed = (50, 50, 50)
        self.generatePlate()
        self.over = False
    
    def reset(self):
        self.matrix = None
        self.revealed = None
        self.utils = {}
        
        self.generatePlate()
        self.over = False
        
    def getUtil(self, util):
        return self.utils.get(util)
    
    def gridX(self, x):
        return math.floor(x / (self.utils.get('padSize') + self.utils.get('blank')))

    def gridY(self, y):
        return math.floor(y / (self.utils.get('padSize') + self.utils.get('blank')))

    def reveal(self):
        x = self.gridX(p5.mouseX)
        y = self.gridY(p5.mouseY)
    
        if x >= 0 and x < self.getUtil('inX') and y >= 0 and y < self.getUtil('inY') and not self.revealed[x][y]:
            self.revealEmpty(x, y, True)

    def revealEmpty(self, x, y, reveal = False):
        if x < 0 or x >= self.getUtil('inX') or y < 0 or y >= self.getUtil('inY') or self.revealed[x][y]:
            return
        if not self.matrix[x][y] == 0 and not reveal:
            return

        self.revealed[x][y] = True
        if self.matrix[x][y] == -1:
            self.gameOver()
            return

        for rx, ry in ( (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), ( x, y + 1 ), ( x + 1, y - 1 ), (x + 1, y), (x + 1, y + 1) ):
            self.revealEmpty(rx, ry)
        
    def sameColor(self, x, y, col):
        cl = p5.get(int(x), int(y))
        
        print(col, cl)
        
        return col[0] == cl[0] and col[1] == cl[1] and col[2] == cl[2]
    
    def drawPlate(self):
        if self.over:
            p5.fill(0, 0, 0, 75)
            p5.rect(0, 0, WIDTH, HEIGHT)

            p5.fill(0, 0, 0)
            p5.textSize(100)
            p5.textAlign(p5.CENTER, p5.CENTER)
            p5.text('Game Over', WIDTH / 2, HEIGHT / 2)
            return
        
        matrix = self.matrix
        
        def cords(x, y):
            if x < 0 or x >= self.getUtil('inX') or y < 0 or y >= self.getUtil('inY'):
                return None
            return matrix[x][y]
        
        def fX(i):
            return (i + 1) * self.utils.get('blank') + i * self.utils.get('padSize')
        def fY(i):
            return (i + 1) * self.utils.get('blank') + i * self.utils.get('padSize') 
        
        p5.textSize(20)
        for x in range(self.getUtil('inX') - 1):
            for y in range(self.getUtil('inY') - 1):
                if not self.revealed[x][y]:
                    p5.fill(*self.unrevealed)
                    p5.rect(fX(x), fY(y), self.getUtil('padSize'), self.getUtil('padSize'))
                else:
                    cols = (p5.color(255, 255, 255), p5.color(0, 0, 255), p5.color(0, 128, 0), p5.color(255, 0, 0), p5.color(0, 0, 128), p5.color(128, 0, 0), p5.color(0, 128, 128), p5.color(0, 0, 0), p5.color(128, 128, 128))
                    pad = cords(x, y)
                    
                    if pad == -1:
                        p5.fill(255)
                        p5.text("💣", fX(x) + 10, fY(y) + 20)
                    else:
                        p5.fill(cols[pad])
                        p5.text(str(pad), fX(x) + 10, fY(y) + 20)
                   
        
    def gameOver(self):
        self.over = True
        self.drawPlate()
        
    def generatePlate(self, *, padSize = 30, w = WIDTH, h = HEIGHT, blank = 10, bombs = False):
        blank = abs(blank)
        inX = math.floor(w / (padSize + blank))
        inY = math.floor(h / (padSize + blank))
        
        inX, inY = min(inX, inY), min(inX, inY)
        
        if inY < 1 or inX < 1:
            raise Exception("Please provide a valid padSize size")
        
        totalMines = inX * inY
        
        matrix = [[0 for _ in range(inX)] for _ in range(inY)]
        self.revealed = [[False for _ in range(inX)] for _ in range(inY)]

        if not bombs:
            bombs = totalMines * .1
        bombs = int(bombs)
        if bombs < 1 or bombs > totalMines:
            raise Exception("Please put a valid amount of bombs")
    
        self.utils = {
            "padSize": padSize,
            "w": WIDTH,
            "h": HEIGHT,
            "blank": blank,
            "inX": inX,
            "inY": inY
        }
    
        plate = []
        def cords(x, y):
            if x < 0 or x >= inX or y < 0 or y >= inY:
                return None
            return plate[x][y]

        def fill():
            for _ in range(inX):
                plate.append([])

            for x in range(inX):
                for y in range(inY):
                    plate[x].append(0)
        def randCords():
            coordinates = random.randint(0, inX - 1);
            return coordinates;

        fill()
        for _ in range(bombs):
            plate[randCords()][randCords()] = -1

        for x in range(inX):
            for y in range(inY):
                count = 0
                if cords(x, y) != -1:
                    for z in [(x - 1, y), (x + 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
                        if cords(z[0], z[1]) == -1:
                            count+= 1
                    plate[x][y] = count
        self.matrix = plate
        return self
            

def setup():
    p5.createCanvas(WIDTH, HEIGHT)
    p5.background(p5.color(bg))
    p5.frameRate(frmRate)


game = Game()
wait = None

def isHoverText():
    x = p5.mouseX;
    y = p5.mouseY
    
    p5.textSize(50)
    w = p5.textWidth("Play again")
    h = 50
    
    frX = WIDTH / 2 - w / 2 - 20
    frY = HEIGHT / 1.3 - 10
    
    toX = frX + 2 * w + 40
    toY = frY + h + 20
    
    return x >= frX and x <= toX and y >= frY and y <= toY

def draw():
    global game, wait
    
    if game.over:
        p5.textSize(50)
        p5.textAlign(p5.CENTER, p5.CENTER)
        
        p5.fill(250 if not isHoverText() else 200,  0, 0, 100)
        p5.text("Play again", WIDTH / 2, HEIGHT / 1.3)
        
        if p5.mouseIsPressed and p5.mouseButton == p5.LEFT and isHoverText():
            game.reset()
        wait = Wait(1)
        return
    
    
    if not not wait:
        wait.check()
        if not wait.ended():
            return
    
    p5.background(p5.color(bg))
    game.drawPlate()
    if p5.mouseIsPressed and p5.mouseButton == p5.LEFT:
        game.reveal()
    
p5.run()
