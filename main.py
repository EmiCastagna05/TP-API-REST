from fastapi import FastAPI, HTTPException
import json
import unicodedata

app = FastAPI()

with open("data.json", "r", encoding="utf-8") as archivo:
  data = json.load(archivo)

def normalizar(texto: str) -> str:
  texto = texto.lower()
  texto = unicodedata.normalize("NFD", texto)
  texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
  return texto

@app.get('/cantidad-entidades')
def cantidadEntidades(filtro: str) -> dict[str, int]:
  '''
  Muestra cuantas entidades existen segun fuente, provincia o categoria
  '''
  filtros: dict[str, int] = {}
  filtros['total'] = 0
  
  if filtro == 'provincia':
    for e in data['entidades']:
      filtroEntidad = normalizar(e['provincia']['nombre'])
      if filtroEntidad not in filtros:
        filtros[filtroEntidad] = 1
        filtros['total'] += 1
      else:
        filtros[filtroEntidad] += 1
  else:
    for e in data['entidades']:
      filtroEntidad = normalizar(e[filtro])
      if filtroEntidad not in filtros:
        filtros[filtroEntidad] = 1
        filtros['total'] += 1
      else:
        filtros[filtroEntidad] += 1
  return filtros

@app.get("/categorias-por-provincia")
def contarCategorias(provincia: str | None = None):
  if provincia:
    municipios = []
    for m in data['entidades']:
      if normalizar(m["provincia"]["nombre"]) == normalizar(provincia):
        municipios.append(m)
    if not municipios:
      raise HTTPException(status_code=404)
  else:
    municipios = data['entidades']

  conteo = {}

  for m in municipios:
    categoria = normalizar(m["categoria"])
    if categoria in conteo:
      conteo[categoria] += 1
    else:
      conteo[categoria] = 1

  if provincia:
    return {
      "provincia": provincia,
      "total": sum(conteo.values()),
      "categorias": conteo
    }
  else:
    return {
      "total": sum(conteo.values()),
      "categorias": conteo
    }

@app.get("/mostrar-entidades")
def mostrarEntidades(filtro: str) -> list[str]:
  '''
  Muestra las entidades existentes segun fuente, provincia o categoria
  '''
  filtros = []
  
  if filtro == 'provincia':
    for e in data['entidades']:
      filtroEntidad = normalizar(e['provincia']['nombre'])
      if filtroEntidad not in filtros:
        filtros.append(filtroEntidad)
  else:
    for e in data['entidades']:
      filtroEntidad = normalizar(e[filtro])
      if filtroEntidad not in filtros:
        filtros.append(filtroEntidad)
  return filtros

@app.get("/entidades-por-provincia")
def entidadesPorProvincia(provincia: str, categoria: str | None = None):
  entidades = set()
  nombreProvParam = normalizar(provincia)

  if categoria:
    for e in data['entidades']:
      nombreProv = normalizar(e['provincia']['nombre'])
      nombreCategoria = normalizar(e['categoria'])
      if nombreProv == nombreProvParam and nombreCategoria == categoria:
        entidades.add(e['nombre'])

  else:
    for m in data['entidades']:
      provEntidad = normalizar(m['provincia']['nombre'])
      if provEntidad == nombreProvParam:
        entidades.add(m['nombre'])

  if not entidades:
    raise HTTPException(status_code=404)

  if categoria:
    return {
      'provincia': provincia,
      'cantidad': len(entidades),
      categoria: sorted(entidades)
    }
  else:
    return {
      'provincia': provincia,
      'cantidad': len(entidades),
      'entidades': sorted(entidades)
    }

@app.get("/entidad-mapa")
def municipio_mapa(provincia: str, nombreEntidad: str):
  provEncontrada = False
  for m in data["entidades"]:
    
    if normalizar(m["provincia"]["nombre"]) == normalizar(provincia):
      provEncontrada = True
      if normalizar(m["nombre"]) == normalizar(nombreEntidad):
        lat = m["centroide"]["lat"]
        lon = m["centroide"]["lon"]
        id = m['id']

        return {
          "id": id,
          "lat": lat,
          "lon": lon,
          "google_maps": f"https://www.google.com/maps?q={lat},{lon}"
        }
  if not provEncontrada:
    raise HTTPException(status_code=404)
  raise HTTPException(status_code=404)

@app.patch('/cambio-nombres-y-categoria')
def reemplazo(provincia: str, nombreActual: str, nuevoNombre: str | None = None, categoria: str | None = None):
  provEncontrada = False
  entidades = data["entidades"]

  for e in entidades:
    if normalizar(e["provincia"]["nombre"]) == normalizar(provincia):
      provEncontrada = True
      
      if normalizar(e["nombre"]) == normalizar(nombreActual):
        if nuevoNombre:
          e["nombre"] = nuevoNombre
        if categoria:
          e["categoria"] = categoria
        e["nombre_completo"] = f"{e['categoria']} {e['nombre']}"
        return {
          "mensaje": "Entidad actualizado",
          "entidad": e
        }
        
  if not provEncontrada:
    raise HTTPException(status_code=404)
  raise HTTPException(status_code=404)

@app.post('/agregar-entidad')
def agregarEntidad(nombre: str, categoria: str, provincia: str, lat: float, lon: float):
    ids = [int(e['id']) for e in data['entidades']]
    nuevoId = max(ids) + 1
    
    nuevaEntidad = {
        "nombre_completo": f"{categoria.capitalize()} {nombre.capitalize()}",
        "fuente": "Usuario",
        "nombre": nombre.capitalize(),
        "id": str(nuevoId),
        "provincia": {
            "nombre": provincia.capitalize(),
            "id": "00"
        },
        "categoria": categoria.capitalize(),
        "centroide": {
            "lat": lat,
            "lon": lon
        }
    }
    
    data['entidades'].append(nuevaEntidad)
    data['total'] += 1
    data['cantidad'] += 1

    return {
        "mensaje": "Entidad creada",
        "entidad": nuevaEntidad
    }

@app.delete('/eliminar-entidad')
def eliminarEntidad(id: str):
  entidades = data['entidades']
  for i, m in enumerate(entidades):
    if m["id"] == id:
      eliminado = entidades.pop(i)
      data['total'] -= 1
      data['cantidad'] -= 1
      return {
        "mensaje": "Entidad eliminada",
        "entidad": eliminado
      }
  raise HTTPException(status_code=404)