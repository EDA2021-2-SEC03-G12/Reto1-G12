import config as cf
import model
import csv

def initCatalog(tipoLista):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipoLista)
    return catalog

# REQ 00

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtwork(catalog)
    loadArtist(catalog)
    
def loadArtwork(catalog):

    artworkfile = cf.data_dir + '\MoMA\Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addartwork(catalog, artwork)

def loadArtist(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artist in input_file:
        model.addartist(catalog, artist)

# REQ 01

def artistasCronologicos(catalog, fecha_inicio, fecha_fin):
    full_list=model.search_range_info(catalog, fecha_inicio, fecha_fin)      
    return full_list

#REQ 02

def adquisicionesCronologicas(catalog,LenSub,ord):
    lista=model.search_crono_adquired(catalog['artwork'],LenSub,ord)
    return lista

#REQ 03

def portecnica(catalog, name):
    dic={}
    dic2={}
    lista=model.tecnicaArtista(catalog,name,dic,dic2)
    return lista

#REQ 05

def costo(catalog,depname):
    lista=model.transporteobras(catalog,depname)
    return lista