import requests

def buscar_noticias(funcionario):
    url = f'https://newsapi.org/v2/everything?q={funcionario['nombre']}+corrupcion&apiKey=TU_API_KEY'
    response = requests.get(url)
    noticias = response.json.get('articles', [])
    return noticias