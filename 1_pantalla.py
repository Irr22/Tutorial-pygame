import pygame , sys

# Definiremos los tamaños de la pantalla
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

# Iniciaremos pygame
pygame.init()

# Crearemos la ventana
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

# Bucle principal
while True:
    for event in pygame.event.get():
        # Detectamos si se cierra la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            