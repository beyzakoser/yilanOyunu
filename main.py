import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600)) #ekran boyutu
pygame.display.set_caption('Snake')
crashed = False
clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz
while not crashed:
    for event in pygame.event.get():  # oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT:  # olay tipine göre karar mekanizmalarını kuruyoruz
            crashed = True  #  döngüyü kırar


        #print(event)  #mouse olayını yazıyor ekrana

    pygame.display.update()  # her döngüde ekranı tekrar çizdiriyoruz
    clock.tick(60)  #burada saniyede 60 framelik bir yenilenme olacak demektir.

pygame.quit()
quit()
