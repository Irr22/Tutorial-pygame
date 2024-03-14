import pygame , sys, random

ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

pygame.init()
ventana = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))

radio = 5 # Creamos una variable para el radio de la redonda
fuente = pygame.font.SysFont(None, 36) # Definimos la fuente para mostrar la puntuacion
puntos = 0 # Cada vez que mate augmentara

# Quitamos el rectangulo de aqui
# Rectangulo_rect = pygame.Rect(0,0,100,100)
redonda_rect = pygame.Rect(100 - radio,100 - radio,radio * 2,radio * 2)

# Crear carpeta donde estaran los enemigos
enemigos = []

tiempo_ultimo_movimiento = 0

def movimiento(rect,tecla_presionada,tiempo_actual,rect_colisionado):
    global tiempo_ultimo_movimiento
    if tiempo_actual - tiempo_ultimo_movimiento > 5:
        # Comprovar si la posicion de despues sale de la pantalla
        if tecla_presionada[pygame.K_w] and not (rect.top <= 0): # Que no salga por arriba
            rect.y -= 1
        elif tecla_presionada[pygame.K_s] and not (rect.bottom >= ALTO_PANTALLA): # Que no salga por abajo
            rect.y += 1
        if tecla_presionada[pygame.K_d] and not (rect.right >= ANCHO_PANTALLA): # Que no salga por la izquierda
            rect.x += 1
        elif tecla_presionada[pygame.K_a] and not (rect.left <= 0): # Que no salga por la derecha
            rect.x -= 1

        colisiones(rect,rect_colisionado)

        tiempo_ultimo_movimiento = tiempo_actual

def colisiones(rect,rect_colisionado_lista):
    global radio, puntos
    # Recoreremos la lista para buscar si colisiono con algo
    for rect_colisionador in rect_colisionado_lista:
        if rect.colliderect(rect_colisionador):
            rect_colisionador.x = 1000 # lo mandamos fuera de la pantalla
            rect_colisionado_lista.remove(rect_colisionador) # Si colisiona lo borramos de la lista
            radio += .1 # Incrementamos el radio cada vez que colisione
            puntos += 1 # Sumamos puntos
            redonda_rect.height, redonda_rect.width = radio * 2, radio * 2 # Actualizamos el rect
   
while True:
    tiempo = pygame.time.get_ticks()

    # Definir el texto y posicionarlo
    texto_puntuacion = fuente.render(str(puntos), True, (0,255,0))
    texto_puntuacion_rect = texto_puntuacion.get_rect()
    texto_puntuacion_rect.topright = (ANCHO_PANTALLA,10)

    # Comprovar si ahy algun cuadrado en pantalla
    if len(enemigos) <= 0: # Si no ahy ninguno crear uno
        # Crearemos las posiciones y el tamaño aletoria
        ancho = random.randint(10,50)
        y_aleatorio = random.randint(0,ALTO_PANTALLA - ancho)
        x_aleatorio = random.randint(0,ANCHO_PANTALLA - ancho)
        rectangulo_rect = pygame.Rect(x_aleatorio,y_aleatorio,ancho,ancho)
        enemigos.append(rectangulo_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    teclas = pygame.key.get_pressed()
    movimiento(redonda_rect,teclas,tiempo,enemigos) # Camviamos el rectangulo por la lista

    # Dibujar todos los enemigos en pantalla
    for cuadrado in enemigos:
        pygame.draw.rect(ventana,(255,255,255),cuadrado)
    pygame.draw.circle(ventana, (255,255,255), redonda_rect.center, radio) # Canviamos el 50 por radio
    # Imprimir texto en pantalla
    ventana.blit(texto_puntuacion, texto_puntuacion_rect)

    pygame.display.update()

    ventana.fill((0,0,0))
