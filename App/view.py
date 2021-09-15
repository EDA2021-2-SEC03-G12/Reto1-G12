
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

    print("_____________________________________________________________________")
    print(" ")
    print("         Ｂｉｅｎｖｅｎｉｄｏ　ａ　ＭｏＭＡ＇Ｓ　ＤＡＴＡ             ")
    print(" ")
    print(" ")
    print("                        ｏｐｃｉｏｎｅｓ                           ")
    print(" ")
    print("１ - Cargar información en el catálogo.")
    print("２ - Listar cronológicamente los artistas.")
    print("３ - Listar cronológicamente las adquisiciones. ")
    print("４ - Clasificar las obras de un artista por técnica.")
    print("５ - Clasificar las obras por la nacionalidad de sus creadores.")
    print("６ - Transportar obras de un departamento.")
    print("７ - Proponer una nueva exposición en el museo. ")
    print("0  - Salir" )
    print(" ")
    print("_____________________________________________________________________")
    
catalog = None

#REQ 00
def initCatalog():
    tipoLista = input('Ingrese S si desea la lista Single Linked o A si la desea Array: ')
    print("_____________________________________________________________________")
    print("...ｃａｒｇａｎｄｏ　ｉｎｆｏｒｍａｃｉｏｎ　ｄｅ　ａｒｃｈｉｖｏｓ ....")
    print("...ｅｓｐｅｒｅ...")
    print(" ")
    return controller.initCatalog(tipoLista)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def imprimir_tres(catalog, key):
    for i in range (0,3):
            print(lt.getElement(catalog[key],NUM_WORK-i))
    print(" ")

#REQ 01

def artistasCronologicos (catalog):
    anio_inicio = int(input("Ingrese la fecha de minima de nacimiento: "))
    anio_fin =int(input("Ingrese la fecha maxima de busqueda: "))
    lista_artistas_crono=controller.artistasCronologicos(catalog, anio_inicio, anio_fin)
    return lista_artistas_crono
    
#REQ 02

def adquisicionesCronologicas (catalog):
    LenSub= int(input("Ingrese la longitud(en numeros) de la muestra que desea ver: "))
    Ordenamiento= input("Ingrese la inicial del tipo de ordenamiento que desea utilizar (I)Insertion,(S)Shell, (M)Merge o (Q)Quick Sort: ")

    lista_adquisiciones_crono=controller.adquisicionesCronologicas(catalog,LenSub,Ordenamiento)
    return lista_adquisiciones_crono

# MENU PRINCIPAL
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print(" ")
        catalog = initCatalog()
        loadData(catalog)
        NUM_WORK=lt.size(catalog['artist'])
        print('ARTISTAS CARGADOS : ' + str(NUM_WORK))
        NUM_ART=lt.size(catalog['artwork'])
        print('OBRAS CARGADAS : ' + str(NUM_ART))
        print(" ")
        print("PRIMEROS ARTISTAS...")
        imprimir_tres(catalog,"artist")
        print(" ")
        print("PRIMERAS OBRAS...")
        imprimir_tres(catalog,"artwork")

    elif int(inputs[0]) == 2:
        lista=artistasCronologicos(catalog)
        print('Hay '+str(lt.size(lista))+ " pintores que cumplen entre esas fechas.")
        
    elif int(inputs[0]) == 3:
        lista, tiempo, let =adquisicionesCronologicas(catalog)
        print('La muestra es de '+str(lt.size(lista))+ " elementos.")
        print("La funcion " + let+ " tarda " +str(tiempo)+ " milisegundos.")

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

