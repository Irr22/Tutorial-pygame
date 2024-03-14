import pygame , sys

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

pygame.init()
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

rectangulo_rect = pygame.Rect(0,0,100,100)
redonda_rect = pygame.Rect(50,250,100,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Para detectar el raton
    raton = pygame.mouse.get_pressed()
    if raton[2]: # 0 = click izquierdo, 1 = rueda, 2 = click derecho
        print('Se pulso el raton')
    
    # Aqui detectamos si se pulso alguna tecla
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]: # Podeis poner cualquier tecla
        print('Tecla presionada w')

    
    pygame.draw.rect(ventana,(255,255,255),rectangulo_rect)
    pygame.draw.circle(ventana, (255,255,255), redonda_rect.center, 50)

    pygame.display.update()

    ventana.fill((0,0,0))
    