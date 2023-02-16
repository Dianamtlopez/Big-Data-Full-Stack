#INTRODUCIR DATOS
dia = int(input("Ingrese el día: "))
mes = input("Ingrese el mes: ")

#CONSTANTES
enero = 31
febrero = 28
marzo = 31
abril = 30
mayo = 31
junio = 30
julio = 31
agosto = 31
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

#CONTAR LOS DÍAS
dias_transcurridos = 0
if(mes == '1'):
    dias_transcurridos = dia
elif(mes == '2'):
    dias_transcurridos = enero + dia
elif(mes == '3'):
    dias_transcurridos = enero + febrero + dia
elif(mes == '4'):
    dias_transcurridos = enero + febrero + marzo + dia
elif(mes == '5'):
    dias_transcurridos = enero + febrero + marzo + abril + dia
elif(mes == '6'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + dia
elif(mes == '7'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + dia
elif(mes == '8'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + julio + dia
elif(mes == '9'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + julio + agosto + dia
elif(mes == '10'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + dia
elif(mes == '11'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + dia
elif(mes == '12'):
    dias_transcurridos = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + dia
else:
    print("Error, el mes ingresado está por fuera del rango!")
    
#IMPRIMIR DATOS
print("a los",dia,"días, del mes",mes,"hay:",dias_transcurridos,"días transcurridos")