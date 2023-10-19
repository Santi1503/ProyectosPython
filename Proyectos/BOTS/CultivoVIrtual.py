import random

class Cultivo:
    def __init__(self, nombre, tiempo_maduracion):
        self.nombre = nombre
        self.tiempo_maduracion = tiempo_maduracion
        self.dias_crecimiento = 0
        self.cosechable = False

    def crecer(self):
        self.dias_crecimiento += 1
        if self.dias_crecimiento >= self.tiempo_maduracion:
            self.cosechable = True

class Jugador:
    def __init__(self):
        self.cultivos = []

    def plantar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def cosechar(self, cultivo):
        if cultivo and cultivo.cosechable:
            print(f"Has cosechado {cultivo.nombre} después de {cultivo.dias_crecimiento} días.")
            self.cultivos.remove(cultivo)
        else:
            print("Aún no es el momento de cosechar.")

    def esperar(self):
        for cultivo in self.cultivos:
            cultivo.crecer()

def main():
    zanahoria = Cultivo("Zanahoria", 7)
    trigo = Cultivo("Trigo", 5)

    jugador = Jugador()
    dias_pasados = 0

    while True:
        print(f"Días pasados: {dias_pasados}")

        opcion = input("¿Qué deseas hacer? (plantar/cosechar/esperar/salir): ").lower()

        if opcion == "salir":
            break
        elif opcion == "plantar":
            cultivo_elegido = input("¿Qué cultivo deseas plantar? (zanahoria/trigo): ").lower()
            if cultivo_elegido == "zanahoria":
                jugador.plantar_cultivo(zanahoria)
                print(f"Has plantado una zanahoria que tardará {zanahoria.tiempo_maduracion} días en crecer.")
            elif cultivo_elegido == "trigo":
                jugador.plantar_cultivo(trigo)
                print(f"Has plantado trigo que tardará {trigo.tiempo_maduracion} días en crecer.")
            else:
                print("Cultivo no válido.")
        elif opcion == "cosechar":
            cultivo_elegido = input("¿Qué cultivo deseas cosechar? (zanahoria/trigo): ").lower()
            if cultivo_elegido == "zanahoria":
                jugador.cosechar(zanahoria)
            elif cultivo_elegido == "trigo":
                jugador.cosechar(trigo)
            else:
                print("Cultivo no válido.")
        elif opcion == "esperar":
            dias_pasados += 1
            jugador.esperar()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
