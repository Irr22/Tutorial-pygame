import pygame , sys

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

pygame.init()
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

rectangulo_rect = pygame.Rect(0,0,100,100)
redonda_rect = pygame.Rect(50,250,100,100)

tiempo_ultimo_movimiento = 0

def movimiento(rect,tecla_presionada,tiempo_actual,rect_colisionado):
    global tiempo_ultimo_movimiento
    if tiempo_actual - tiempo_ultimo_movimiento > 5:
        if tecla_presionada[pygame.K_w]:
            rect.y -= 1
        elif tecla_presionada[pygame.K_s]:
            rect.y += 1

        if tecla_presionada[pygame.K_d]:
            rect.x += 1
        elif tecla_presionada[pygame.K_a]:
            rect.x -= 1

        # Comprobar si el rect colisiono con algun rect
        colisiones(rect,rect_colisionado)

        tiempo_ultimo_movimiento = tiempo_actual


# Controlar las colisiones
def colisiones(rect,rect_colisionado):
    # Si el rectangulo que se mueve colisiona con el otro, el otro deseparecera
    if rect.colliderect(rect_colisionado):
        rect_colisionado.x = 1000



while True:

    tiempo = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    raton = pygame.mouse.get_pressed()
    if raton[2]:
        print('Se pulso el raton')
    
    teclas = pygame.key.get_pressed()
    movimiento(redonda_rect,teclas,tiempo,rectangulo_rect)

    
    pygame.draw.rect(ventana,(255,255,255),rectangulo_rect)
    pygame.draw.circle(ventana, (255,255,255), redonda_rect.center, 50)

    pygame.display.update()

    ventana.fill((0,0,0))
    