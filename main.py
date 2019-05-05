import pygame
import random
import time
class duvar():
    def __init__(self,screen):
        self.duvarX=720
        self.duvarY=-20
        self.duvar2X=-20
        self.duvar2Y=430
        width=screen.get_width() #800
        height=screen.get_height() #600

        self.rectangle= pygame.rect.Rect(-25,10 ,int(width / 10),int(height)-int(height/2))

        self.rectangle2 = pygame.rect.Rect(745,350, int(width / 10), int(height)-int(height/2))

    def draw(self,screen):
        self.image = pygame.image.load("images/dikey.png")
        self.image = pygame.transform.scale(self.image, (self.rectangle[2], self.rectangle[3]))
        self.image2 = pygame.image.load("images/dikey.png")
        self.image2 = pygame.transform.scale(self.image2, (self.rectangle2[2], self.rectangle2[3]))


        screen.blit(self.image, self.rectangle)
        screen.blit(self.image2, self.rectangle2)

class yilan():

    def __init__(self,screen):
        self.yilanX=500
        self.yilanY=400
        width=screen.get_width() #800
        height=screen.get_height() #600
        self.yilanUzunlugu=[]
        self.bes=5
        self.ekran=20
        self.yilanLength=0
        self.rectangle = pygame.rect.Rect(self.yilanX , self.yilanY ,int(width / 40),int(height / 30))
        self.crashed=False
        self.puan=0
        self.hızX=0
        self.hızY = 0


    def draw(self,mx,my,screen): #yılanı cizer
        self.hızX = mx
        self.hızY = my
        self.yilanX= self.yilanX + self.hızX*4
        self.yilanY = self.yilanY + self.hızY*4
        self.yilanTamami = []
        self.yilanTamami.append(self.yilanX)
        self.yilanTamami.append(self.yilanY)
        self.yilanUzunlugu.append(self.yilanTamami) # yilanUzunlugu=[[x,y],[x,y],[x,y]]


        for konumlar in self.yilanUzunlugu:
            self.image = pygame.image.load("images/gri3min.png")
            self.image = pygame.transform.scale(self.image, (self.rectangle[2], self.rectangle[3]))
            self.rectangle[0]=konumlar[0]
            self.rectangle[1]=konumlar[1]
            screen.blit(self.image, self.rectangle)


        if len(self.yilanUzunlugu) > self.yilanLength: #yılan sondan silindi uzayıp gitmesin diye
            del self.yilanUzunlugu[0]



        if gameDuvar.rectangle.contains(self.rectangle) \
                or gameDuvar.rectangle2.contains(self.rectangle):#eger duvara çarparsa oyun biter
                gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)


        self.ekranGecisi(gameDisplay)
        self.eat()
        mesaj(gameDisplay, gameYilan.yilanLength * 5)




    def ekranGecisi(self,screen): #ekran arası yılan gecisi icin

        width=screen.get_width() #800
        height=screen.get_height() #600
        if self.yilanY>= height:
            self.yilanY= 50
        elif self.yilanY < 50:
            self.yilanY = height
        if self.yilanX >= width:
            self.yilanX = 0
        elif self.yilanX < 0:
            self.yilanX = width

    def eat(self):
        #elmanın yilanın bulundugu x y konumları arasında olup olmadığının kontrolu
        if (gameYilan.yilanX >= gamePlaneApple.rectangle[0] and gameYilan.yilanX <= (gamePlaneApple.rectangle[0])+gamePlaneApple.rectangle[2]
                and gameYilan.yilanY >= gamePlaneApple.rectangle[1] and gameYilan.yilanY <= (gamePlaneApple.rectangle[1])+gamePlaneApple.rectangle[3]):

            yeni=elma(gameDisplay)#elmayı yediğinde yeni elma oluşur

            gamePlaneApple.rectangle[0]=yeni.elmaX
            gamePlaneApple.rectangle[1] = yeni.elmaY

            self.yilanLength += 1 #yılan uzunlugu 1 artar
        elif(gameYilan.yilanX >= gamePlaneApple2.rectangle2[0] and gameYilan.yilanX <= (gamePlaneApple2.rectangle2[0]) + gamePlaneApple2.rectangle2[2]
                and gameYilan.yilanY >= gamePlaneApple2.rectangle2[1] and gameYilan.yilanY <= (gamePlaneApple2.rectangle2[1]) + gamePlaneApple2.rectangle2[3]):

            yeni = elma(gameDisplay)

            gamePlaneApple2.rectangle2[0] = yeni.elma2X
            gamePlaneApple2.rectangle2[1] = yeni.elma2Y


            if gamePlaneApple2.secilen== gamePlaneApple.elmalar[0]: #1azaltan
                if self.yilanLength==0:
                    gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)

                self.yilanLength -= 1
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[1]: #3artıran
                    self.yilanLength += 3
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[2]: #hizlandiran
                gameYilan.bes=6
                gameYilan.ekran=100


            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[3]: #olduren
                gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)

            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[4]: #yavaslatan
                gameYilan.bes=4
                gameYilan.ekran=4


            gamePlaneApple2.randomElma()  # elma yendikten sonra random farklı elma gelmesi icin

        for kare in gameYilan.yilanUzunlugu[:-1]: #son kareye kadar
            if kare == gameYilan.yilanTamami:
                gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)

class elma():

    def __init__(self,screen):

        width=screen.get_width() #800
        height=screen.get_height() #600
        self.elmaX = round(random.randrange(50, width -80))
        self.elmaY = round(random.randrange(30, height -50))
        self.elma2X = round(random.randrange(50, width -80)) #yeşilden farlı olan elma
        self.elma2Y = round(random.randrange(30, height -50))


        if self.elmaX<self.elma2X and self.elmaX>self.elma2X+30:
            if self.elmaY < self.elma2Y and self.elmaY > self.elma2Y + 30:
                #bu kısım 2 elmanın üst üste gelmemesi için tekrar random deger atadım
                self.elma2X = round(random.randrange(30, width - 50))
                self.elma2Y = round(random.randrange(30, height - 50))


        self.rectangle = pygame.rect.Rect(self.elmaX , self.elmaY ,int(width / 13),int(height / 13))
        self.rectangle2 = pygame.rect.Rect(self.elma2X , self.elma2Y ,int(width / 13),int(height / 13))
        self.elmalar = ["1AzaltanElma", "3ArtıranElma", "hızlı", "olduren", "salyangoz"]

        self.randomElma()

    def drawApple(self,screen):
        self.image = pygame.image.load("images/1ArtıranElma.png")

        self.image= pygame.transform.scale(self.image, (self.rectangle[2],self.rectangle[3]))
        screen.blit(self.image, self.rectangle)

    def drawApple2(self,screen):

        self.image2 = pygame.image.load("images/" + self.secilen + ".png")

        self.image2= pygame.transform.scale(self.image2, (self.rectangle2[2],self.rectangle2[3]))
        screen.blit(self.image2, self.rectangle2)


    def randomElma(self):

        self.secilen = random.choice(self.elmalar)


def mesaj(screen,skor): #ekranda skoru gösterecek
    yaziTipi = pygame.font.SysFont("arial", 20)
    yaziTipi2 = pygame.font.SysFont("arial", 50)

    text = yaziTipi.render("Skor: "+str(skor)+" /100", True, black)
    gameYilan.puan=skor
    screen.blit(text, [screen.get_width()/2,0])#ekranın ortasında olması için

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    yaziTipi = pygame.font.SysFont("arial", 20)
    contador = yaziTipi.render("time: " + str(seconds) + " /100.0", True, black)
    gameDisplay.blit(contador, [0, 0])

    if skor==100:

        gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)
    if seconds > 100:

        gameYilan.crashed = gameOverMenu.runExitMenu(gameDisplay)


class Menu_ButtonItem():
    def __init__(self, name, width=100, height=100, centerlocation=(0, 0), mainColor=(128, 128, 128),
                 onMouseOverColor=(128, 150, 150), onMouseDownColor=(50, 100, 150), text="notext", textSize=80,
                 textColor=(0, 0, 0)):
        self.name = name
        self.colorList = [mainColor, onMouseOverColor, onMouseDownColor]
        self.centerlocation = centerlocation
        self.width = width
        self.height = height
        self.rectangle = pygame.rect.Rect(0, 0, self.width, self.height)
        self.rectangle.center = centerlocation

        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        self.fontedText = pygame.font.SysFont("arial", self.textSize).render(self.text, True, self.textColor)
        self.textRectangle = pygame.rect.Rect(0, 0, self.fontedText.get_width(), self.fontedText.get_height())
        self.textRectangle.center = self.rectangle.center
        self.isMouseOver = False  # mouse is over
        self.state = 0  # mouse state for color changing
        self.mouseDownEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseDownEvent")
        self.mouseUpEvent = pygame.event.Event(pygame.USEREVENT, attr1=self.name, attr2="mouseUpEvent")

    def checkMouseOver(self, mlocation):
        if self.state == 2:
            return True
        if self.rectangle.collidepoint(mlocation):
            self.state = 1
            return True
        self.state = 0
        return False

    def onMouseDown(self, mlocation):
        if self.rectangle.collidepoint(mlocation):
            pygame.event.post(self.mouseDownEvent)
            self.state = 2

    def onMouseUp(self, mlocation):
        if self.state == 2:
            pygame.event.post(self.mouseUpEvent)
            self.state = 0
            self.checkMouseOver(mlocation)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colorList[self.state], self.rectangle)
        screen.blit(self.fontedText, self.textRectangle)


class Menu_TextItem():
    def __init__(self, name, text="notext", textSize=100, mainColor=(128, 128, 128), centerlocation=(0, 0)):
        self.name = name
        self.text = text
        self.textSize = textSize
        self.color = mainColor

        self.centerlocation = centerlocation
        self.fontedTextList = [
            pygame.font.SysFont("arial", self.textSize).render(self.text, True, self.color)]
        self.width = self.fontedTextList[0].get_width()
        self.height = self.fontedTextList[0].get_height()
        self.rectangle = pygame.rect.Rect(0, 0, self.width, self.height)
        self.rectangle.center = centerlocation


    def draw(self, screen):
        screen.blit(self.fontedTextList[0], self.rectangle)


class Menu():
    def __init__(self, screenrect=pygame.rect.Rect(0, 0, 0, 0)):
        self.isActive = False
        self.objectList = []
        self.clock = pygame.time.Clock()
        self.screenrect = screenrect
        self.initilize()

    def initilize(self):

        self.btnRestart = Menu_ButtonItem(name="button1", text="Restart", width=200, height=50, textSize=50,
                                          mainColor=(220, 20, 60), onMouseOverColor=(0, 205, 205),
                                          centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 120))
        self.objectList.append(self.btnRestart)

        self.btnResume = Menu_ButtonItem(name="button2", text="Resume", width=200, height=50, textSize=50,
                                         mainColor=(220, 20, 60), onMouseOverColor=(0, 205, 205),
                                         centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 60))
        self.objectList.append(self.btnResume)

        self.btnExit = Menu_ButtonItem(name="button3", text="exit", width=100, height=50, textSize=50,
                                       mainColor=(220, 20, 60), onMouseOverColor=(0, 205, 205),
                                       centerlocation=(self.screenrect.center[0], self.screenrect.center[1]))
        self.objectList.append(self.btnExit)

    def reset_state(self):
        for item in self.objectList:
            item.state = 0

    def runMenu(self, screen):
        self.reset_state()
        self.isActive = True
        screenshoot = screen.copy()
        while self.isActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameYilan.crashed = True
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.isActive = False
                elif event.type == pygame.MOUSEMOTION:
                    self.checkMouseOver(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onMouseDown(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.onMouseUp(pygame.mouse.get_pos())
                elif event == self.btnResume.mouseDownEvent:
                    self.isActive = False
                elif event == self.btnExit.mouseDownEvent:
                    gameYilan.crashed = True
                    return True
                elif event == self.btnRestart.mouseDownEvent:
                    gameYilan.yilanLength=0
                    gameYilan.yilanUzunlugu=[]#yilanın boyu sıfırlanacak
                    gameYilan.puan=0 #puan sıfırlanacak
                    game() #oyun tekrar başlayacak

                screen.blit(screenshoot, (0, 0))
                self.draw(screen)
                pygame.display.update()
                self.clock.tick(60)
        return False

    def checkMouseOver(self, location):
        for item in self.objectList:
            item.checkMouseOver(location)

    def onMouseDown(self, location):
        for item in self.objectList:
            item.onMouseDown(location)

    def onMouseUp(self, location):
        for item in self.objectList:
            item.onMouseUp(location)

    def draw(self, screen):
        for item in self.objectList:
            item.draw(screen)
class GameOverMenu():
    def __init__(self, screenrect=pygame.rect.Rect(0, 0, 0, 0)):
        self.isActive = False
        self.objectList=[]
        self.text = []
        self.clock = pygame.time.Clock()
        self.screenrect = screenrect
        self.initilize()


    def initilize(self):
        self.gameOverText=Menu_TextItem(name="text1", text="GAME OVER", textSize=50,
                                          mainColor=(220, 20, 60),
                                          centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 200))
        self.text.append(self.gameOverText)
        self.btnRestart = Menu_ButtonItem(name="button2", text="Restart", width=200, height=50, textSize=50,
                                         mainColor=(220, 20, 60), onMouseOverColor=(0, 205, 205),
                                         centerlocation=(self.screenrect.center[0], self.screenrect.center[1] - 60))
        self.objectList.append(self.btnRestart)

        self.btnExit = Menu_ButtonItem(name="button3", text="exit", width=100, height=50, textSize=50,
                                       mainColor=(220, 20, 60), onMouseOverColor=(0, 205, 205),
                                       centerlocation=(self.screenrect.center[0], self.screenrect.center[1]))
        self.objectList.append(self.btnExit)

    def checkMouseOver(self, location):
        for item in self.objectList:
            item.checkMouseOver(location)

    def onMouseDown(self, location):
        for item in self.objectList:
            item.onMouseDown(location)

    def onMouseUp(self, location):
        for item in self.objectList:
            item.onMouseUp(location)

    def runExitMenu(self, screen):

        self.isActive = True
        screenshoot = screen.copy()
        while self.isActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameYilan.crashed= True
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        menu.runMenu(gameDisplay)
                elif event.type == pygame.MOUSEMOTION:
                    self.checkMouseOver(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onMouseDown(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.onMouseUp(pygame.mouse.get_pos())
                elif event == self.btnExit.mouseDownEvent:
                    gameYilan.crashed = True
                    return True
                elif event == self.btnRestart.mouseDownEvent:

                    gameYilan.yilanLength=0
                    gameYilan.yilanUzunlugu=[]#yilanın boyu sıfırlanacak
                    gameYilan.puan=0 #puan sıfırlanacak
                    game() #oyun tekrar başlayacak


                screen.blit(screenshoot, (0, 0))
                self.draw(screen)
                pygame.display.update()
                self.clock.tick(60)
        return False

    def draw(self, screen):
        for t in self.objectList:
            t.draw(screen)

        for t in self.text:
            t.draw(screen)


pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
mavi=(91,163,220)
red=(243,23,11)
gameDisplay.fill(white)

gameYilan = yilan(gameDisplay)
gamePlaneApple = elma(gameDisplay)
gamePlaneApple2 = elma(gameDisplay)
gameDuvar = duvar(gameDisplay)
menu = Menu(gameDisplay.get_rect())
gameOverMenu = GameOverMenu(gameDisplay.get_rect())
start_ticks=pygame.time.get_ticks()
def game():
    mx=0
    my=0

    while not gameYilan.crashed:
        for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
            if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
                gameYilan.crashed = True  #  döngüyü kırar
            if event.type == pygame.KEYDOWN:
            #sayı olarak 5 verme sebebim karelerin arasında beyazlık gorunmesi icin
                if event.key == pygame.K_ESCAPE:
                    gameYilan.crashed = menu.runMenu(gameDisplay)
                if event.key == pygame.K_LEFT:
                    mx  = -gameYilan.bes
                    my  = 0
                elif event.key == pygame.K_RIGHT:
                    mx  =gameYilan.bes
                    my  = 0
                elif event.key == pygame.K_UP:
                    my  = -gameYilan.bes
                    mx  = 0
                elif event.key == pygame.K_DOWN:
                    my = gameYilan.bes
                    mx  = 0

        gameDisplay.fill(white)
        gameYilan.draw(mx, my,gameDisplay)
        gamePlaneApple2.drawApple2(gameDisplay)
        gamePlaneApple.drawApple(gameDisplay)
        gameDuvar.draw(gameDisplay)




        clock.tick(gameYilan.ekran)  #burada saniyede 30 framelik bir yenilenme olacak demektir.
        pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz

    pygame.quit()
    quit()
game()
