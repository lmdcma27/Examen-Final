from math import factorial

def sucesion(lista, m):
    d = 0
    subsucesiones_buenas = 0
    for x in lista:
        if int(x) % m == 0:
            d += 1
        
    for y in range(1, d + 1):
        subsucesiones_buenas += factorial(d)/(factorial(y)*factorial(d - y))
    return subsucesiones_buenas



def leerarchivo():
    entrada = open("sucesion.text", "r")
    salida = open("respuesta1.text", "w")
    T = entrada.readline()
    respuesta = []
    if int(T) > 0 and int(T) < 1001:
        for i in range(int(T)):
            vector1 = entrada.readline()
            v1 = vector1.split(" ")
            vector2 = entrada.readline()
            v2 = vector2.split(" ")
            if int(v1[0]) > 0 and int(v1[0]) < 31 and int(v1[1]) > 0 and int(v1[1]) < 1001:
                respuesta.append(sucesion(v2, int(v1[1])))
            else:
                print("Hay una entrada ínvalida")
        
        for i in respuesta:
            salida.write("{}\n".format(str(i)))
        entrada.close()
        salida.close()
    else:
        print("El número de casos de prueba no es válido")

leerarchivo()

                                    
            
        
