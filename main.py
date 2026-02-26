# Importación de módulos

import os
os.system('cls')

from victoria_musura_catalogo_peliculas import CatalogoPelicula, Pelicula

# Funciones para la ejecución del programa

def listarCatalogos(): # Funcionalidad para listar los catálogos existentes
    directorio = "." # Indica que la ruta del directorio es el directorio actual 
    archivos_catalogos_existentes = [f for f in os.listdir(directorio) if f.endswith('.txt')] # Lista que almacena todos los archivos de catálogos que existen
    nombre_archivos_catalogos_existentes = [os.path.splitext(f)[0] for f in archivos_catalogos_existentes] # Lista de nombres de los archivos sin extensión
    print("Listado de catálogos:")
    for elemento in nombre_archivos_catalogos_existentes:
        print(elemento)

def menuPrincipal(): # Funcionalidad para mostrar un menú de inicio.
    tituloPrograma = "Bienvenido al catálogo de películas🍿🎦" 
    print(tituloPrograma) # Se impime un mensaje de bienvenida
    while True: # Se genera un bucle para mantener activo el programa
        opciones = "Opciones:\n1-Ingresar a un catálogo\n2-Salir"
        print(opciones) # Se imprimen las opciones disponibles y se solicita al usuario que ingrese una opción
        input_opcion = input("Elija una opción: ")
        if input_opcion == "1": # La opción 1 muestra los catálogos existentes e ingresa a la función ingresoCatalogo
            listarCatalogos()
            ingresoCatalogo()
        else: 
            if input_opcion == "2": # La opción 2 finaliza el programa
                print("Se ha cerrado el programa.")
                break
            else: # Cualquier otra opción es tomada como inválida y muestra un mensaje al usuario.
                print("Opción inválida. Ingrese un número de las opciones listadas.")


def menuCatalogo(catalogo): # Funcionalidad de acciones dentro del catálogo
    while True:
        listadoOpciones = "Opciones:\n1. Agregar película\n2- Listar películas\n3- Eliminar catálogo actual\n4- Volver al menú anterior\n5- Salir"
        print(listadoOpciones) # Se muestran las opciones disponibles al usuario
            
        inputMenu = input("Elija una opción: ") # Se le solicita al usuario que ingrese un número de opción
            
        if inputMenu == "1": # La opción 1 redirige al método agregarPelicula() de la clase CatalogoPelicula
                catalogo.agregarPelicula()
        else:
            if inputMenu == "2": # La opción 2 redirige al método listarPelicula() de la clase CatalogoPelicula
                catalogo.listarPeliculas()
            else:
                if inputMenu == "3": # La opción 3 redirige al método eliminarCatalogo() de la clase CatalogoPelicula
                    catalogo.eliminarCatalogo()
                    break
                else:
                    if inputMenu == "4":
                        break
                    else:
                        if inputMenu == "5": # La opción 5 finaliza la sesión
                            print("Ha finalizado su sesión en el catálogo de películas")
                            exit()
                        else: # Cualquier otro valor numérico ingresado le indica al usuario que la opción es inválida y habilita nuevamente el menú con su input.
                            print("La opción ingresada no es válida. Vuelva a intentar")

def ingresoCatalogo(): # Funcionalidad de ingreso.
    inputCatalogo = input("Inserte el nombre del catálogo sobre el que desea operar: ") # Se le solicita al usuario que ingrese el nombre de un catálogo.
    catalogo = CatalogoPelicula(inputCatalogo)

    if not os.path.exists(catalogo.ruta_archivo): # El programa verifica si el catálogo ya existe. En caso de que no, pregunta al usuario si desea crearlo. 
        # Se pasa a minúsculas para evitar inconsistencias.
        crearCatalogo = input("El catálogo no existe. ¿Desea crearlo?(si/no): ").lower()
        if crearCatalogo == "si": # Si decide crear un catálogo con ese nombre, se generará el mismo y se accederá al menú correspondiente.
            with open(catalogo.ruta_archivo, 'a', encoding='UTF-8') as archivo:
                archivo.write(f"Nombre del catálogo: '{catalogo.nombre_catalogo}'\n")
                print(f"Nuevo catálogo '{catalogo.nombre_catalogo}' creado con éxito.")
                menuCatalogo(catalogo.ruta_archivo)
        else: # Si no desea crearlo, habilitará nuevamente el input para que ingrese un catálogo existente.
                print("No se ha podido acceder al sistema. Intente nuevamente")
    else: # En caso de que el catálogo ya exista, ingresará al menú de acciones del catálogo
        return menuCatalogo(catalogo)

def catalogoMuestra(): # Función que genera un catálogo de muestra para el programa
    catalogo = CatalogoPelicula('Catalogo de Muestra')
    pelicula_muestra = Pelicula("Tiempo de valientes", "Damián Szifron", 2005, "Un clásico argentino que nos muestra la relación entre un psicoanalista y un policia")
    with open(catalogo.ruta_archivo, 'w', encoding='UTF-8') as archivo:
        archivo.write(f'Nombre del catálogo: {catalogo.nombre_catalogo}\n')
        archivo.write(f"Nombre de la película: {pelicula_muestra.nombre_pelicula}\n")
        archivo.write(f"Director: {pelicula_muestra.director}\n")
        archivo.write(f"Año: {pelicula_muestra.anio}\n")
        archivo.write(f"Review: {pelicula_muestra.review}\n")

# Ejecución del programa

catalogoMuestra()
if __name__ == "__main__":
    menuPrincipal()
