from bs4 import BeautifulSoup
import requests
from collections import Counter
from requests.exceptions import HTTPError

# - - - - - - Scrapers de precios - - - - - -


def MercadoLibrepriceScrap():
    url = "https://www.mercadolibre.com.ar/ofertas#nav-header"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    # set headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        MLPriceScrapData={}  
        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all(
            'div', class_='andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated')
        for producto in productos:
            nombre = producto.find('a', class_='poly-component__title')
            precio = producto.find(
                'span', class_='andes-money-amount andes-money-amount--cents-superscript')
            if nombre is None or precio is None:
                continue
            print(f'Producto: {nombre.text}\nPrecio: {precio.text}')
            MLPriceScrapData[nombre.text] = precio.text
    else:
        print('error')
        print(response.status_code)

       # -----------------------------TIENDA MIA-------------------------------------------------


def TiendaMiapriceScrap():
    url = "https://tiendamia.com/ar/tiendamia-en-vivo"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    # set headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        TMPriceScrapData={}  
        soup = BeautifulSoup(response.text, 'html.parser')

        productos = soup.find_all('div', class_='prod-fijo-left')
        for producto in productos:
            nombre = producto.find('a', class_='textMulish')
            precio = producto.find(
                'span', class_='price_en_vivo currency_price')
            if nombre is None or precio is None:
                continue
            print(f'Producto: {nombre.text}\nPrecio: {precio.text}')
            TMPriceScrapData[nombre.text] = precio.text
    else:
        print('error')
        print(response.status_code)

# - - - - - - Busqueda por palabras - - - - - -


def wordSearch(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    # set headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        palabra = input(
            "Ingrese la palabra o frase a encontrar en la page: ").lower()
        numero_apariciones = 0
        instancias = soup.find_all(text=lambda t: t and palabra in t.lower())
        for instancia in instancias:
            numero_apariciones = numero_apariciones+1
            tag = instancia.parent

            # Imprimir información sobre el elemento

            print("-Etiqueta:", tag.name)
            print("-Clases:", tag.get('class'))
            print("-Padre:", tag.parent.name if tag.parent else "Raíz")
            hermanos = [
                hermano.name for hermano in tag.parent.contents if hermano != tag and hermano.name]
            if hermanos:
                print("-Hermanos:", hermanos)
            else:
                print("-Hermanos: Sin hermanos")
            print("-Texto:", tag.get_text(strip=True))
            print("-" * 50)

        print(
            f"Esta palabra aparece un total de {numero_apariciones} veces a lo largo de la pagina especificada")

    else:
        print('error')
        print(response.status_code)

# - - - - - - Data de datos Generales- - - - - -


def generalDataScrap(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Sacar el título de la página
    titulo = soup.title.text
    print("Título:", titulo)
    # Sacar la descripción de la página
    descripcion = soup.find("meta", attrs={"name": "description"})
    if descripcion:
        print("Descripción:", descripcion.get("content"))
    # Sacar las palabras clave de la página
    keywords = soup.find("meta", attrs={"name": "keywords"})
    if keywords:
        print("Palabras clave:", keywords.get("content"))
    # Sacar el contenido del cuerpo de la página
    cuerpo = soup.body.text
    """ print("Contenido del cuerpo:", cuerpo)  """

# - - - - - - Analisis por etiquetas y clases - - - - - -


def tagAnalyzer(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las etiquetas
        etiquetas = [tag.name for tag in soup.find_all(True)]

        # Contar la cantidad de cada etiqueta
        contador_etiquetas = Counter(etiquetas)

        # Imprimir las etiquetas y sus apariciones
        print("Etiquetas y sus apariciones:")
        for etiqueta, cantidad in contador_etiquetas.most_common():
            print(f"{etiqueta}: {cantidad}")

        # Encontrar las clases más comunes
        clases = [clase for tag in soup.find_all(
            class_=True) for clase in tag.get('class')]
        contador_clases = Counter(clases)

        # Imprimir las clases más comunes
        print("\nClases más comunes:")
        for clase, cantidad in contador_clases.most_common(10):
            print(f"{clase}: {cantidad} apariciones")

    else:
        print("Error:", response.status_code)


def validar_url():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }

    while True:
        url = input("Ingrese la URL que desea analizar: ")
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error http: {http_err}")
        except Exception as err:
            print(f"Ocurrió un error de algun tipo: {err}")
        else:
            print("URL valida!")
            return url


#def crear_informe():
    
# -----------------------------MENU PRINCIPAL--------------------------------------------

print("Bienvenido al programa de scraping y análisis de URLs")

while True:
    print("¿Qué desea hacer?")
    print("1. Scraping de precios")
    print("2. Análisis de URL")
    print("3. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("Scraping de precios")
        print("1. Tienda Mia")
        print("2. Mercado Libre")
        opcion_scraping = input("Ingrese su opción: ")
        if opcion_scraping == "1":
            TiendaMiapriceScrap()
        elif opcion_scraping == "2":
            MercadoLibrepriceScrap()
        else:
            print("Opción inválida")
    elif opcion == "2":
        url = validar_url()
        print("Análisis de URL")
        print("1. Búsqueda por palabras")
        print("2. Análisis de datos generales")
        print("3. Análisis de etiquetas y clases")
        print("4. Salir")
        opcion_analisis = input("Ingrese su opción: ")
        if opcion_analisis == "1":
            wordSearch(url)
        elif opcion_analisis == "2":
            generalDataScrap(url)
        elif opcion_analisis == "3":
            tagAnalyzer(url)
        elif opcion_analisis == "4":
            break
        else:
            print("Opción inválida")
    elif opcion == "3":
        break
    else:
        print("Opción inválida")

# LISTA DE CAMBIOS PENDIENTES:

# 1- Estandarizar una URL ingresada por el usuario al inicio del programa para que todas las opciones del menu y el mismo informe se creen en base a esa URL>>>> LISTO
# 2- Crear el menu, incluyendo la opcion de guardar informe >>>>LISTO
# 3- Darle la eleccion al usuario sobre que info guardar de cada opcion (quiza usa la opcion del general data scrap pero no quiere el cuerpo, solo titulo y descripcion en el informe, que eso sea posible)
# 4- Añadir las lineas con las que se guardara la informacion y la variable independiente donde se guardara toda la info que ira en el informe final
# 5- A la hora de guardar el informe, el usuario debera poder elegir el formato (TXT plano o XLSX, que son de excel podrian ser buenos formatos a elegir) que tendra el archivo que contendra toda la data de la variable independiente
# 6- Es necesario revisar si faltan limites o integrar avisos de errores 
        #---url>>>LISTO
        