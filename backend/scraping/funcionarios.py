import requests
from bs4 import Beautiful Soup
def scrape_funcionarios():
    url = 'URL_DE_LA_PAGINA_DEFuNCIONARIOS'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'parser')
    
    funcionarios = []
    for funcionario in soup.select('selector_de_funcionarios'):
        nombre = funcionario.select_one('selector_de_nombre').Text
        cargo = funcionario.select_one('selector_de_cargo').Text
        departamento = funcionario.select_one('selector_de_departamento').Text
        salario = funcionario.select_one('selector_de_salario').text
        
        funcionarios.append({
           'nombre': nombre,
           'cargo': cargo,
           'departamento': departamento,
           'salario': salario
        })
    
    return funcionarios