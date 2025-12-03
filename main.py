from fastapi import FastAPI
import requests

app = FastAPI()

url = 'https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.4/download/municipios.json'
data = requests.get(url)
data = data.json()

@app.get('/cantidad-entidad-por-filtro')
def cantidadEntidadesPor(filtro: str) -> dict[str, int] | str:
  '''
  Muestra cuantas entidades existen en cada filtro????
  '''
  filtros: dict[str, int] = {}
  filtros['total'] = 0
  
  if filtro == 'provincia':
    for e in data['municipios']:
      filtroEntidad = e['provincia']['nombre']
      if filtroEntidad not in filtros:
        filtros[filtroEntidad] = 1
        filtros['total'] += 1
      else:
        filtros[filtroEntidad] += 1
  else:
    for e in data['municipios']:
      filtroEntidad = e[filtro]
      if filtroEntidad not in filtros:
        filtros[filtroEntidad] = 1
        filtros['total'] += 1
      else:
        filtros[filtroEntidad] += 1
  return filtros