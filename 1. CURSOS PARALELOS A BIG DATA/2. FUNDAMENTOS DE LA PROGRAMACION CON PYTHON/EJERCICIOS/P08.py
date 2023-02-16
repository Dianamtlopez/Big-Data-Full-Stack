import turtle

miTortugaLucera = turtle.Turtle()

lados = int(input("¿Cuantos lados quieres?:"))

for _ in range(0,lados):
    #lo que se tabula se llama bloque de codigo
    miTortugaLucera.forward(50)
    miTortugaLucera.left(360/lados)


