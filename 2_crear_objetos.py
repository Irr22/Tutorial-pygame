import pygame , sys

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

pygame.init()
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

# Crearemos un rectangulo (en 0x 0y y 100 ancho y alto)
rectangulo_rect = pygame.Rect(0,0,100,100)

# Crearemos una redonda (en 50x 250y)
redonda_rect = pygame.Rect(50,250,100,100) # Los dos ultimos numeros son el radio por 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Dibujar el rectangulo en ventana de color blanco
    pygame.draw.rect(ventana,(255,255,255),rectangulo_rect)

    # Dibujar el círculo
    pygame.draw.circle(ventana, (255,255,255), redonda_rect.center, 50)

    # Actualizamos la pantalla
    pygame.display.update()
    