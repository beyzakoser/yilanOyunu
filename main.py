import pygame

class yilan():
    def __init__(self,screen):
        self.yilanX=300
        self.yilanY=300

    def draw(self,screen,mx,my): #yılanı cizer
        self.yilanX= self.yilanX + mx * 6
        self.yilanY = self.yilanY + my * 6
        pygame.draw.rect(gameDisplay, mavi, [self.yilanX, self.yilanY, 20, 20])

    def ekranGecisi(self,screen): #ekran arası gecis icin

        width=screen.get_width()
        height=screen.get_height()
        if self.yilanY>= height:
            self.yilanY= 0
        elif self.yilanY < 0:
            self.yilanY = height-1
        if self.yilanX >= width:
            self.yilanX = 0
        elif self.yilanX < 0:
            self.yilanX = width-1



pygame.init()

gameDisplay = pygame.display.set_mode((870,650))
pygame.display.set_caption('Snake')


crashed = False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
mavi=(91,163,220)
gameDisplay.fill(white)


gamePlane=yilan(gameDisplay)
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
    gamePlane.draw(gameDisplay,mx,my)
    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz
    clock.tick(30)  #burada saniyede 30 framelik bir yenilenme olacak demektir.

pygame.quit()
quit()
