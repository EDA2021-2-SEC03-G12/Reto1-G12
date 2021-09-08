
import config as cf
import sys
import controller
from collections import OrderedDict
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido a MoMA\'S DATA")
    print("1 - Cargar información en el catálogo")
    print("2 - Listar cronológicamente los artistas")
    print("3 - Listar cronológicamente las adquisiciones ")
    print("4 - Clasificar las obras de un artista por técnica")
    print("5 - Clasificar las obras por la nacionalidad de sus creadores")
    print("6 - Transportar obras de un departamento")
    print("7 - Proponer una nueva exposición en el museo ")

catalog = None
lista = None

#REQ 00
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

#REQ 01

def artistasCronologicos (catalog,lista):
    anio_inicio = int(input("Ingrese la fecha de minima de nacimiento: "))
    anio_fin =int(input("Ingrese la fecha maxima de busqueda: "))
    lista_artistas_crono=controller.artistasCronologicos(catalog, anio_inicio, anio_fin,lista)
    return lista_artistas_crono
    


# MENU PRINCIPAL
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        NUM_WORK=lt.size(catalog['artist'])
        print('Artistas cargados: ' + str(NUM_WORK))
        NUM_ART=lt.size(catalog['artwork'])
        print('Obras cargados: ' + str(NUM_ART))
        
        for i in range (0,3):
            print(lt.getElement(catalog['artist'],NUM_WORK-i))

        for i in range (0,3):
            print(lt.getElement(catalog['artwork'],NUM_WORK-i))

    elif int(inputs[0]) == 2:
        lista=artistasCronologicos(catalog,lista)
        print(lista)
        print(n)
        print('Hay '+str(lt.size(lista))+ "pintores que cumplen entre esas fechas.")
        

    elif int(inputs[0]) == 3:
        print("No disponible en esta version")

    elif int(inputs[0]) == 4:
        print("No disponible en esta version")

    elif int(inputs[0]) == 5:
        print("No disponible en esta version")

    elif int(inputs[0]) == 6:
        print("No disponible en esta version")

    elif int(inputs[0]) == 7:
        print("No disponible en esta version")

    else:
        sys.exit(0)
sys.exit(0)

