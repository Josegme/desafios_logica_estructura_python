from random import choice 
#esta bueno leer la documentación de cada librearia para saber un poco lo que contiene
#igualmente tenemos que investigar los métodos que podemos utilizar para cada problema y donde podemos encontrarlos.

# Lista de palabras
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']

# Listas para letras correctas e incorrectas
letras_correctas = []
letras_incorrectas = []

# Contadores
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    """Elige una palabra al azar y devuelve la palabra junto con la cantidad de letras únicas."""
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))  # Contamos las letras únicas en la palabra
    return palabra_elegida, letras_unicas

def pedir_letra():
    """Solicita una letra al usuario y valida que sea una sola letra del abecedario."""
    letra_elegida = ''
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while True:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            return letra_elegida
        print('No has elegido una letra válida. Intenta de nuevo.')

def mostrar_nuevo_tablero(palabra_elegida):
    """Muestra la palabra oculta con guiones y letras adivinadas."""
    lista_oculta = [letra if letra in letras_correctas else '-' for letra in palabra_elegida]
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias, letras_unicas):
    """Verifica si la letra está en la palabra y actualiza las listas y contadores."""
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1  # Se cuenta la cantidad de letras únicas descubiertas
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        return perder(palabra_oculta), vidas, coincidencias
    elif coincidencias == letras_unicas:
        return ganar(palabra_oculta), vidas, coincidencias

    return False, vidas, coincidencias  # El juego sigue

def perder(palabra_real):
    """Muestra el mensaje de derrota."""
    print(f'Te has quedado sin vidas. La palabra era: {palabra_real}')
    return True

def ganar(palabra_descubierta):
    """Muestra el mensaje de victoria y la palabra completa."""
    mostrar_nuevo_tablero(palabra_descubierta)
    print('¡Felicitaciones! Has encontrado la palabra.')
    return True

# Elegimos una palabra al azar
palabra, letras_unicas = elegir_palabra(palabras)

# Bucle principal del juego
while not juego_terminado:
    print('\n' + '*' * 30)
    mostrar_nuevo_tablero(palabra)
    print(f'\nLetras incorrectas: {", ".join(letras_incorrectas)}')
    print(f'Vidas restantes: {intentos}')
    print('*' * 30 + '\n')

    letra = pedir_letra()

    if letra in letras_correctas or letra in letras_incorrectas:
        print("Ya elegiste esa letra, intenta con otra.")
        continue  # Evita perder intentos con letras repetidas

    juego_terminado, intentos, aciertos = chequear_letra(letra, palabra, intentos, aciertos, letras_unicas)
