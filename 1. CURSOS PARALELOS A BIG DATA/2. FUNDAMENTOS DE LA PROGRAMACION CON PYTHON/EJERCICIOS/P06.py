import turtle

miTortugaLucera = turtle.Turtle()

respuesta = input("Quieres un triangulo?:")
respuesta = respuesta.upper()

if respuesta == "S":
    for _ in range(0,3):
        #lo que se tabula se llama bloque de codigo
        miTortugaLucera.forward(50)
        miTortugaLucera.left(120)
else:
    for _ in range(0,4):
        #lo que se tabula se llama bloque de codigo
        miTortugaLucera.forward(50)
        miTortugaLucera.left(90)

