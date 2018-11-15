
entrada = open("archivo.text", "r")
    
tamaño = int(entrada.readline())
matriz = []

for i in range(tamaño): #crear matriz
    linea = str(entrada.readline())
    nueva=linea.split(" ")
    matriz.append(nueva)



matrizsus = matriz
filas1 = []
columnas = []

#recorrer filas y columnas para obtener los valores mas pequeños de las filas y los mas grandes de las columnas
for i in range(tamaño):
    filas = []
    for x in matrizsus[i]:
        filas.append(int(x))
    filas = sorted(filas)
    filas1.append(filas[0])
    colum = []
    for y in range(tamaño):
        colum.append(int(matrizsus[y][i]))
    columnas.append(sorted(colum)[-1])

r_max = sorted(filas1)[-1]
c_min = sorted(columnas)[0]
#Se consideran los siguientes casos: el primero verifica que c_min > r_max, entonces cuenta los valores que son mayores a r_max 
# en la columna de c_min y los valores que son menores a c_min en la fila de r_max, por último imprime el conteo mas pequeño.
#El segundo caso es r_max > c_min, entonces cuenta en la lista columnas los valores que son menores a r_max y en la lista filas1 
# los valores que son mas mayores a c_min, por último imprime el conteo mas pequeño.

if r_max == c_min:
    print("la matriz es chilera")

posiciony = columnas.index(c_min)
posicionx = filas1.index(r_max)
contadorfila = 0
contadorcolumna = 0
if c_min > r_max:
    for i in range(tamaño):
        if c_min > int(matrizsus[posicionx][i]):
            contadorfila += 1
        if r_max < int(matrizsus[i][posiciony]):
            contadorcolumna += 1
    if contadorfila < contadorcolumna:
        print("La cantidad mínima de movimientos es:", contadorfila)
    else:
        print("La cantidad mínima de movimientos es:", contadorcolumna)
elif c_min < r_max:
    for i in range(tamaño):
        if r_max > columnas[i]:
            contadorcolumna += 1
        if c_min < filas1[i]:
            contadorfila += 1
    if contadorcolumna < contadorfila:
        print("La cantidad mínima de movimientos es:", contadorcolumna)
    else:
        print("La cantidad mínima de movimientos es:", contadorfila)

        

