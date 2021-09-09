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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():
    """
    Inicializa el catálogo de obras. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artist': None,
               'artwork': None,
               }

    catalog['artwork'] = lt.newList()
    catalog['artist'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartist)
    
    return catalog

# REQ 0

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

# REQ 1
   
def search_range_info(catalog, fecha_inicio, fecha_fin):

    lista=lt.newList()

    for artista in lt.iterator(catalog["artist"]):
        print(artista)
        if artista["ArtistBio"]!="":
            art_fecha=artista["ArtistBio"].split(" ")
            print(art_fecha)
            
            date=art_fecha[-1]
            if date[0] in "1234567890":
                if "–" in date:
                    date=date.split("–")
                    date=date[0]

                print(date)
                if int(date) in range(fecha_inicio,fecha_fin):
                    lt.addLast(lista, artista)

    return lista

    



    

