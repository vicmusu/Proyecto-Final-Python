import os
os.system('cls')

from pathlib import Path

"""
El funcionamiento esperado es el siguiente:
• Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
• Si el catálogo de películas no existe se creará uno nuevo. Este catálogo se va a
guardar en un archivo txt donde posteriormente se guardarán las películas. Si el
catálogo existe se podrá seguir modificando el archivo.
• Se debe mostrar un menú de opciones, que permita realizar las siguientes
operaciones:
1. Agregar Película
2. Listar Películas
3. Eliminar catálogo películas
4. Salir

Funcionamiento de las opciones:
• Agregar Película: se va a solicitar el nombre de la película y esta película se va a
guardar en el archivo txt.
• Listar Peliculas: va a mostrar todas las peliculas del catalogo y guardadas en el archivo
txt.
• Eliminar catálogo: elimina el archivo txt que corresponde al catálogo de películas.
• Salir: debe finalizar el programa mostrando un mensaje al usuario.
Implementación POO:
El programa debe implementar programación orientada a objetos.
Se solicita:
• Clase Pelicula.
* Uno de sus atributos debe ser privado.
• Clase CatalogoPelicula.
* atributo nombre
* atributo ruta_archivo
* métodos: agregar, listar, eliminar
"""

# Textos adicionales para la pantalla

tituloPrograma = "Bienvenido al catálogo de películas🍿🎦"
print(tituloPrograma)

# Clases, funciones y variables para funcionalidades del catálogo

class CatalogoPelicula: # Clase para generar objetos catálogos. Contiene atributos y métodos según lo solicitado por el trabajo final.
    def __init__(self, nombre_catalogo, ruta_archivo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_archivo = ruta_archivo

    def agregarPelicula(nombre_catalogo, ruta_archivo): # Método para agregar una película al catálogo. 
        # Solicita al usuario ingresar diferentes valores, escribiendolos en el archivo a medida que son ingresados
        # Genera un objeto "nueva_pelicula" utilizando como atributos los valores ingresados por el usuario.
        # Al final se imprime un mensaje que indica al usuario que se ha añadido correctamente la película.
        with open(f"{ruta_archivo}" , 'a', encoding="UTF-8") as archivo:
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            archivo.write(f"Nombre de la película: {nombre_pelicula}\n")
            director = input("Ingrese el nombre del director: ")
            archivo.write(f"Director: {director}\n")
            anio = input("Ingrese el año de estreno: ")
            archivo.write(f"Año de estreno: {anio}\n")
            __review = input("Ingrese una review: ")
            archivo.write(f"Review de la película: {__review}\n")
            nueva_pelicula = Pelicula(nombre_catalogo, ruta_archivo, nombre_pelicula, director, anio, __review)
        print(f"🎬 La pelicula '{nueva_pelicula.nombre_pelicula}' se ha añadido con éxito al catálogo '{nombre_catalogo}'")

    def listarPeliculas(ruta_archivo): # Método para listar las películas del catálogo.
        # Se lee el contenido del archivo devolviendo las líneas como lista. Para cada línea se omiten los saltos.
        with open(f"{ruta_archivo}" , 'r', encoding="UTF-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                print(linea.strip())

    def eliminarCatalogo(ruta_archivo): # Método para eliminar el catálogo
        # Verifica la existencia del archivo y, si existe, lo elimina.
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
            print("⚠️  Se ha eliminado el catálogo.")
        else:
            print("No se ha podido eliminar el catálogo.")

def ingresoCatalogo(): # Funcionalidad de ingreso.
    inputCatalogo = input("Inserte el nombre del catálogo sobre el que desea operar: ") # Se le solicita al usuario que ingrese el nombre de un catálogo.
    directorio = "." # Indica que la ruta del directorio es el directorio actual 
    archivos_catalogos_existentes = [f for f in os.listdir(directorio) if f.endswith('.txt')] # Lista que almacena todos los archivos de catálogos que existen
    nombre_archivos_catalogos_existentes = [os.path.splitext(f)[0] for f in archivos_catalogos_existentes] # Lista de nombres de los archivos sin extensión
    nombresCatalogos = [elemento.lower() for elemento in nombre_archivos_catalogos_existentes] # Se convierten los nombres a minúsculas para evitar inconsistencias

    def menuCatalogo(): # Funcionalidad de acciones dentro del catálogo
        listadoOpciones = "Opciones:\n1. Agregar película\n2- Listar películas\n3- Eliminar catálogo actual\n4- Volver al menú anterior\n5- Salir"
        print(listadoOpciones) # Se muestran las opciones disponibles al usuario
        inputMenu = input("Elija una opción: ") # Se le solicita al usuario que ingrese un número de opción
        opcionMenu = inputMenu
        nombre_catalogo = f"{inputCatalogo}"
        ruta_archivo = f"{inputCatalogo}.txt"
        if opcionMenu == "1": # La opción 1 redirige al método agregarPelicula() de la clase CatalogoPelicula
            CatalogoPelicula.agregarPelicula(nombre_catalogo, ruta_archivo)
        else:
            if opcionMenu == "2": # La opción 2 redirige al método listarPelicula() de la clase CatalogoPelicula
                CatalogoPelicula.listarPeliculas(ruta_archivo)
            else:
                if opcionMenu == "3": # La opción 3 redirige al método eliminarCatalogo() de la clase CatalogoPelicula
                    CatalogoPelicula.eliminarCatalogo(ruta_archivo)
                else:
                    if opcionMenu == "4":
                         ingresoCatalogo()
                    else:
                        if opcionMenu == "5": # La opción 5 finaliza la sesión
                            print("Ha finalizado su sesión en el catálogo de películas")
                        else: # Cualquier otro valor numérico ingresado le indica al usuario que la opción es inválida y habilita nuevamente el menú con su input.
                            print("La opción ingresada no es válida. Vuelva a intentar")
                            menuCatalogo()

    if inputCatalogo.lower() in nombresCatalogos: # El programa verifica si el catálogo ya existe. En caso de que sí, ingresa al menú.
                print(f"Bienvenido al catálogo '{inputCatalogo}'")
                menuCatalogo()
    else: # En caso de que no, se indicará al usuario que dicho catálogo no existe y preguntará si desea crearlo.
            crearCatalogo = input("El catálogo no existe. ¿Desea crearlo?(si/no): ")
            input_crearCatalogo = crearCatalogo.lower() # Se pasa a minúsculas para evitar inconsistencias
            if input_crearCatalogo == "si": # Si decide crear un catálogo con ese nombre, se generará el mismo y se accederá al menú correspondiente.
                with open(f"{inputCatalogo}.txt", 'a', encoding='UTF-8') as archivo:
                    archivo.write(f"Nombre del catálogo: '{inputCatalogo}'\n")
                    # ruta = Path(f"{inputCatalogo}.txt").resolve()
                    # archivo = CatalogoPelicula({inputCatalogo}, {ruta})
                    # nombre_archivo = archivo.nombre_catalogo
                    # nombresCatalogos.append(nombre_archivo)
                    print("Nuevo catálogo creado con éxito.")
                menuCatalogo()
            else: # Si no desea crearlo, habilitará nuevamente el input para que ingrese un catálogo existente.
                print("No se ha podido acceder al sistema.")

class Pelicula(CatalogoPelicula): # Subclase para generar objetos película. Se establece el atributo privado "review" según lo solicitado por el trabajo final. 
    # Los atributos fueron elegidos aleatoriamente por quien genera el código ya que no se especificaban los mismos.
        def __init__(self, nombre_catalogo, ruta_archivo, nombre_pelicula, director, anio, __review):
            super().__init__(nombre_catalogo, ruta_archivo)
            self.nombre_pelicula = nombre_pelicula
            self.director = director
            self.anio = anio
            self.__review = __review

        @property
        def review(self):
             return self.__review
        
        @review.setter
        def nueva_review(self, review_actualizada):
             if isinstance(review_actualizada, any):
                  self.__review = review_actualizada
             

def catalogoMuestra(): # Función que genera un catálogo de muestra para el programa
    catalogo = CatalogoPelicula('Catalogo de Muestra', 'CatalogoMuestra.txt')
    pelicula_muestra = Pelicula(f"{catalogo.nombre_catalogo}", {catalogo.ruta_archivo},"Tiempo de valientes", "Damián Szifron", 2005, "Un clásico argentino que nos muestra la relación entre un psicoanalista y un policia")
    with open(f'{catalogo.ruta_archivo}', 'w', encoding='UTF-8') as archivo:
        archivo.write(f'Nombre del catálogo: {catalogo.nombre_catalogo}\n')
        archivo.write(f"Nombre de la película: {pelicula_muestra.nombre_pelicula}\n")
        archivo.write(f"Director: {pelicula_muestra.director}\n")
        archivo.write(f"Año: {pelicula_muestra.anio}\n")
        archivo.write(f"Review: {pelicula_muestra.review}\n")

# Ingreso al catálogo y variables de prueba

catalogoMuestra()
ingresoCatalogo()

