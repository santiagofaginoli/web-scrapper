from bs4 import BeautifulSoup
import requests

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
        nombre = producto.find('a', class_= 'poly-component__title').text
        precio = producto.find('span', class_= 'andes-money-amount andes-money-amount--cents-superscript').text
        print(f'Producto: {nombre}\nPrecio: {precio}')
else: 
    print('error') 
    print(response.status_code)
