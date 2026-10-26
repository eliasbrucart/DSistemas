import requests

def obtener_datos_api(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json() # Retorna los datos en formato diccionario/lista de Python
        return None
    except requests.exceptions.RequestException as e:
        #print(f"Error en la petición: {e}")
        return None
