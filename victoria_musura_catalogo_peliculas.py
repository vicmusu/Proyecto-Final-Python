import os
os.system('cls')

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

# Clases y funciones para funcionalidades del catálogo

def ingresoCatalogo(): # Funcionalidad de ingreso.
        inputCatalogo = input("Inserte el nombre del catálogo sobre el que desea operar: ") # Se le solicita al usuario que ingrese el nombre de un catálogo.
        if inputCatalogo in catalogosExistentes: # El programa verifica si el catálogo ya existe. En caso de que sí, ingresa al menú.
            menuCatalogo()
        else: # En caso de que no, se indicará al usuario que dicho catálogo no existe y preguntará si desea crearlo.
             crearCatalogo = input("El catálogo no existe. ¿Desea crearlo?(si/no): ")
             if crearCatalogo == "Si": # Si decide crear un catálogo con ese nombre, se generará el mismo y se accederá al menú correspondiente.
                  print("Nuevo catálogo creado con éxito.")
                  menuCatalogo()
             else: # Si no desea crearlo, habilitará nuevamente el input para que ingrese un catálogo existente.
                  print("Intente nuevamente ingresando el nombre de un catálogo existente.")
                  ingresoCatalogo()

def menuCatalogo(): # Funcionalidad de acciones dentro del catálogo
        listadoOpciones = "1. Agregar película\n2- Listar películas\n3- Eliminar catálogo actual\n4- Volver al menú anterior\n5- Salir"
        print(listadoOpciones) # Se muestran las opciones disponibles al usuario
        inputMenu = int(input("Elija una opción: ")) # Se le solicita al usuario que ingrese un número de opción
        opcionMenu = inputMenu
        if opcionMenu == 1: # La opción 1 redirige al método agregarPelicula() de la clase CatalogoPelicula
           CatalogoPelicula.agregarPelicula()
        else:
            if opcionMenu == 2: # La opción 2 redirige al método listarPelicula() de la clase CatalogoPelicula
                CatalogoPelicula.listarPeliculas()
            else:
                if opcionMenu == 3: # La opción 3 redirige al método eliminarCatalogo() de la clase CatalogoPelicula
                    CatalogoPelicula.eliminarCatalogo()
                else:
                    if opcionMenu == 4: # La opción 4 redirige nuevamente al ingreso
                        ingresoCatalogo()
                    else: 
                        if opcionMenu == 5: # La opción 5 finaliza la sesión
                            print("Ha finalizado su sesión en el catálogo de películas")
                        else: # Cualquier otro valor numérico ingresado le indica al usuario que la opción es inválida y habilita nuevamente el menú con su input.
                            print("La opción ingresada no es válida. Vuelva a intentar")
                            menuCatalogo()

class CatalogoPelicula: # Clase para generar objetos catálogos. Contiene atributos y métodos según lo solicitado por el trabajo final.
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo

    def agregarPelicula():
        inputCatalogo = input("Inserte el nombre de la película a agregar: ")
        print("Pelicula añadida con éxito")

    def listarPeliculas():
        print("Peliculas")

    def eliminarCatalogo():
        print("Se ha eliminado el catálogo")

class Pelicula(CatalogoPelicula): # Subclase para generar objetos película. Se establece el atributo privado "review" según lo solicitado por el trabajo final. 
    # Los atributos fueron elegidos aleatoriamente por quien genera el código ya que no se especificaban los mismos.
    def __init__(self, nombre_pelicula, director, anio, __review):
        self.nombre_pelicula = nombre_pelicula
        self.director = director
        self.anio = anio
        self.__review = __review


# Ingreso al catálogo y variables de prueba

catalogoTest = CatalogoPelicula("Test", "Test")
catalogoDePrueba = catalogoTest.nombre
catalogosExistentes = [catalogoDePrueba]
print(tituloPrograma)
ingresoCatalogo()

# Probando atributo privado
# pelicula1 = Pelicula("El secreto de sus ojos", "Juan José Campanella", 2009, "Gran película. Director gorila")
# print(pelicula1.__review)