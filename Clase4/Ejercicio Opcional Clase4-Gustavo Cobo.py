# Ejercicio OPCIONAL
print ("\033[H\033[J")
def alumnos(alu_pro,ap):
    for alu_pro in (alu_pro):
        if alu_pro["Promedio"]>=ap:
            print("El Alumno:", alu_pro["Nombre"], "con nota: ",alu_pro["Promedio"], "esta Aprobado")
    return 
def orden(alumnos_notas):
    alumnos_ordenados = sorted(alumnos_notas, key=lambda i: i['Nombre'])
    return alumnos_ordenados
alumnos_notas= [{"Nombre":"Juan","Promedio":8},{"Nombre":"Pedro","Promedio":7},
                {"Nombre":"Jorge","Promedio":3},{"Nombre":"Aldana","Promedio":8}]
ordenar = orden(alumnos_notas)
apro = 7
alumnos(ordenar,apro)







