import pygame
import random
import time

class yilan():

    def __init__(self):
        self.yilanX=300
        self.yilanY=300


    def draw(self,mx,my): #yılanı cizer
        self.yilanX= self.yilanX + mx * 5
        self.yilanY = self.yilanY + my * 5
        pygame.draw.rect(gameDisplay, mavi, [self.yilanX, self.yilanY, 20, 20])

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

class elma():
    def __init__(self,screen):

        width=screen.get_width() #800
        height=screen.get_height() #600
        self.elmaX = round(random.randrange(30, width -50))
        self.elmaY = round(random.randrange(30, height -50))
        self.rectangle = pygame.rect.Rect(self.elmaX , self.elmaY ,int(width / 13),int(height / 13))

    def drawApple(self,screen):
        self.image = pygame.image.load("images/1ArtıranElma.png")
        self.image= pygame.transform.scale(self.image, (self.rectangle[2],self.rectangle[3]))
        screen.blit(self.image, self.rectangle)

        #pygame.draw.rect(gameDisplay, black, [self.elmaX, self.elmaY, 30, 30])

    def eat(self):
        if gamePlane.yilanX >= self.rectangle[0] and gamePlane.yilanX <= (self.rectangle[0])+self.rectangle[2]:
            if gamePlane.yilanY >= self.rectangle[1] and gamePlane.yilanY <= (self.rectangle[1])+self.rectangle[3]:

                yeni=elma(gameDisplay)
                self.rectangle[0]=yeni.elmaX
                self.rectangle[1] = yeni.elmaY



pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')


crashed = False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
mavi=(91,163,220)
gameDisplay.fill(white)


gamePlane=yilan()
gamePlaneApple=elma(gameDisplay)
mx=0
my=0

while not crashed:
    for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
            crashed = True  #  döngüyü kırar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mx  = -1
                my  = 0
            elif event.key == pygame.K_RIGHT:
                mx  = 1
                my  = 0
            elif event.key == pygame.K_UP:
                my  = -1
                mx  = 0
            elif event.key == pygame.K_DOWN:
                my = 1
                mx  = 0


    gameDisplay.fill(white)
    gamePlane.ekranGecisi(gameDisplay)
    gamePlane.draw(mx, my)
    gamePlaneApple.drawApple(gameDisplay)

    gamePlaneApple.eat()


    clock.tick(30)  #burada saniyede 30 framelik bir yenilenme olacak demektir.
    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz

pygame.quit()
quit()
