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

    a="SINGLE_LINKED"

    if tipoLista.lower() == "s":
       a="SINGLE_LINKED" 

    elif tipoLista.lower() == "a":
        a="ARRAY_LIST"

    else:
        print("Valor ingresado no valido se ejecutara por defecto SINGLE LINKED")

    catalog = {'artist': None,
               'artwork': None,
               }

    catalog['artwork'] = lt.newList(a)
    catalog['artist'] = lt.newList(a,
                                    cmpfunction=compareartist)
    
    return catalog

# REQ 00

def addartwork(catalog, artwork):

    lt.addLast(catalog['artwork'], artwork)

    #artists = artwork['artist'].strip("[]")
    #artists = artist.split(",")
    
    #for artist in artists:
       # addArtworkArtist(catalog, artist.strip(), artwork)

def addartist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artist'], artist)

def addArtworkArtist(catalog, artistname, artwork):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    artists = catalog['artist']
    posartist = lt.isPresent(artists, artistname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    lt.addLast(artist['artwork'], artwork)

def newArtist(name):
  
    artist = {'name': "", "artwork": None  }
    artist['name'] = name
    artist['artwork'] = lt.newList('ARRAY_LIST')
    return artist

def compareartist(artistname1, artist):
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1

def sortArtist(catalog, size, key):
    # TODO completar modificaciones para el laboratorio 4
    sub_list = lt.subList(catalog[key], 1, size) 
    sub_list = sub_list.copy() 
    start_time = time.process_time() 
    sorted_list = sa.sort(sub_list, compareratings) 
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return elapsed_time_mseg, sorted_list 

# REQ 01
   
def search_range_info(catalog, fecha_inicio, fecha_fin):

    lista=lt.newList()

    for artista in lt.iterator(catalog["artist"]):

        if artista["ArtistBio"]!="":
            art_fecha=artista["ArtistBio"].split(" ")
            
            date=art_fecha[-1].strip()

            if date[0] in "1234567890":
                date=date[:4]

                if int(date) in range(fecha_inicio,fecha_fin):
                    artista["DATE"]=int(date)
                    lt.addLast(lista, artista)
                    #sa(lista, cmpfunction=)

    return lista

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

    tiempo,listaordenada= sortArtist(catalog,a)
    
    return lt.subList(listaordenada,1,LenSub),tiempo,let

def cmpArtworkByDateAcquired(artwork1, artwork2):

    COMP_1=artwork1["DateAcquired"].replace("-","")
    COMP_2=artwork2["DateAcquired"].replace("-","")
    if COMP_1=="":
        COMP_1="0"
    if COMP_2=="":
        COMP_2="0"

    return (int(COMP_1) < int(COMP_2))

#DEF FOR SORTING

def sortArtist (catalog,A):
    start_time = time.process_time() 
    sorted_list = A.sort(catalog, cmpArtworkByDateAcquired) 
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return elapsed_time_mseg, sorted_list 



    

