# Ejercicio OPCIONAL

# Genero una lista de 20 alumnos con sus notas
alumnos_notas= [{"Apellido y Nombre":"Lopez, Juan","Nota1":8,"Nota2":4,"Nota3":6,"Nota4":6,"Nota5":10,"Nota6":10},
                {"Apellido y Nombre":"Vargas, Pedro","Nota1":3,"Nota2":4,"Nota3":10,"Nota4":1,"Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Fernandez, Jorge","Nota1":6,"Nota2":6,"Nota3":6,"Nota4":6,"Nota5":10,"Nota6":""},
                {"Apellido y Nombre":"Lima, Marcelo","Nota1":7,"Nota2":10,"Nota3":8,"Nota4":"","Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Gonzalez, Pablo","Nota1":8,"Nota2":1,"Nota3":1,"Nota4":6,"Nota5":10,"Nota6":10},
                {"Apellido y Nombre":"Estevez, Julian","Nota1":10,"Nota2":2,"Nota3":6,"Nota4":6,"Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Rodriguez, Lautaro","Nota1":2,"Nota2":3,"Nota3":7,"Nota4":6,"Nota5":10,"Nota6":""},
                {"Apellido y Nombre":"Zalasar, Lionel","Nota1":1,"Nota2":4,"Nota3":8,"Nota4":"","Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Paso, Ezequiel","Nota1":4,"Nota2":6,"Nota3":10,"Nota4":6,"Nota5":10,"Nota6":10},
                {"Apellido y Nombre":"Revoredo, Lisandro","Nota1":9,"Nota2":7,"Nota3":9,"Nota4":6,"Nota5":10,"Nota6":""},
                {"Apellido y Nombre":"Ramos, Alejandro","Nota1":8,"Nota2":4,"Nota3":8,"Nota4":6,"Nota5":"","Nota6":""},
                {"Apellido y Nombre":"De Martin, Esteban","Nota1":5,"Nota2":10,"Nota3":7,"Nota4":"","Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Dalesio, Enzo","Nota1":8,"Nota2":4,"Nota3":6,"Nota4":6,"Nota5":10,"Nota6":10},
                {"Apellido y Nombre":"Estorte, Julio","Nota1":3,"Nota2":6,"Nota3":5,"Nota4":6,"Nota5":10,"Nota6":""},
                {"Apellido y Nombre":"Molina, Maria","Nota1":6,"Nota2":8,"Nota3":4,"Nota4":6,"Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Acevedo, Nicolas","Nota1":8,"Nota2":10,"Nota3":10,"Nota4":"","Nota5":"","Nota6":""},
                {"Apellido y Nombre":"Ronconi, Sol","Nota1":2,"Nota2":1,"Nota3":9,"Nota4":6,"Nota5":10,"Nota6":10},
                {"Apellido y Nombre":"Escribano, Yamila","Nota1":1,"Nota2":4,"Nota3":8,"Nota4":6,"Nota5":10,"Nota6":""},
                {"Apellido y Nombre":"Gomez, Julieta","Nota1":9,"Nota2":5,"Nota3":4,"Nota4":6,"Nota5":"","Nota6":""},
                {"Apellido y Nombre":"De luca, Camila","Nota1":10,"Nota2":2,"Nota3":2,"Nota4":"","Nota5":"","Nota6":""}]

# Genero una funcion para listar los Apellidos y Nombres de los Alumnos
def alumnos(alu_apenom):
    for alu_apenom in (alu_apenom):
        print(alu_apenom["Apellido y Nombre"])       
    return 
# Genero una funcion para ordenar Apellidos y Nombres de los Alumnos
def ordenalf(alumnos_notas):
    alumnos_ordenados = sorted(alumnos_notas, key=lambda i: i['Apellido y Nombre'])
    return alumnos_ordenados
# Genero una funcion para mostrar los Apellidos y Nombres de los Alumnos con sus notas
def alumnosynotas(alu_apenomynotas):
    for alu_apenomynotas in (alu_apenomynotas):
            print(alu_apenomynotas["Apellido y Nombre"], "--Notas: ", 
            alu_apenomynotas["Nota1"],"-",
            alu_apenomynotas["Nota2"],"-",
            alu_apenomynotas["Nota3"],"-",
            alu_apenomynotas["Nota4"],"-",
            alu_apenomynotas["Nota5"],"-",
            alu_apenomynotas["Nota6"])
    return 
# Genero una funcion para mostrar los Apellidos y Nombres de los Alumnos con sus promedios
def alumnosprome(alu_apenomynotas):
    for alu_apenomynotas in (alu_apenomynotas):
            # pregunto si la nota numero 6, no es vacia, es decir que tiene una nota 6
            if alu_apenomynotas["Nota6"]!="":
                # Calculo el promedio de ese alumno por sus 6 notas
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"]+
                alu_apenomynotas["Nota6"])/6)
                print(alu_apenomynotas["Apellido y Nombre"], "Promedio: ", promedio)
            # pregunto si la nota numero 5, no es vacia, es decir que tiene una nota 5
            elif alu_apenomynotas["Nota5"]!="":
                # Calculo el promedio de ese alumno por sus 5 notas
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"])/5)
                print(alu_apenomynotas["Apellido y Nombre"], "Promedio: ", promedio)
            # pregunto si la nota numero 4, no es vacia, es decir que tiene una nota 4
            elif alu_apenomynotas["Nota4"]!="":
                # Calculo el promedio de ese alumno por sus 4 notas
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"])/4)
                print(alu_apenomynotas["Apellido y Nombre"], "Promedio: ", promedio)
            else:
            # por defecto tiene 3 notas si o si
            # Calculo el promedio de ese alumno por sus 3 notas
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"])/3)
                print(alu_apenomynotas["Apellido y Nombre"], "Promedio: ", promedio)
    return 

def alumnosnotamedia(alu_apenomynotas):
    # pongo un acumulador en Cero para sumar los promedios de todos los alumnos
    acumpromedio = 0
    for alu_apenomynotas in (alu_apenomynotas):
            # con la misma mecanica que la funcion anterior voy acumulando los promedios de acuerdo a la cantidad
            # de notas que posee cada alumno
            if alu_apenomynotas["Nota6"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"]+
                alu_apenomynotas["Nota6"])/6)
                acumpromedio = acumpromedio + promedio    
            elif alu_apenomynotas["Nota5"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"])/5)
                acumpromedio = acumpromedio + promedio    
            elif alu_apenomynotas["Nota4"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"])/4)
                acumpromedio = acumpromedio + promedio    
            else:
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"])/3)
                acumpromedio=acumpromedio+promedio
    # Una vez que tengo la suma de todos los promedios, sabemos que la cantidad de alumnos son 20
    # dividimos y sacamos el promedio general o la nota media de todos los alumnos
    print("Nota media de todos los alumnos: ", acumpromedio/20)
    return

def alumnosaprobadosnotamedia(alu_apenomynotas):
     # pongo un acumulador en Cero para sumar los promedios de todos los alumnos Aprobados
     # pongo un acumulador en Cero para sumar la cantidad de alumnos Aprobados
    acumpromedio = 0
    cantaluaprobados = 0
    for alu_apenomynotas in (alu_apenomynotas):
            # con la misma mecanica que la funcion anterior voy acumulando los promedios de acuerdo a la cantidad
            # de notas que posee cada alumno
            if alu_apenomynotas["Nota6"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"]+
                alu_apenomynotas["Nota6"])/6)
                # Solo Acumulo los promedios de los alumnos que estan aprobados 
                # Solo Sumo los alumnos que aprobaron
                if promedio >= 7:
                    acumpromedio = acumpromedio + promedio
                    cantaluaprobados = cantaluaprobados + 1
            elif alu_apenomynotas["Nota5"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"])/5)
                if promedio >= 7:
                    acumpromedio = acumpromedio + promedio
                    cantaluaprobados = cantaluaprobados + 1
            elif alu_apenomynotas["Nota4"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"])/4)
                if promedio >= 7:
                    acumpromedio = acumpromedio + promedio
                    cantaluaprobados = cantaluaprobados + 1
            else:
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"])/3)
                if promedio >= 7:
                    acumpromedio = acumpromedio + promedio
                    cantaluaprobados = cantaluaprobados + 1
    # Al finalizar solo sumo los promedios de los alumnos aprobados y conto la cantidad de alumnos aprobados
    # hacemos la division y me queda el promedio de los alumnos aprobados
    print("Nota media de los ",cantaluaprobados," alumnos Aprobados: ", acumpromedio/cantaluaprobados)
    return
def alumnossuspendidosnotamedia(alu_apenomynotas):
    # pongo un acumulador en Cero para sumar los promedios de todos los alumnos Suspendidos
    # pongo un acumulador en Cero para sumar la cantidad de alumnos Suspendidos
    acumpromedio = 0
    cantalususpendidos = 0
    for alu_apenomynotas in (alu_apenomynotas):
            if alu_apenomynotas["Nota6"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"]+
                alu_apenomynotas["Nota6"])/6)
                # En este caso tomamos los alumnos como suspendidos aquellos con su promedio de notas inferior a 7
                if promedio < 7:
                    acumpromedio = acumpromedio + promedio
                    cantalususpendidos = cantalususpendidos + 1              
            elif alu_apenomynotas["Nota5"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"]+
                alu_apenomynotas["Nota5"])/5)
                if promedio < 7:
                    acumpromedio = acumpromedio + promedio
                    cantalususpendidos = cantalususpendidos + 1
            elif alu_apenomynotas["Nota4"]!="":
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"]+
                alu_apenomynotas["Nota4"])/4)
                if promedio < 7:
                    acumpromedio = acumpromedio + promedio
                    cantalususpendidos = cantalususpendidos + 1
            else:
                promedio = ((alu_apenomynotas["Nota1"]+ alu_apenomynotas["Nota2"]+alu_apenomynotas["Nota3"])/3)
                if promedio < 7:
                    acumpromedio = acumpromedio + promedio
                    cantalususpendidos = cantalususpendidos + 1
    # Al finalizar solo sumo los promedios de los alumnos suspendidos y conto la cantidad de alumnos suspendidos
    # hacemos la division y me queda el promedio de los alumnos suspendidos
    print("Nota media de los ",cantalususpendidos," alumnos Suspendidos: ", acumpromedio/cantalususpendidos)
    return
print ("\033[H\033[J")
ing = 0
# Utilizo un While para que el menu se repita hasta que deseen salir del programa
# Opcion 9
while ing!= 9:
    print("                 Listado de Alumnos del Colegio")
    print ("")
    print ("1-Listado de Alumnos ordenado por Nombre Alfabeticamente")
    print ("2-Listado de Alumnos ordenado por Nombre Alfabeticamente, con sus NOTAS")
    print ("3-Listado de Alumnos ordenado por Nombre Alfabeticamente, con sus PROMEDIOS")
    print ("4-Promedio general denotas de todos los Alumnos")
    print ("5-Listado de Alumnos APROBADOS")
    print ("6-Listado de Alumnos SUSPENDIDOS")
    print ("")
    ing = int(input("Ingrese la opcion deseada, toque 9 para salir del Programa: "))
    # se identifican las opciones con numeros y ejecuta cada funcion de acuerdo a la opcion elegida
    if ing == 1:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnos(ordenar)
        # esto es para que permita visualizar los datos antes de volver al menu nuevamente.
        input("Pulse una tecla para continuar...")
    elif ing ==2:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnosynotas(ordenar)
        input("Pulse una tecla para continuar...")
    elif ing ==3:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnosprome(ordenar)
        input("Pulse una tecla para continuar...")
    elif ing ==4:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnosnotamedia(ordenar)
        input("Pulse una tecla para continuar...")
    elif ing ==5:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnosaprobadosnotamedia(ordenar)
        input("Pulse una tecla para continuar...")
    elif ing ==6:
        print ("\033[H\033[J")
        ordenar = ordenalf(alumnos_notas)
        alumnossuspendidosnotamedia(ordenar)
        input("Pulse una tecla para continuar...")
    else:
        # con la opcion 9 salimos del Programa definitivamente
        ing==9
        print("Termino el programa")
        
