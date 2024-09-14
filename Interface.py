import pygame


pygame.init()

pygame.display.set_caption('Physics made Simple')
window_surface = pygame.display.set_mode((800, 600))

white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)




is_running = True

font = pygame.font.Font('/Users/austin/Desktop/Physics Simulator /cream_wish/Cream Wish.ttf',64)
text = font.render('Physics made simple', True, green, blue)

textRect = text.get_rect()

textRect.center = (800 // 2, 600 // 2)


while is_running:

    window_surface.fill(white)
    window_surface.blit(text, textRect)
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False



    pygame.display.update()
