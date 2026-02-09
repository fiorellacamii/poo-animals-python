class animales: 
    
    def __init__(self, nombre, especie, edad, color, sonido, peso, genero):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.sonido = sonido
        self.peso = peso
        self.genero = genero

        self.energia = 100
        self.hambre = 0

    
    def atributos(self):
        print(self.nombre)
        print("Especie: ", self.especie)
        print("Edad: ", self.edad, "Años")
        print("Color: ", self.color)
        print("Sonido: ", self.sonido)
        print("Peso: ", self.peso, "Kg")
        print("Energia: ", self.energia)
        print("Hambre: ", self.hambre)
        print("Genero: ", self.genero)
 
    def hacer_sonido(self):
        print(self.nombre, "Dice: ", self.sonido)

    def moverse(self):
        if self.energia >= 10:
            self.energia -= 10
            self.hambre += 5
            print(self.nombre, "Se ha movido y ahora tiene", self.energia,  "de energia")
        else:
            print(self.nombre, "Esta muy cansado")

    def dormir(self):
        self.energia = 100
        print(self.nombre, "Ha dormido y recupero toda la energia")

    def jugar(self):
        if self.energia >= 20:
            self.energia -= 20
            self.hambre += 10
            print(self.nombre, "Ha jugado y ahora tiene", self.energia, "de energia")

    def cumplir_años(self):
        self.edad += 1
        print(self.nombre, "ahora tiene", self.edad, "años")

    def comer(self):
        self.hambre -= 15
        if self.hambre <0:
            self.hambre = 0
        self.peso += 0.2
        print(self.nombre, "Comio y ahora pesa", self.peso, "Kg")

class gato(animales):

    def __init__(self, nombre, edad, color, peso, genero):
        super().__init__(nombre, "Gato", edad, color, "Miau", peso, genero)

    def hacer_sonido(self):
        print(self.nombre, "dice: " "MIAUUUUUUU")
    
    def ronronear(self):
        print(self.nombre, "hace: " "prrr")

class perro(animales):
    
    def __init__(self, nombre, edad, color, peso, genero):
        super().__init__(nombre, "Perro", edad, color, "Guau", peso, genero)

    def hacer_sonido(self):
        print(self.nombre, "dice: " "Guau guauu")

    def cuidar_casa(self):
        print(self.nombre, "Esta cuidando la casa")

class vaca(animales):

    def __init__(self, nombre, edad, color, peso, genero):
        super().__init__(nombre, "Vaca", edad, color, "Muu", peso, genero)
    
    def hacer_sonido(self):
        print(self.nombre, "Dice: " "Muuu")

    def dar_leche(self):
        print(self.nombre, "dio leche")

class gallina(animales):
    def __init__(self, nombre, edad, color, peso, genero):
        super().__init__(nombre, "Gallina", edad, color, "Cooc coo co", peso, genero)

    def hacer_sonido(self):
        print(self.nombre, "Dice: " "Kikirikiii")

    def poner_huevo(self):
        print(self.nombre, "Ha puesto un huevo")

gallinita = gallina("edgardo", 10, "Negra", 1, "Hembra")
vaquita = vaca("Perla", 10, "Blanca", 150, "Hembra")
gatico = gato("Tom", 2 ,"Blanco con negro", 3, "Macho")
perrito = perro("Luna", 4, "Marron", 10, "Hembra")

animal_actual = None

while True:
    print("\n****Menu principal****")
    print("1. Seleccionar Vaca")
    print("2. Seleccionar Gallina")
    print("3. Seleccionar Gato")
    print("4. Seleccionar Perro")
    print("0. Salir")

    opcion = int(input("Elige: "))

    if opcion == 1:
        animal_actual = vaquita

    elif opcion == 2:
        animal_actual = gallinita

    elif opcion == 3:
        animal_actual = gatico

    elif opcion == 4:
        animal_actual = perrito

    elif opcion == 0:
        print("adios ")
        break
    else:
        print("Opcion Invalida")
        continue

    while True:
        print("Menu de: ",animal_actual.nombre)
        print("1. Hacer sonido")
        print("2. Moverse")
        print("3. Comer")
        print("4. Dormir")
        print("5. Jugar")
        print("6. Cumplir años")
        print("7. Ver atributos")
        print("8. Accion especial")
        print("0. Volver")

        opcion2= int(input("Elige accion: "))

        if opcion2 == 1:
            animal_actual.hacer_sonido()

        elif opcion2 == 2:
            animal_actual.moverse()

        elif opcion2 == 3:
            animal_actual.comer()

        elif opcion2 == 4:
            animal_actual.dormir()

        elif opcion2 == 5:
            animal_actual.jugar()

        elif opcion2 == 6:
            animal_actual.cumplir_años()
        
        elif opcion2 == 7:
            animal_actual.atributos()
        
        elif opcion2 == 8: 
            
            if animal_actual.especie == "Vaca":
                animal_actual.dar_leche()

            elif animal_actual.especie == "Gato":
                animal_actual.ronronear()

            elif animal_actual.especie == "Gallina":
                animal_actual.poner_huevo()

            elif animal_actual.especie == "Perro":
                animal_actual.cuidar_casa()
            else:
                print("Este animal no tiene accion especial")
        
        elif opcion2 == 0: 
            break

        else: 
            print("No valido")
