import pygame

class yilan():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.imageOrder=0 #görüntü sırası
        width=screen.get_width()
        height=screen.get_height()
        self.rectange=[200,int(height/2),int(width/10),int(height/10)]


    def draw(self,screen,mx,my):
        self.imageOrder = self.imageOrder % 3 + 1
        self.image=pygame.image.load("images/kafa("+str(self.imageOrder)+").png")
        self.rectange[0]=self.rectange[0]+mx*3
        self.rectange[1]=self.rectange[1]+my*3
        self.image= pygame.transform.scale(self.image, (self.rectange[2],self.rectange[3]))
        screen.blit(self.image, self.rectange)

    def drawYukari(self, screen, mx, my):
        self.imageOrder = self.imageOrder % 3 + 1
        self.image = pygame.image.load("images/kafaY(" + str(self.imageOrder) + ").png")
        self.rectange[0] = self.rectange[0] + mx * 3
        self.rectange[1] = self.rectange[1] + my * 3
        self.image = pygame.transform.scale(self.image, (self.rectange[2], self.rectange[3]))
        screen.blit(self.image, self.rectange)


pygame.init()

gameDisplay = pygame.display.set_mode((870,650))
pygame.display.set_caption('Snake')


crashed = False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

white = (255, 255,255)
black = (0,0,0)
gameDisplay.fill(white)

myimage = pygame.image.load("images/acikKahve.jpg") #beyaz olanda güzel oldu sonra tekrar bak
backGraundImage= pygame.transform.scale(myimage, (gameDisplay.get_width(), gameDisplay.get_height()))
gamePlane=yilan(gameDisplay)
mx=0
my=0
while not crashed:
    for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
            crashed = True  #  döngüyü kırar
        if event.type == pygame.KEYDOWN:
            gamePlane.drawYukari(gameDisplay, mx, my)
            if event.key == pygame.K_UP:
                gamePlane.drawYukari(gameDisplay, mx, my)
                my=-1
            if event.key == pygame.K_DOWN:
                my=1
            if event.key == pygame.K_LEFT:
                mx=-1
            if event.key == pygame.K_RIGHT:
                mx=1
        if event.type == pygame.KEYUP:
            gamePlane.drawYukari(gameDisplay, mx, my)
            if event.key == pygame.K_UP:
                gamePlane.drawYukari(gameDisplay, mx, my)

                my=0

            if event.key == pygame.K_DOWN:
                my=0
            if event.key == pygame.K_LEFT:
                mx=0
            if event.key == pygame.K_RIGHT:
                mx=0

    gameDisplay.blit(backGraundImage, (0, 0))
    mouse_position = pygame.mouse.get_pos()
    gamePlane.draw(gameDisplay, mx, my)



    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz
    clock.tick(20)  #burada saniyede 60 framelik bir yenilenme olacak demektir.

pygame.quit()
quit()
