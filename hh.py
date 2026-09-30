import datetime

def saludar():
    print("Hola, Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
resultado = calcular_area_triangulo(10, 5)
print(f"El área del triángulo es: {resultado}")

def saludar_persona(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Raúl", 19)
#No parámetros
def mensaje_bicho():
    print("¡El Bicho siempre aparece en los momentos importantes!")
mensaje_bicho()

def mensaje_chivas():
    print("¡Vamos Chivas!")
mensaje_chivas()
#Parametros 
def jugador_favorito(nombre):
    print("Mi jugador favorito es:", nombre)
jugador_favorito("Cristiano Ronaldo")

def equipo_favorito(equipo):
    print("Mi equipo favorito es:", equipo)
equipo_favorito("Chivas")