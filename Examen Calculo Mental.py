import time
#En esta funcion se recibe una lista con los datos del examen (pregunta y respuesta) para hacer una pregunta
#al usuario, aquí el puntaje es calculado dependiendo del tiempo tomado en contestar todas las preguntas de manera correcta.
def preguntaBase(datos):
    pr = float(input(datos[1]))
    while(True):
        if(pr==datos[0]):
            print("Respuesta correcta!")
            break
        else:
            pr = float(input("Respuesta incorrecta, intenta de nuevo: "))

#En esta funcion el puntaje se va añadiendo a una lista para posteriormente calcular el resultado.
def preguntaBase2(datos,lista):
    pr = float(input(datos[1]))
    if(pr==datos[0]):
        print("Respuesta correcta!")
        lista.append(20)
    else:
        print("Respuesta incorrecta")
        lista.append(0)

#En esta funcion se toma la lista de puntajes acumulados y se calcula el puntaje final del examen
def calcula_calificacion(lista):
    temp = 0
    for n in lista:
        temp = temp + n
    return temp

#Para este tipo de examen, se tiene que responder correctamente para pasar a la siguiente pregunta.
#Al momento de terminar el examen, se calcula el tiempo transcurrido y se calcula la puntuación
def examen1(datos):
    print("\nExamen de calculo mental")
    print("Mientras contestes incorrectamente no podras pasar a la siguiente pregunta")
    print("Tu puntaje depende del tiempo que tardes en contestar\n")
    start_time = time.time()
    preguntaBase(datos[0])
    preguntaBase(datos[1])
    preguntaBase(datos[2])
    preguntaBase(datos[3])
    preguntaBase(datos[4])
    total_time = time.time() - start_time
    puntaje_total = (120 - total_time)
    if(puntaje_total>100):
        puntaje_total = 100
    if(puntaje_total<0):
        puntaje_total = 0
    print("\nPuntaje obtenido: ", puntaje_total)

#En examen 2 y 3, lo único que cambia son las preguntas y respuestas
def examen2(datos):
    lista=[]
    print("\nExamen Multiplicaciones")
    print("Tu puntaje depende de tus aciertos")
    preguntaBase2(datos[0],lista)
    preguntaBase2(datos[1],lista)
    preguntaBase2(datos[2],lista)
    preguntaBase2(datos[3],lista)
    preguntaBase2(datos[4],lista)
    x = calcula_puntaje(lista)
    print("\nPuntaje obenido: ", x)
def examen3(datos):
    lista=[]
    print("\nExamen Divisiones")
    print("Tu puntaje depende de tus aciertos")
    preguntaBase2(datos[0],lista)
    preguntaBase2(datos[1],lista)
    preguntaBase2(datos[2],lista)
    preguntaBase2(datos[3],lista)
    preguntaBase2(datos[4],lista)
    x = calcula_puntaje(lista)
    print("\nPuntaje obenido: ", x)

#Aquí se toma el nombre completo escrito por el usuario y se crea un mensaje utilizando solo su primer nombre
def mensaje_despedida(nombre):
    new_name = nombre.split()
    final_name = new_name[0]
    print("\nFelicidades",final_name,"hiciste un buen trabajo!!\n")

datos_examen_1_1 = [[49,"¿Cual es el resultado de 7x7? "],[48,"¿Cual es el resultado de 8x6? "],
                [132,"¿Cual es el resultado de 12x11? "],[8,"¿Cual es el resultado de 72/9? "],
                [17,"¿Cual es el resultado de 36-19? "]]

datos_examen_1_2 = [[36,"¿Cual es el resultado de 120/20+30? "], [25,"¿Cual es el resultado de (65+35)/4? "],
                    [112,"¿Cual es el resultado de 16x2+80? "], [125,"¿Cual es el resultado de 25x5? "],
                    [14,"¿Cual es el resultado de (35x4)/10? "]]

datos_examen_1_3 = [[72,"¿Cual es el resultado de 2x36? "], [273,"¿Cual es el resultado de (8x6)+225? "],
                    [109,"¿Cual es el resultado de 85+24? "], [135,"¿Cual es el resultado de (81/9)x15? "],
                    [60,"¿Cual es el resultado de (50+65+5)/2? "]]
datos_examen_2_1 = [[64,"¿Cual es el resultado de 8x8? "], [28,"¿Cual es el resultado de 7x4? "],
                    [9,"¿Cual es el resultado de 3x3? "], [42,"¿Cual es el resultado de 6x7? "],
                    [200,"¿Cual es el resultado de 20x10? "]]

datos_examen_2_2 = [[64,"¿Cual es el resultado de 32x2? "], [250,"¿Cual es el resultado de 50x5? "],
                    [48,"¿Cual es el resultado de 12x4? "], [170,"¿Cual es el resultado de 85x2? "],
                    [92,"¿Cual es el resultado de 23x4? "]]

datos_examen_3_2 = [[450,"¿Cual es el resultado de 75x6? "], [216,"¿Cual es el resultado de 36x6? "],
                    [384,"¿Cual es el resultado de 96x4? "], [468,"¿Cual es el resultado de 156x3? "],
                    [552,"¿Cual es el resultado de 69x8? "]]

datos_examen_3_1 = [[3,"¿Cual es el resultado de 12/4? "], [4,"¿Cual es el resultado de 20/5? "],
                    [10,"¿Cual es el resultado de 100/10? "], [5,"¿Cual es el resultado de 50/10? "],
                    [7,"¿Cual es el resultado de 35/5? "]]

datos_examen_3_2 = [[20,"¿Cual es el resultado de 120/6? "], [8,"¿Cual es el resultado de 72/9? "],
                    [50,"¿Cual es el resultado de 250/5? "], [12,"¿Cual es el resultado de 96/8? "],
                    [13,"¿Cual es el resultado de 156/12? "]]

datos_examen_3_3 = [[36.95,"¿Cual es el resultado de 850/23? "], [21.66,"¿Cual es el resultado de 260/12? "],
                    [52.5,"¿Cual es el resultado de 1260/24? "], [52,"¿Cual es el resultado de 156/3? "],
                    [10.05,"¿Cual es el resultado de 965/96? "]]

print("Bienvenido al test de calculo mental, ingresa tu nombre completo: ")
nombre = input()
print("\nElige el tipo de prueba")
tipo_de_examen = int(input("1. Calculo mental\n2. Multiplicaciones\n3. Divisiones\n"))
dificultad = int(input("1.Basico\n2. Intermedio\n3. Casi imposible\n"))
tot = 0
while(True):
    if(tipo_de_examen == 1):
        if(dificultad == 1):
            examen1(datos_examen_1_1)
            mensaje_despedida(nombre)
        elif(dificultad == 2):
            examen1(datos_examen_1_2)
            mensaje_despedida(nombre)
        elif(dificultad == 3):
            examen1(datos_examen_1_3)
            mensaje_despedida(nombre)
        else:
            print("Opcion invalida")
    elif(tipo_de_examen == 2):
        if(dificultad == 1):
            examen2(datos_examen_2_1)
            mensaje_despedida(nombre)
        elif(dificultad == 2):
            examen2(datos_examen_2_2)
            mensaje_despedida(nombre)
        elif(dificultad == 3):
            examen2(datos_examen_2_3)
            mensaje_despedida(nombre)
        else:
            print("Opcion invalida")
    elif(tipo_de_examen == 3):
        if(dificultad == 1):
            examen3(datos_examen_3_1)
            mensaje_despedida(nombre)
        elif(dificultad == 2):
            examen3(datos_examen_3_2)
            mensaje_despedida(nombre)
        elif(dificultad == 3):
            examen3(datos_examen_3_3)
            mensaje_despedida(nombre)
        else:
            print("Opcion invalida")
    else:
        print("Opcion incorrecta de examen")
    break;