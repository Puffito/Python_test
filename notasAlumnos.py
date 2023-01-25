

class Alumno:
    alumnosTotales = 0
    
    def __init__(self,name,nota):
        self.name = name
        self.nota = nota
        Alumno.alumnosTotales+=1
        
        
def main():    
    salir = False
    while not salir:
        opcion = int(input("""
                        Bienvenido a la base de datos de las Notas del colegio
                        ¿Qué desea hacer?
                        1. Ver notas
                        2. Añadir nota
                        3. Borrar nota
                        4. Estadísticas
                        5. Ver suspendidos
                        6. Salir
                        """))
        if opcion == 1: verNotas()
        elif opcion == 2: anadirNota()
        elif opcion == 3: borrarNota()
        elif opcion == 4: estadistica()
        elif opcion == 5: verSuspensos()
        elif opcion == 6: salir = True
    print("Gracias por usar la base de datos")



def verNotas():
    contador = 0
    if Alumno.alumnosTotales > 0:
        for x in database:
            print("Nota {0}: {1} {2}".format(contador,x.name,x.nota))
            contador+=1
    else: print("No hay alumnos suficientes")

def anadirNota():
    nombre = input("Introduzca el nombre del Alumno")
    nota = int(input("Introduzca la nota del Alumno"))
    database.append(Alumno(nombre,nota))

def borrarNota():
    posición = int(input("Introduce la posición de la nota que deseas borrar"))
    if posición < Alumno.alumnosTotales and posición > 0:
       del database[posición]
       Alumno.alumnosTotales-=1

def estadistica():
    notaMax = 0
    notaMin = 11
    suma = 0
    for x in database:
        suma += x.nota
        if x.nota > notaMax : notaMax = x.nota
        if x.nota < notaMin : notaMin = x.nota
    print("""
            La media de las notas de los alumnos es: {0}
            La nota más alta es: {1}
            La nota más baja es: {2}
            """.format(suma/Alumno.alumnosTotales,notaMax,notaMin))

def verSuspensos():
    print("Los alumnos suspensos son:")
    for x in range(Alumno.alumnosTotales):
        if database[x].nota <5 : print("{0} {1}".format(database[x].name,database[x].nota))

database = []
        
main()