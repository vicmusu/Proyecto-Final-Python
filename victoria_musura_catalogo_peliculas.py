# Importación de módulos
import os
from pathlib import Path

# Clases, funciones y variables para funcionalidades del catálogo

class CatalogoPelicula: # Clase para generar objetos catálogos. Contiene atributos y métodos según lo solicitado por el trabajo final.
    def __init__(self, nombre_catalogo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"
        self.peliculas = []

    def agregarPelicula(self): # Método para agregar una película al catálogo. 
        # Solicita al usuario ingresar diferentes valores, escribiendolos en el archivo a medida que son ingresados
        # Genera un objeto "nueva_pelicula" utilizando como atributos los valores ingresados por el usuario.
        # Al final se imprime un mensaje que indica al usuario que se ha añadido correctamente la película.
        with open(self.ruta_archivo , 'a', encoding="UTF-8") as archivo:
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            archivo.write(f"\nNombre de la película: {nombre_pelicula}\n")
            director = input("Ingrese el nombre del director: ")
            archivo.write(f"Director: {director}\n")
            anio = input("Ingrese el año de estreno: ")
            archivo.write(f"Año de estreno: {anio}\n")
            review = input("Ingrese una review: ")
            archivo.write(f"Review de la película: {review}\n")
            nueva_pelicula = Pelicula(nombre_pelicula, director, anio, review)
            self.peliculas.append(nueva_pelicula)
        print(f"🎬 La pelicula '{nombre_pelicula}' se ha añadido con éxito al catálogo '{self.nombre_catalogo}'")

    def listarPeliculas(self): # Método para listar las películas del catálogo.
        # Se lee el contenido del archivo devolviendo las líneas como lista. Para cada línea se omiten los saltos.
        with open(self.ruta_archivo , 'r', encoding="UTF-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                print(linea.strip())

    def eliminarCatalogo(self): # Método para eliminar el catálogo
        # Verifica la existencia del archivo y, si existe, lo elimina.
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("⚠️  Se ha eliminado el catálogo.")
        else:
            print("No se ha podido eliminar el catálogo.")
    
class Pelicula(): # Clase para generar objetos película. Se establece el atributo privado "review" según lo solicitado por el trabajo final. 
    # Los atributos fueron elegidos aleatoriamente por quien genera el código ya que no se especificaban los mismos.
        def __init__(self, nombre_pelicula, director, anio, review):
            self.nombre_pelicula = nombre_pelicula
            self.director = director
            self.anio = anio
            self.__review = review

        @property
        def review(self):
             return self.__review
        
        @review.setter
        def nueva_review(self, review_actualizada):
             if isinstance(review_actualizada, str):
                  self.__review = review_actualizada


