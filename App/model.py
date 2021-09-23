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

def sort_fecha(catalog, fecha_inicio, fecha_fin):
    start_time = time.process_time() 
    lista=lt.newList()
    for artista in lt.iterator(catalog["artist"]):
        if artista["BeginDate"]!="":
            if int(artista["BeginDate"]) in range(fecha_inicio,fecha_fin+1):
                lt.addLast(lista, artista)
                
    s.sort(lista, cmpfunction=comparedate)  
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000           
    return lista,elapsed_time_mseg

def comparedate (artist1, artist2):
    return artist1["BeginDate"]<artist2["BeginDate"]

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

    start_time = time.process_time()

    compare=""
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

    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return {"TOTALOBRAS":len(dic2.values()),"TOTALTECNICAS":len(dic),
            "TECNICATOP":key,"OBRAS POR LA TECNICA": dic2["Obras"+key]},elapsed_time_mseg  
        
#REQ 05

def transporteobras(catalog,depmuseo):
    start_time = time.process_time()

    obrasdep=lt.newList()
    sumattl=0
    pesottl=0
    for obra in lt.iterator(catalog["artwork"]):
        if obra["Department"]==depmuseo:
            lt.addLast(obrasdep,obra)
            calculos=sumasdeobras(dict(obra))
            obra["PRICE"]=calculos
            sumattl+=calculos
            pesopieza=obra["Weight (kg)"].strip()
            if pesopieza!="":
                pesottl+=pesopieza
    
    obrasantiguas5=s.sort(obrasdep,cmpfunction=compareold)
    obrasantiguas5=lt.subList(obrasantiguas5,1,5)

    obrascostosas=s.sort(obrasdep,cmpfunction=compareprice)
    obrascostosas=lt.subList(obrascostosas,1,5)

    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return {"TOTAL OBRAS":lt.size(obrasdep),"ESTIMADO USD": sumattl,"PESO ESTIMADO":pesottl,
    "OBRAS ANTIGUAS":obrasantiguas5, "OBRAS COSTOSAS": obrascostosas},elapsed_time_mseg

def sumasdeobras(obra):

    dimen=obra["Dimensions"]
    otros=list(obra.values())
    d=otros[13:21]

    #['Circumference (cm)', 'Depth (cm)',
    #'Diameter (cm)', 'Height (cm)', 'Length (cm)',
    #'Weight (kg)', 'Width (cm)', 'Seat Height (cm)']
    circulo= d[2]!=""
    circulo2= d[0]!=""

    rectangle= d[3]!="" and d[4]!=""
    rectangle2= d[6]!="" and d[7]!=""

    cubo= d[3]!="" and d[4]!="" and d[6]!=""
    cubo2= d[1]!= "" and d[3]!= "" and d[4]!= "" 

    peso=d[5]!=""

    #ASIGNACIONES:
    mayorprecio=48.00
    preciocir=0
    preciocir2=0
    preciodime=0
    preciorec=0
    preciorec2=0
    preciocub=0
    preciocub2=0
    preciopeso=0

    if circulo:
        b=d[2].strip()
        preciocir=72.00/((180*(float(b**2)))/4)

    if circulo2:
        a=d[0].strip()
        L=(float(a))
        preciocir2=72.00/((L*(L/360))/2)

    if dimen!="":
        size=dimen.split("\"")
        size=size[-1].strip()
        size=size.strip("()[]cm ")
        size=size.split("×")
        preciodimen= rectangulo(size[0],size[1])

    if rectangle:
        preciorec= rectangulo(d[3],d[4])   

    if rectangle2:
        preciorec2= rectangulo(d[6],d[7]) 

    if cubo:
        preciocub= cubos(d[3],d[4],d[6])

    if cubo2:
        preciocub2= cubos(d[3],d[4],d[1])

    if peso:
        kg=d[5].strip()
        preciopeso=72.00/float(kg)

    valormayor=max(preciocir,preciocir2,preciodime, preciorec,preciorec2,preciocub,preciocub2,preciopeso) 
    if valormayor!=0:
         mayorprecio=valormayor

    return mayorprecio
            
def rectangulo(base,altura):
    base=base.strip()
    altura=altura.strip()
    size=float(base)*float(altura)
    precio=72.00/(size*(10**(-4)))
    return precio
            
def cubos(base,altura, profundidad):
    base=base.strip()
    altura=altura.strip()
    base=profundidad.strip()
    size=float(base)*float(altura)*float(profundidad)
    precio=72.00/(size*(10**(-4)))
    return precio

def compareprice(PRICE1,PRICE2):
    return PRICE1["PRICE"]<PRICE2["PRICE"]

def compareold(obra1,obra2):
    a=obra1["Date"]
    b=obra2["Date"]

    for val in [a,b]:
        if len(val)>0:
            if (len(val)==11) or ("c" in val):
                val=val[-4:]
            elif "-" in val:
                val=val[:5]
            else: 
                val=0

    return a<b













    

