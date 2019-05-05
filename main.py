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


    def draw(self,mx,my,screen): #yılanı cizer
        self.yilanX= self.yilanX + mx*7
        self.yilanY = self.yilanY + my*7
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
            gameYilan.crashed = True


        self.ekranGecisi(gameDisplay)
        self.eat()
        mesaj(gameDisplay, gameYilan.yilanLength*5)



    def ekranGecisi(self,screen): #ekran arası yılan gecisi icin

        width=screen.get_width() #800
        height=screen.get_height() #600
        if self.yilanY>= height:
            self.yilanY= 0
        elif self.yilanY < 0:
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
                    self.yilanLength -= 1
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[1]: #3artıran
                    self.yilanLength += 3
            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[2]: #hizlandiran
                    self.ekran=200


           # elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[3]: #olduren
            #        self.crashed=True #bu kısımda ekrana mesaj verdir restart butonu ekle

            elif gamePlaneApple2.secilen== gamePlaneApple.elmalar[4]: #yavaslatan
                   self.ekran=5



            gamePlaneApple2.randomElma() #elma yendikten sonra random farklı elma gelmesi icin



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

    text = yaziTipi.render("Skor: "+str(skor)+" /100", True, black)
    screen.blit(text, [screen.get_width()/2,0])#ekranın ortasında olması için
    if skor==100:gameYilan.crashed=True #skor 100 ü gecerse oyun bitecek



pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')

#crashed=False
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
start_ticks=pygame.time.get_ticks()
while not gameYilan.crashed:


    for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
            gameYilan.crashed = True  #  döngüyü kırar
        if event.type == pygame.KEYDOWN:
            #sayı olarak 5 verme sebebim karelerin arasında beyazlık gorunmesi icin
            if event.key == pygame.K_LEFT:
                mx  = -3
                my  = 0
            elif event.key == pygame.K_RIGHT:
                mx  =3
                my  = 0
            elif event.key == pygame.K_UP:
                my  = -3
                mx  = 0
            elif event.key == pygame.K_DOWN:
                my = 3
                mx  = 0

    gameDisplay.fill(white)
    gameYilan.draw(mx, my,gameDisplay)
    gamePlaneApple2.drawApple2(gameDisplay)
    gamePlaneApple.drawApple(gameDisplay)
    gameDuvar.draw(gameDisplay)

    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    yaziTipi = pygame.font.SysFont("arial", 20)
    contador = yaziTipi.render("time: " + str(seconds)+" /100.0", True, black)
    gameDisplay.blit(contador, [0, 0])
    if seconds>100: break #bu kısımda menu ekranına geri dönecek

    clock.tick(gameYilan.ekran)  #burada saniyede 30 framelik bir yenilenme olacak demektir.
    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz

pygame.quit()
quit()
