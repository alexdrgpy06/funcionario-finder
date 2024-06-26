import requests

def obtener_funcionarios():
  url = 'https://datos.hacienda.gov.py/odmh-api-v1/nomina'
  params = {
    'size': 1000,  # Puedes ajustar el tamao
    'page': 0  # Puedes ajustar el numero de page
  }
  response = requests.get(url, params)
  data = response.json()
  
  funcionarios = []
  for item in data['data']:
    funcionario = {
      'nombre': item''nombre',
      'cargo': item''cargo',
      'departamento': item''institucion_descripcion',
      'salario': item'salario_mensual'
  }
    funcionarios.append(funcionario)
  return funcionarios
