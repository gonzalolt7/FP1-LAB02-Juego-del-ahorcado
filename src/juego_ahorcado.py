import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    res = ""
    for c in cadena:
        if c == "á" or c == "ä": # c in "áä" tambien vale
            res += "a"
        elif c in "éë":
            res += "e"
        elif c in "íï":
            res += "i"
        elif c in "úü":
            res += "u"
        elif c in "óö":
            res += "o"
        else:
            res += c
    return res

def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    palabra_oculta=""
    for k in palabra_secreta:
        if k in letras_usadas:
            palabra_oculta += k
        else:
            palabra_oculta += "_"
    return palabra_oculta

def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" in palabra_enmascarada: 
        return False 
    else:
       return True
    
def mostrar_estado(palabra_enmascarada,letras_usadas,intentos_restantes):
    print(f'Estado: {"".join(palabra_enmascarada)}')
    if len(letras_usadas) == 0:
        print(f"Letras usadas: ninguna")
    else: 
        print(f"Letras usadas: {letras_usadas}")

    print(f"Le quedan: {intentos_restantes}")
    
    return mostrar_estado

def pedir_letra(letras_usadas):
    letra=input("Introduzca una letra: ")
    if len(letra)>1:
        print("debes poner una sola letra")
    elif letra.isdigit():
        print("debe ser una una letra")
    elif letra in letras_usadas:
        print("esa letra ya la has usado")
    while len(letra)>1 or letra.isalpha() or letra == letras_usadas:
        letra
    return letra


    

