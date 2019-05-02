import pygame
import random
import time
class duvar():
    def __init__(self,screen):
        self.duvarX=660
        self.duvarY=-20
        self.duvar2X=-20
        self.duvar2Y=430
        width=screen.get_width() #800
        height=screen.get_height() #600
        self.rectangle= pygame.rect.Rect(self.duvarX , self.duvarY ,int(width / 5),int(height / 3))

        self.rectangle2 = pygame.rect.Rect(self.duvar2X, self.duvar2Y, int(width / 5), int(height / 3))

    def draw(self,screen):
        self.image = pygame.image.load("images/duvar.png")
        self.image = pygame.transform.scale(self.image, (self.rectangle[2], self.rectangle[3]))
        self.image2 = pygame.image.load("images/duvar2.png")
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
        if (gameYilan.yilanX >= gamePlaneApple.rectangle[0] and gameYilan.yilanX <= (gamePlaneApple.rectangle[0])+gamePlaneApple.rectangle[2]
                and gameYilan.yilanY >= gamePlaneApple.rectangle[1] and gameYilan.yilanY <= (gamePlaneApple.rectangle[1])+gamePlaneApple.rectangle[3]):



            yeni=elma(gameDisplay)
            gamePlaneApple.rectangle[0]=yeni.elmaX
            gamePlaneApple.rectangle[1] = yeni.elmaY
            self.yilanLength += 1
        elif(gameYilan.yilanX >= gamePlaneApple2.rectangle2[0] and gameYilan.yilanX <= (gamePlaneApple2.rectangle2[0]) + gamePlaneApple2.rectangle2[2]
                and gameYilan.yilanY >= gamePlaneApple2.rectangle2[1] and gameYilan.yilanY <= (gamePlaneApple2.rectangle2[1]) + gamePlaneApple2.rectangle2[3]):

            yeni = elma(gameDisplay)
            gamePlaneApple2.rectangle2[0] = yeni.elma2X
            gamePlaneApple2.rectangle2[1] = yeni.elma2Y



            if gamePlaneApple2.secilen== gamePlaneApple.elmalar[0]: #1azaltan
                    self.yilanLength -= 1
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[1]: #3artıran
                    self.yilanLength += 3
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[2]: #hizlandiran
                    self.ekran=70


           # elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[3]: #olduren
            #        self.crashed=True #bu kısımda ekrana mesaj verdir restart butonu ekle

            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[4]: #yavaslatan
                   self.ekran=5



            gamePlaneApple2.randomElma() #elma yendikten sonra random farklı elma gelmesi icin



class elma():

    def __init__(self,screen):

        width=screen.get_width() #800
        height=screen.get_height() #600
        self.elmaX = round(random.randrange(30, width -50))
        self.elmaY = round(random.randrange(30, height -50))
        self.elma2X = round(random.randrange(30, width -50)) #yeşilden farlı olan elma
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
        #self.image = pygame.image.load("images/1AzaltanElma.png")
        self.image2 = pygame.image.load("images/" + self.secilen + ".png")

        self.image2= pygame.transform.scale(self.image2, (self.rectangle2[2],self.rectangle2[3]))
        screen.blit(self.image2, self.rectangle2)


    def randomElma(self):

        self.secilen = random.choice(self.elmalar)


pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')

crashed=False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
mavi=(91,163,220)
gameDisplay.fill(white)


gameYilan=yilan(gameDisplay)
gamePlaneApple=elma(gameDisplay)
gamePlaneApple2=elma(gameDisplay)
gameDuvar=duvar(gameDisplay)

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
    gamePlaneApple2.drawApple2(gameDisplay)
    gamePlaneApple.drawApple(gameDisplay)
    gameDuvar.draw(gameDisplay)


    clock.tick(gameYilan.ekran)  #burada saniyede 30 framelik bir yenilenme olacak demektir.
    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz

pygame.quit()
quit()
