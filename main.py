import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600)) #ekran boyutu
pygame.display.set_caption('Snake Game')

gameExit = False

yilan_x = 300
yilan_y = 300

mx = 0
my = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mx  = -5
                my  = 0
            elif event.key == pygame.K_RIGHT:
                mx  = 5
                my  = 0
            elif event.key == pygame.K_UP:
                my  = -5
                mx  = 0
            elif event.key == pygame.K_DOWN:
                my = 5
                mx  = 0

    yilan_x += mx
    yilan_y += my

#bu kısım diğer ekrandan çıkabilmesi için
    if yilan_y >= 600: yilan_y=0
    elif yilan_y <0: yilan_y=599
    if yilan_x>=800: yilan_x=0
    elif yilan_x<0 : yilan_x=799

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [yilan_x, yilan_y, 20, 20])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()