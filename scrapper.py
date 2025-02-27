from bs4 import BeautifulSoup
import requests


# - - - - - - Scrapers de precios - - - - - -
def MercadoLibrepriceScrap():
    url = "https://www.mercadolibre.com.ar/ofertas#nav-header"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    # set headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        productos = soup.find_all('div', class_='andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated')
        for producto in productos:
            nombre = producto.find('a', class_= 'poly-component__title')
            precio = producto.find('span', class_= 'andes-money-amount andes-money-amount--cents-superscript')
            if nombre is None or precio is None:
                    continue
            print(f'Producto: {nombre.text}\nPrecio: {precio.text}')
    else: 
        print('error') 
        print(response.status_code)
        
        
       #-----------------------------TIENDA MIA------------------------------------------------- 
def TiendaMiapriceScrap():
        url = "https://tiendamia.com/ar/tiendamia-en-vivo"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }
        # set headers
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
            productos = soup.find_all('div', class_='prod-fijo-left')
            for producto in productos:
                nombre = producto.find('a', class_= 'textMulish')
                precio = producto.find('span', class_= 'price_en_vivo currency_price')
                if nombre is None or precio is None:
                    continue
                print(f'Producto: {nombre.text}\nPrecio: {precio.text}')
        else: 
            print('error') 
            print(response.status_code)

#- - - - - - Busqueda por palabras - - - - - - 
def wordSearch():
    url = "https://tiendamia.com/ar/tiendamia-en-vivo"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }
    # set headers
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            palabra= input("Ingrese la palabra o frase a encontrar en la page: ").lower()
            numero_apariciones=0
            instancias = soup.find_all(text=lambda t: t and palabra in t.lower())
            for instancia in instancias:
                numero_apariciones=numero_apariciones+1
                tag = instancia.parent
    
                # Imprimir información sobre el elemento
                
                print("-Etiqueta:", tag.name)
                print("-Clases:", tag.get('class'))
                print("-Padre:", tag.parent.name if tag.parent else "Raíz")
                hermanos = [hermano.name for hermano in tag.parent.contents if hermano != tag and hermano.name]
                if hermanos:
                    print("-Hermanos:", hermanos)
                else:
                    print("-Hermanos: Sin hermanos")
                print("-Texto:", tag.get_text(strip=True))
                print("-" * 50)

            print(f"Esta palabra aparece un total de {numero_apariciones} veces a lo largo de la pagina especificada")
    
    else: 
            print('error') 
            print(response.status_code)    
wordSearch()