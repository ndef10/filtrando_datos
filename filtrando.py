#Dada la siguiente lista de nombres:

nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

#Separar los nombres en tres grupos: 
# magos, científicos y otros

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

listado_magos =[]
listado_cientificos = []
otros = []

def separar_nombres(nombres):

    for nombre in nombres:
        if nombre in magos:
            listado_magos.append(nombre)

        elif nombre in cientificos:
            listado_cientificos.append(nombre) 

        else:
            otros.append(nombre)

    print("\n") 
    print("Listado de magos") 
    print("================")  

    for mago in listado_magos:
        print(f"{mago}")

    print("\n")
    print("Listado de cientificos")
    print("======================")

    for cientifico in listado_cientificos:
        print(f"{cientifico}")

    print("\n")
    print("Listado de otros")
    print("================")

    for otro in otros:
        print(f"{otro}")
            
separar_nombres(nombres)


#escribir una funcion llamada hacer_grandioso() 
# que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.

def hacer_grandioso(nombres):
    print("\n")
    print("Hacer grandiosos")
    print("==============")

    for nombre in magos:
        print("El gran " + nombre)

hacer_grandioso(nombres)


#Crear una función llamada imprimir_nombres(), 
# que imprime el nombre de cada persona de la lista.

def imprimir_nombres(nombres):
    print("\n")
    print("Imprimir nombres")
    print("================")

    for nombre in nombres:
        print(f"{nombre}")
    print("\n")
    
imprimir_nombres(nombres)