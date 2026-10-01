def mostrar_encabezado_escuela():
    print("Universidad Tecnologica de Xicotepec")
    print("Registro de Calificaciomnj")


def obtener_nota_minima_aprobatoria():
    return 6.0


def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"


def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)


def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)

    print("***** BOLETA *****")
    print("Nombre:", nombre_alumno)
    print("Nota de examenes:", nota_examenes)
    print("Nota de tareas:", nota_tareas)
    print("Nota final:", nota_final)
    print("Estado académico:", estado)
    print("******************")

    if nota_final < nota_minima:
        print("Examen extraordinario: Siiiuuu")
    else:
        print("Examen extraordinario: Np")


mostrar_encabezado_escuela()
generar_boleta("Yordi", 8.5, 9.0) 