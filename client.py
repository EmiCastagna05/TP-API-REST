import requests
import json
import os

# IP de la pc de la facu
URL_API = 'http://127.0.0.1:8000'

def limpiarPantalla():
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
  print('7- Agregar una nueva entidad')
  print('8- Eliminar una entidad')
  print('0- SALIR\n')

opcion = 999

while opcion != 0:
  opcionSegMenu = 0
  params = {}
  mostrar_menu()
  opcion = int(input('Seleccione una opción: '))

  while (opcion < 1 or opcion > 8) and opcion != 0:
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
        print(f"Error inesperado. Código: {response.status_code}")
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
          print(f"Error inesperado. Código: {response.status_code}")
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
          print(f"Error inesperado. Código: {response.status_code}")
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
        print(f"Error inesperado. Código: {response.status_code}")
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
      print('1- Municipio')
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
        params['categoria'] = 'municipio'
      if cat == 2:
        params['categoria'] = 'comision municipal'
      if cat == 3:
        params['categoria'] = 'comision de fomento'
      if cat == 4:
        params['categoria'] = 'comuna'
      if cat == 5:
        params['categoria'] = 'delegacion municipal'
      if cat == 6:
        params['categoria'] = 'comuna rural'
      if cat == 7:
        params['categoria'] = 'junta vecinal'

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
          print(f"Error inesperado. Código: {response.status_code}")
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
          print(f"Error inesperado. Código: {response.status_code}")
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
    
    params = {
      'provincia': prov,
      'nombreEntidad': entidad
    }
    
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
        print(f"Error inesperado. Código: {response.status_code}")
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

  elif opcion == 6:
    limpiarPantalla()
    print('Se requiere autenticacion')
    user = str(input('Usuario: '))
    pwd = str(input('Contraseña: '))
    
    try:
      authResponse = requests.get(f'{URL_API}/verificar-auth', auth=(user, pwd))
      
      if authResponse.status_code == 401:
        print('ACCESO DENEGADO. Usuario o Contraseña incorrectos.')
        input("\nPresione Enter para continuar...")
        continue

      print('ACCESO OTORGADO')

      limpiarPantalla()
      prov = input('Escriba el nombre de la provincia: ')
      nombreActual = input('Escriba el nombre actual de la entidad a modificar: ')
      limpiarPantalla()

      print("\nDatos a insertar. Dejar vacio el campo que no se desee modificar.")
      nuevoNombre = input('Nuevo nombre: ')
      categoria = input('Nueva categoría: ')

      if not nuevoNombre and not categoria:
        limpiarPantalla()
        print("No se ingresaron cambios.")
        input("\nPresione Enter para continuar...")

      params = {
        'provincia': prov,
        'nombreActual': nombreActual
      }
      
      if nuevoNombre:
        params['nuevoNombre'] = nuevoNombre.strip().title()
      if categoria:
        params['categoria'] = categoria.strip().title()

    
      response = requests.patch(f'{URL_API}/cambio-nombres-y-categoria', params=params)
      limpiarPantalla()
      if response.status_code == 200:
        data = response.json()
        print(f"Mensaje: {data['mensaje']}")
        print(json.dumps(data['entidad'], indent=4, ensure_ascii=False))
        input("\nPresione Enter para continuar...")
        limpiarPantalla()
      else:
          limpiarPantalla()
          print(f"Error inesperado. Código: {response.status_code}")
          input("\nPresione Enter para continuar...")
          limpiarPantalla()
    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

  elif opcion == 7:
    limpiarPantalla()
    print('Se requiere autenticacion')
    user = str(input('Usuario: '))
    pwd = str(input('Contraseña: '))
    
    try:
      authResponse = requests.get(f'{URL_API}/verificar-auth', auth=(user, pwd))
      
      if authResponse.status_code == 401:
        print('ACCESO DENEGADO. Usuario o Contraseña incorrectos.')
        input("\nPresione Enter para continuar...")
        continue

      print('ACCESO OTORGADO')

      limpiarPantalla()
      nombre = input('Nombre de la entidad: ')
      categoria = input('Categoría: ')
      prov = input('Provincia: ')

      while nombre == '' or categoria == '' or prov == '':
        limpiarPantalla()
        print("Los campos Nombre, Categoría y Provincia son obligatorios.")
        if nombre == '':
          nombre = input('Nombre de la entidad: ')
        if categoria == '':
          categoria = input('Categoría: ')
        if prov == '':
          prov = input('Provincia: ')

      while True:
        try:
          lat = input('Latitud (ej: -31.40): ')
          break
        except ValueError:
          print("El campo Lat es obligatorio. Ingrese una Latitud (ej: -31.40): ")

      while True:
        try:
          lon = input('Longitud (ej: -64.18): ')
          break
        except ValueError:
          print("El campo Lon es obligatorio. Ingrese una Longitud (ej: -64.18): ")

      params = {
        'nombre': nombre.strip().title(),
        'categoria': categoria.strip().title(),
        'provincia': prov.strip().title(),
        'lat': float(lat.strip()),
        'lon': float(lon.strip())
      }
      
      response = requests.post(f'{URL_API}/agregar-entidad', params=params, auth=(user, pwd))
      limpiarPantalla()
      if response.status_code == 200:
        data_resp = response.json()
        print(json.dumps(data_resp['entidad'], indent=4, ensure_ascii=False))
        input("\nPresione Enter para continuar...")
      else:
        print(f"Error inesperado. Código: {response.status_code}")
        input("\nPresione Enter para continuar...")

    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

  elif opcion == 8:
    limpiarPantalla()
    print('Se requiere autenticacion')
    user = str(input('Usuario: '))
    pwd = str(input('Contraseña: '))
    
    try:
      authResponse = requests.get(f'{URL_API}/verificar-auth', auth=(user, pwd))
      
      if authResponse.status_code == 401:
        print('ACCESO DENEGADO. Usuario o Contraseña incorrectos.')
        input("\nPresione Enter para continuar...")
        continue

      print('ACCESO OTORGADO')

      idBorrar = str(input('Ingrese el ID de la entidad a eliminar: '))
      
      if not idBorrar:
        limpiarPantalla()
        while idBorrar == '':
          print('El ID ingresado no es valido.')
          idBorrar = str(input('Ingrese el ID de la entidad a eliminar: '))

      seguro = input(f"¿Seguro que desea borrar la entidad {idBorrar}? (s/n): ").lower()
      if seguro != 's':
        print("Operacion cancelada.")
        input("\nPresione Enter para continuar...")
        continue

      response = requests.delete(f'{URL_API}/eliminar-entidad', params={'id': idBorrar}, auth=(user, pwd))
      limpiarPantalla()
      if response.status_code == 200:
        data = response.json()
        print("Entidad eliminada:")
        print(json.dumps(data['entidad'], indent=4, ensure_ascii=False))
        input("\nPresione Enter para continuar...")
      else:
        print(f"Error inesperado. Código: {response.status_code}")
        input("\nPresione Enter para continuar...")

    except requests.exceptions.ConnectionError:
      limpiarPantalla()
      print('Error al intentar conectarse a la API')
      input("\nPresione Enter para continuar...")
      limpiarPantalla()

    input("\nPresione Enter para continuar...")
    limpiarPantalla()

  elif opcion == 0:
    print('\nFIN DEL PROGRAMA\n')