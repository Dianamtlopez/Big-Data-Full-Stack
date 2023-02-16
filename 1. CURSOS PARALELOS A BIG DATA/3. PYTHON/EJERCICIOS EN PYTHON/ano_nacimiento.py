#Quien Eres
nombre=input('Como te llamas?: ')
print('Hola,',nombre)

#Toma de datos
edad=int(input('Ingrese su edad: '))
anio_actual=int(input('Ingrese el año actual: '))
cumplido=input('Has cumplido años ya (S/N)?: ')
cumplido=cumplido.upper()

#Cálculos
if(cumplido=="S"):
    anio_nacimiento=anio_actual-edad
elif(cumplido=="N"):
    anio_nacimiento=(anio_actual-edad-1)

#Presentacion de Resultados
print(nombre,'Usted nacio en: ',anio_nacimiento)