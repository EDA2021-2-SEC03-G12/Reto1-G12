"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.singlelinkedlist import subList
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as m
from DISClib.Algorithms.Sorting import insertionsort as i
from DISClib.Algorithms.Sorting import shellsort as s
from DISClib.Algorithms.Sorting import quicksort as q
import re
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog(tipoLista):
    """
    Inicializa el catálogo de obras. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """

    a="ARRAY_LIST"

    if tipoLista.lower() == "s":
       a="SINGLE_LINKED" 

    elif tipoLista.lower() == "a":
        a="ARRAY_LIST"

    else:
        print("Valor ingresado no valido se ejecutara por defecto ARRAY LIST")

    catalog = {'artist': None,
               'artwork': None,
               }

    catalog['artwork'] = lt.newList(a)
    catalog['artist'] = lt.newList(a)
    
    return catalog

# REQ 00


def addartwork(catalog, artwork):
    lt.addLast(catalog['artwork'], artwork)

    artists = artwork['ConstituentID'].strip("[]")
    artists = artists.split(",")

def addartist(catalog, artist):
    lt.addLast(catalog['artist'], artist)


# REQ 01
   
def search_range_info(catalog, fecha_inicio, fecha_fin):

    lista=lt.newList()
    
    for artista in lt.iterator(catalog["artist"]):
        if artista["ArtistBio"]!="":
            art_fecha=artista["ArtistBio"].split(" ")
            
            date=art_fecha[-1].strip()

            if date[0] in "1234567890":
                date=date[:4]

                if int(date) in range(fecha_inicio,fecha_fin+1):
                    
                    artista["DATE"]=int(date)
                    lt.addLast(lista, artista)
                    s.sort(lista, cmpfunction=comparedate)

    return lista

def comparedate (artist1, artist2):
    return artist1["DATE"]<artist2["DATE"]

#REQ 02  

def search_crono_adquired(catalog,LenSub,orde):

    if LenSub > lt.size(catalog):
        LenSub=lt.size(catalog)

    let="Merge Sort"
    a=m
    inputt=orde.lower()
    if inputt == "i":
        let="Insertion Sort"
        a=i
    elif inputt == "s":
        let="Shell Sort"
        a=s
    elif inputt == "m":
        let="Merge Sort"
        a=m
    elif inputt == "q":
        let="Quick Merge"
        a=q
    else:
        print("Entrada no valida se ejecutara Insertion por defecto. ")

    catalogo=lt.subList(catalog,1,LenSub)
    tiempo,listaordenada= sortArtist(catalogo,a)
    
    return listaordenada,tiempo,let

def cmpArtworkByDateAcquired(artwork1, artwork2):

    COMP_1=artwork1["DateAcquired"].replace("-","")
    COMP_2=artwork2["DateAcquired"].replace("-","")
    if COMP_1=="":
        COMP_1="0"
    if COMP_2=="":
        COMP_2="0"

    return (int(COMP_1) < int(COMP_2))

def sortArtist (catalog,A):
    start_time = time.process_time() 
    sorted_list = A.sort(catalog, cmpArtworkByDateAcquired) 
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return elapsed_time_mseg, sorted_list 

#REQ 03

def tecnicaArtista (catalog,nombre,dic,dic2):

    for artista in lt.iterator(catalog["artist"]):
        if artista["DisplayName"]==nombre:
            compare=artista["ConstituentID"]
            break

    for obra in lt.iterator(catalog["artwork"]):
        element=obra["ConstituentID"].strip('[]')
        element=element.split(",")
        if compare in element:
            medio=obra["Medium"]
            if medio not in dic:
                dic[medio]=1
                dic2["Obras"+medio]=[dict(obra)]
            else:
                dic[medio]+=1
                dic2["Obras"+medio]=dic2["Obras"+medio].append(dict(obra))
    
    value=0
    for keys,values in dic.items():
        if values>value:
            value=values
            key=keys

    return {"TOTALOBRAS":len(dic2.values()),"TOTALTECNICAS":len(dic),
            "TECNICATOP":key,"OBRAS POR LA TECNICA": dic2["Obras"+key]}  
        

#REQ 05

def transporteobras(catalog,depmuseo):
    obrasdep=[]
    for obra in lt.iterator(catalog["artwork"]):
        if obra["Department"]==depmuseo:
            obrasdep.append(obra)
            calculos=sumasdeobras(obra)

    return calculos


def sumasdeobras(obra):
    dimen=obra["Dimensions"]
    weigh=obra["Weight (kg)"]

    if weigh!="":
        a=72.00/int(weigh)
    
    if dimen!="":
        size=dimen.split("\"")
        size=size[-1].strip()
        size=size.strip("()[]cm ")
        size=eval(size.replace("×","*"))
        
        precio_dimen=72.00/(size*(10**(-4)))
        
        #b=72.00
  
        print(precio_dimen)

    return size,weigh
            


            









    

