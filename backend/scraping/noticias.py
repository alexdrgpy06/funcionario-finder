import requests

def buscar_noticias(funcionario):
    api_key = 'TU_API_KEY'  # Replaza con tu clave de API de NewsAPI
    url = f'https://newsapi.org/v2/everything?q={funcionario['nombre']}+corrupcion&apiKey={api_key}'
    response = requests.get(url)
    noticias = response.json().get('articles', [])
    return noticias
