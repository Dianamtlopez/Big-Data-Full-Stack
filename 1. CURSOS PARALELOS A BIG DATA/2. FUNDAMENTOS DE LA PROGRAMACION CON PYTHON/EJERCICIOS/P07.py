import turtle

miTortugaLucera = turtle.Turtle()

lados = int(input("¿Cuantos lados quieres?:"))

if lados == 3:
    for _ in range(0,3):
        #lo que se tabula se llama bloque de codigo
        miTortugaLucera.forward(50)
        miTortugaLucera.left(120)
elif lados == 4:
    for _ in range(0,4):
        #lo que se tabula se llama bloque de codigo
        miTortugaLucera.forward(50)
        miTortugaLucera.left(90)
else:
    print("No se dibujar más que cuadrados y triangulos")

