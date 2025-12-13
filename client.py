import requests
import json
import os

# IP de la pc de la facu
URL_API = 'http://127.0.0.1:8000'

def limpiarPantalla():
    # 'nt' es Windows, 'posix' es Linux/Mac
    if os.name == 'nt':     # Windows
        os.system('cls')
    else:                   # Linux/Mac
        os.system('clear')

def mostrar_menu():
  print('\n------------ MENU ------------')
  print('1- Mostrar la cantidad de entidades segun fuente, provincia o categoria')
  print('2- Mostrar la cantidad de categorias existentes en una provincia')
  print('3- Mostrar la cantidad de fuentes, provincias o categorias existentes')
  print('4- Mostrar entidades existentes por provincia y las categorias de la misma')
  print('5- Mostrar la ubicacion de una entidad')
  print('6- Modificar el nombre de una entidad')
  print('7- Eliminar una entidad')
  print('0- SALIR\n')

opcion = 999

while opcion != 0:
  opcionSegMenu = 0
  params = {}
  mostrar_menu()
  opcion = int(input('Seleccione una opción: '))

  while (opcion < 1 or opcion > 6) and opcion != 0:
    limpiarPantalla()
    print(f'La opcion {opcion} no es valida.\n')
    mostrar_menu()
    opcion = int(input('Seleccione una opcion nuevamente: '))

  if opcion == 1:
    limpiarPantalla()
    print('1- Provincia\n2- Fuente\n3- Categoria')
    criterio = int(input('Seleccione el parametro para filtrar: '))
    
    while criterio < 1 or criterio > 3:
      limpiarPantalla()
      print(f'La opcion {criterio} no es valida.\n')
      print('1- Provincia\n2- Fuente\n3- Categoria')
      criterio = int(input('Seleccione una opcion nuevamente: '))

    if criterio == 1:
      params = {'filtro': 'provincia'}
    elif criterio == 2:
      params = {'filtro': 'fuente'}
    elif criterio == 3:
      params = {'filtro': 'categoria'}
      
    try:
      response = requests.get(f'{URL_API}/cantidad-entidades', params=params)
      if response.status_code == 200:
        limpiarPantalla()
        data = response.json()
        print(f'Cantidad de entidades segun: {params['filtro']}')
        print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
      else:
        limpiarPantalla()
        print('Error. Codigo: ', response.status_code)
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()
      
  elif opcion == 2:
    limpiarPantalla()
    print('1- Seleccionar provincia para filtrar\n2- Mostrar sin filtros')
    opcionSegMenu = int(input('Seleccione una opcion: '))
    
    while opcionSegMenu < 1 or opcionSegMenu > 2:
      limpiarPantalla()
      print(f'La opcion {opcionSegMenu} no es valida.\n')
      print('1- Seleccionar provincia para filtrar\n2- Mostrar sin filtros')
      opcionSegMenu = int(input('Seleccione una opcion nuevamente: '))

    if opcionSegMenu == 1:
      limpiarPantalla()
      prov = str(input('Escriba el nombre de una provincia: '))
      
      params = {'provincia': prov}
      
      try:
        response = requests.get(f'{URL_API}/categorias-por-provincia', params=params)
        if response.status_code == 200:
          limpiarPantalla()
          data = response.json()
          print(f'Categorias existentes en {params['provincia']}')
          print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
        else:
          limpiarPantalla()
          print('Error. Codigo: ', response.status_code)
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
      except requests.exceptions.ConnectionError:
        limpiarPantalla()
        print('Error al intentar conectarse a la API')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()

    if opcionSegMenu == 2:
      try:
        response = requests.get(f'{URL_API}/categorias-por-provincia')
        if response.status_code == 200:
          limpiarPantalla()
          data = response.json()
          print('Categorias existentes en todas las provincias')
          print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
        else:
          limpiarPantalla()
          print('Error. Codigo: ', response.status_code)
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
      except requests.exceptions.ConnectionError:
        limpiarPantalla()
        print('Error al intentar conectarse a la API')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()

  elif opcion == 3:
    limpiarPantalla()
    print('1- Provincia\n2- Fuente\n3- Categoria')
    criterio = int(input('Seleccione el parametro para filtrar: '))
    
    while criterio < 1 or criterio > 3:
      limpiarPantalla()
      print(f'La opcion {criterio} no es valida.\n')
      print('1- Provincia\n2- Fuente\n3- Categoria')
      criterio = int(input('Seleccione una opcion nuevamente: '))

    if criterio == 1:
      params = {'filtro': 'provincia'}
    elif criterio == 2:
      params = {'filtro': 'fuente'}
    elif criterio == 3:
      params = {'filtro': 'categoria'}
      
    try:
      response = requests.get(f'{URL_API}/mostrar-entidades', params=params)
      if response.status_code == 200:
        limpiarPantalla()
        data = response.json()
        print(f'{params['filtro'].capitalize()}s')
        print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
      else:
        limpiarPantalla()
        print('Error. Codigo: ', response.status_code)
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

  elif opcion == 4:
    limpiarPantalla()
    print('1- Seleccionar categoria para filtrar\n2- Mostrar sin filtros')
    opcionSegMenu = int(input('Seleccione una opcion: '))

    while opcionSegMenu < 1 or opcionSegMenu > 2:
      limpiarPantalla()
      print(f'La opcion {opcionSegMenu} no es valida.\n')
      print('1- Seleccionar categoria para filtrar\n2- Mostrar sin filtros')
      opcionSegMenu = int(input('Seleccione una opcion nuevamente: '))

    if opcionSegMenu == 1:
      limpiarPantalla()
      prov = str(input('Escriba el nombre de una provincia: '))
      limpiarPantalla()
      print('\n1- Municipio')
      print('2- Comision municipal')
      print('3- Comision de fomento')
      print('4- Comuna')
      print('5- Delegacion municipal')
      print('6- Comuna rural')
      print('7- Junta vecinal')
      cat = int(input('Seleccione una opcion: '))

      while cat < 1 or cat > 7:
        limpiarPantalla()
        print(f'La opcion {cat} no es valida.\n')
        print('\n1- Municipio')
        print('2- Comision municipal')
        print('3- Comision de fomento')
        print('4- Comuna')
        print('5- Delegacion municipal')
        print('6- Comuna rural')
        print('7- Junta vecinal')
        cat = int(input('Seleccione una opcion nuevamente: '))

      params = {'provincia': prov}
      if cat == 1:
        params['categoria'] = 'Municipio'
      if cat == 2:
        params['categoria'] = 'Comision municipal'
      if cat == 3:
        params['categoria'] = 'Comision de fomento'
      if cat == 4:
        params['categoria'] = 'Comuna'
      if cat == 5:
        params['categoria'] = 'Delegacion municipal'
      if cat == 6:
        params['categoria'] = 'Comuna rural'
      if cat == 7:
        params['categoria'] = 'Junta vecinal'

      try:
        response = requests.get(f'{URL_API}/entidades-por-provincia', params=params)
        if response.status_code == 200:
          limpiarPantalla()
          data = response.json()
          print(f'{params['categoria'].capitalize()}s existentes en {params['provincia']}')
          print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
        else:
          limpiarPantalla()
          print('Error. Codigo: ', response.status_code)
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
      except requests.exceptions.ConnectionError:
        limpiarPantalla()
        print('Error al intentar conectarse a la API')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
    
    if opcionSegMenu == 2:
      limpiarPantalla()
      prov = str(input('Escriba el nombre de una provincia: '))
      
      params = {'provincia': prov}
      
      try:
        response = requests.get(f'{URL_API}/entidades-por-provincia', params=params)
        if response.status_code == 200:
          limpiarPantalla()
          data = response.json()
          print(f'Entidades existentes en {params['provincia']}')
          print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
        else:
          limpiarPantalla()
          print('Error. Codigo: ', response.status_code)
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
      except requests.exceptions.ConnectionError:
        limpiarPantalla()
        print('Error al intentar conectarse a la API')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()

  elif opcion == 5:
    limpiarPantalla()
    prov = str(input('Escriba el nombre de una provincia: '))
    limpiarPantalla()
    provResp = requests.get(f'{URL_API}/categorias-por-provincia', params={'provincia': prov})

    if provResp.status_code == 404:
      print('Error. Codigo: ', provResp.status_code)
      input("\nPresione Enter para continuar...")
      continue
    entidad = str(input('Escriba el nombre de una entidad: '))
    limpiarPantalla()
    
    params['provincia'] = prov
    params['nombreEntidad'] = entidad
    
    try:
      response = requests.get(f'{URL_API}/entidad-mapa', params=params)
      if response.status_code == 200:
        limpiarPantalla()
        data = response.json()
        print(f'Ubicacion geografica de {params['nombreEntidad']} en {params['provincia']}')
        print(f'{json.dumps(data, indent=4, ensure_ascii=False)}\n')
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
      else:
        limpiarPantalla()
        print('Error. Codigo: ', response.status_code)
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

  elif opcion == 0:
    # limpiarPantalla()
    print('\nFIN DEL PROGRAMA\n')