import pygame , sys

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

pygame.init()
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

rectangulo_rect = pygame.Rect(0,0,100,100)
redonda_rect = pygame.Rect(50,250,100,100)

# EL tiempo desde pulsacion tecla
tiempo_ultimo_movimiento = 0

# Controlar el movimento
def movimiento(rect,tecla_presionada,tiempo_actual):
    global tiempo_ultimo_movimiento
    # Añadiremos un Colldown
    if tiempo_actual - tiempo_ultimo_movimiento > 5:
        # Controlar direccion
        if tecla_presionada[pygame.K_w]: # Subir
            rect.y -= 1
        elif tecla_presionada[pygame.K_s]: # Bajar
            rect.y += 1

        if tecla_presionada[pygame.K_d]: # Derecha
            rect.x += 1
        elif tecla_presionada[pygame.K_a]: # Izquierda
            rect.x -= 1

        tiempo_ultimo_movimiento = tiempo_actual


while True:

    tiempo = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    raton = pygame.mouse.get_pressed()
    if raton[2]:
        print('Se pulso el raton')
    
    # Llamaremos a la funcion movimiento con la tecla presionada
    teclas = pygame.key.get_pressed()
    movimiento(rectangulo_rect,teclas,tiempo)

    
    pygame.draw.rect(ventana,(255,255,255),rectangulo_rect)
    pygame.draw.circle(ventana, (255,255,255), redonda_rect.center, 50)

    pygame.display.update()

    ventana.fill((0,0,0))
    