import config as cf
import model
import csv

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# REQ 0

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtwork(catalog)
    loadArtist(catalog)
    
def loadArtwork(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
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

# REQ 1

def initList():
    lista=model.newList()
    return lista

def artistasCronologicos(catalog, fecha_inicio, fecha_fin, lista):
    lista=initList()
    full_list=model.search_range_info(catalog, fecha_inicio, fecha_fin, lista)      
    return full_list