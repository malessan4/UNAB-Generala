import random


class Dado:
# para que el dado ya inicialice con un numero random
    def __init__(self):
        self.valor = random.randint(1, 6)
# metodo de tirar dado con valor random
    def tirar(self):
        self.valor = random.randint(1, 6)


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_final = 0

    def jugar_turno(self):
        dados = [Dado() for _ in range(5)]
        print(f"TIRADA ACTUAL DE {self.nombre}: {[dado.valor for dado in dados]}")

# Para que siempre me diga que combinacion tengo y que puntaje obtengo
        conteo, regla = JuegoPuntaje.contar_repetidos([dado.valor for dado in dados])
        puntaje = JuegoPuntaje.calcular_puntaje(conteo, regla)
        print(f"Combinación actual de {self.nombre}: {regla}")
        print(f"Puntaje de {self.nombre} con esta combinación: {puntaje}")
        

# Logica para los turnos para cada jugador
        
        for turnos in range(3):
            dados_a_cambiar = input(f"{self.nombre}, ¿qué dados quieres cambiar? (escribe los numeros de los dados a cambiar seguidos de espacio, o 'nada' para no cambiar nada): Por ejemplo: Mi tirada dio esto (5, 3, 1, 3, 5) y quiero cambiar el 3 el 1 el 3, escribo (2 3 4) ")
            if dados_a_cambiar.lower() != 'nada':
                dados_a_cambiar = list(map(int, dados_a_cambiar.split()))
                for i in dados_a_cambiar:
                    dados[i-1].tirar()
                print(f"TIRADA ACTUAL DE {self.nombre}: {[dado.valor for dado in dados]}")

                conteo, regla = JuegoPuntaje.contar_repetidos([dado.valor for dado in dados])
                puntaje = JuegoPuntaje.calcular_puntaje(conteo, regla)
                print(f"Combinación actual de {self.nombre}: {regla}")
                print(f"Puntaje de {self.nombre} con esta combinación: {puntaje}")

# Como obtengo el resultado final                
        conteo, regla = JuegoPuntaje.contar_repetidos([dado.valor for dado in dados])
        print(f"Resultado final de {self.nombre}: {[dado.valor for dado in dados]}")
        print(f"Regla de puntuación: {regla}")

        puntaje = JuegoPuntaje.calcular_puntaje(conteo, regla)
        self.puntaje_final += puntaje
        print(f"Puntaje total de {self.nombre}: {self.puntaje_final}")

# Para manejar la lógica de puntuación
class JuegoPuntaje:

    def contar_repetidos(tirada):
        conteo = {}
        for valor in tirada:
            conteo[valor] = conteo.get(valor, 0) + 1

        max_count = max(conteo.values())
        if max_count == 5:
            regla = "GENERALA"
        elif max_count == 4:
            regla = "POKER"
        elif max_count == 3:
            if len(conteo) == 2:
                regla = "FULL"
            else:
                regla = "TRIO"
        elif max_count == 2:
            if len(conteo) == 3:
                regla = "DOS PARES"
            else:
                regla = "PAR"
        else:
            regla = "NINGUNA"

        return conteo, regla


    def calcular_puntaje(conteo, regla):
        puntaje = 0
        if regla == "GENERALA":
            puntaje = 50
        elif regla == "POKER":
            puntaje = 40
        elif regla == "FULL":
            puntaje = 30
        elif regla == "ESCALERA":
            puntaje = 20
        elif regla == "TRIO":
            puntaje = 10
        elif regla == "DOS PARES":
            puntaje = 5
        elif regla == "PAR":
            puntaje = 1

        return puntaje



def jugar_generala():
    cantidad_jugadores = int(input('¿Cuántos jugadores son? '))
    if 0 < cantidad_jugadores <= 5:
        jugadores = []
        for i in range(cantidad_jugadores):
            nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
            jugador = Jugador(nombre)
            jugadores.append(jugador)

        print('¡Comencemos el juego de Generala!')

        for jugador in jugadores:
            jugador.jugar_turno()

        # Calcular puntaje final de cada jugador
        puntajes_finales = {jugador.nombre: jugador.puntaje_final for jugador in jugadores}

        # Ordenar la tabla de posiciones de mayor a menor puntaje
        tabla_posiciones = sorted(puntajes_finales.items(), key=lambda x: x[1], reverse=True)

        print("\nTabla de Posiciones:")
        for i, (nombre, puntaje) in enumerate(tabla_posiciones, start=1):
            print(f"{i}. {nombre}: {puntaje} puntos")

        if len(tabla_posiciones) > 1:
            # Verificar si hay un solo ganador o un empate
            if tabla_posiciones[0][1] != tabla_posiciones[1][1]:
                ganador = tabla_posiciones[0][0]
                print(f"FELICIDADES {ganador} HAS GANADO!")
            else:
                print("¡Empate entre algunos jugadores!")
        else:
            print(f"FELICIDADES {tabla_posiciones[0][0]} HAS GANADO!")

    else:
        print("Lo siento, este juego solo admite de 1 a 5 jugadores.")


jugar_generala()
