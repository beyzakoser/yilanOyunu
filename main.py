import pygame
import random
import time
from  threading import Timer

class yilan():

    def __init__(self,screen):
        self.yilanX=300
        self.yilanY=300
        width=screen.get_width() #800
        height=screen.get_height() #600
        self.yilanUzunlugu=[]

        self.yilanLength=0
        self.rectangle = pygame.rect.Rect(self.yilanX , self.yilanY ,int(width / 40),int(height / 30))


    def draw(self,mx,my,screen): #yılanı cizer
        self.yilanX= self.yilanX + mx*3
        self.yilanY = self.yilanY + my*3
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

        self.ekranGecisi(gameDisplay)
        self.eat()



    def ekranGecisi(self,screen): #ekran arası yılan gecisi icin

        width=screen.get_width()
        height=screen.get_height()
        if self.yilanY>= height:
            self.yilanY= 0
        elif self.yilanY < 0:
            self.yilanY = height-5
        if self.yilanX >= width:
            self.yilanX = 0
        elif self.yilanX < 0:
            self.yilanX = width-5

    def eat(self):
        #elmanın yilanın bulundugu x y konumları arasında olup olmadığının kontrolu
        if gameYilan.yilanX >= gamePlaneApple.rectangle[0] and gameYilan.yilanX <= (gamePlaneApple.rectangle[0])+gamePlaneApple.rectangle[2]:
            if gameYilan.yilanY >= gamePlaneApple.rectangle[1] and gameYilan.yilanY <= (gamePlaneApple.rectangle[1])+gamePlaneApple.rectangle[3]:
                yeni=elma(gameDisplay)
                gamePlaneApple.rectangle[0]=yeni.elmaX
                gamePlaneApple.rectangle[1] = yeni.elmaY

                if gamePlaneApple.secilen== gamePlaneApple.elmalar[0]: #1artıran
                    self.yilanLength += 1
                elif gamePlaneApple.secilen== gamePlaneApple.elmalar[1]: #1azaltan
                    self.yilanLength -= 1
                elif gamePlaneApple.secilen== gamePlaneApple.elmalar[2]: #3artıran
                    self.yilanLength += 3


                gamePlaneApple.randomElma() #elma yendikten sonra random farklı elma gelmesi icin



class elma():

    def __init__(self,screen):

        width=screen.get_width() #800
        height=screen.get_height() #600
        self.elmaX = round(random.randrange(30, width -50))
        self.elmaY = round(random.randrange(30, height -50))
        self.rectangle = pygame.rect.Rect(self.elmaX , self.elmaY ,int(width / 13),int(height / 13))
        self.elmalar = ["1ArtıranElma", "1AzaltanElma", "3ArtıranElma"]#, "hızlı", "olduren", "salyangoz"]

        self.randomElma()

    def drawApple(self,screen):


        self.image = pygame.image.load("images/" + self.secilen + ".png")

        self.image= pygame.transform.scale(self.image, (self.rectangle[2],self.rectangle[3]))
        screen.blit(self.image, self.rectangle)

    def randomElma(self):

        self.secilen = random.choice(self.elmalar)


pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')


crashed = False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
mavi=(91,163,220)
gameDisplay.fill(white)


gameYilan=yilan(gameDisplay)
gamePlaneApple=elma(gameDisplay)


mx=0
my=0

while not crashed:
    for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
            crashed = True  #  döngüyü kırar
        if event.type == pygame.KEYDOWN:
            #sayı olarak 5 verme sebebim karelerin arasında beyazlık gorunmesi icin
            if event.key == pygame.K_LEFT:
                mx  = -5
                my  = 0
            elif event.key == pygame.K_RIGHT:
                mx  =5
                my  = 0
            elif event.key == pygame.K_UP:
                my  = -5
                mx  = 0
            elif event.key == pygame.K_DOWN:
                my = 5
                mx  = 0


    gameDisplay.fill(white)
    gameYilan.draw(mx, my,gameDisplay)
    gamePlaneApple.drawApple(gameDisplay)


    clock.tick(20)  #burada saniyede 30 framelik bir yenilenme olacak demektir.
    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz

pygame.quit()
quit()
