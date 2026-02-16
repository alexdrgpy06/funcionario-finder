"""
---------------------------------------------------------------------------------------
Official Records Scraper
---------------------------------------------------------------------------------------
Handles data extraction from the Open Data Portal of the Ministry of Finance (Hacienda).
Parses raw JSON streams into a standardized dictionary format for the API layer.

@author Alejandro Ramírez
---------------------------------------------------------------------------------------
"""

import requests

def obtener_funcionarios():
  """
  Fetches the latest payroll and personnel records from the Hacienda Open Data API.
  
  Returns:
    list: A list of sanitized dictionaries containing personnel information.
  """
  url = 'https://datos.hacienda.gov.py/odmh-api-v1/nomina'
  params = {
    'size': 1000,
    'page': 0
  }
  
  try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    funcionarios = []
    # Data Normalization Pipeline
    for item in data.get('data', []):
      funcionario = {
        'nombre': item.get('nombre'),
        'cargo': item.get('cargo'),
        'departamento': item.get('institucion_descripcion'),
        'salario': item.get('salario_mensual')
      }
      funcionarios.append(funcionario)
    return funcionarios
    
  except Exception as e:
    # Fail-safe: log the error and return an empty list to avoid API crashes
    print(f"Scraper Error: {e}")
    return []
