import turtle
import random
import tkinter
#anda para afrente
def foward (t, passos) -> None:
    t.fd(passos)
    return
tartaruga = turtle.Turtle()
def chegada():
    tartaruga.speed(10)
    tartaruga.penup()
    tartaruga.setpos( 270, 250)
    tartaruga.right(90)
    tartaruga.color('white')

    for step in range(0, 40):
        tartaruga.begin_fill()
        tartaruga.pendown()
        tartaruga.fd(10)

        for i in range (0, 4):
            tartaruga.left(90)
            tartaruga.fd(12)
            if step %2 == 0:
                tartaruga.fillcolor('white')
            if step%2 != 0:
                tartaruga.fillcolor('black')
        tartaruga.end_fill()
    turtle.pendown()

janela = turtle.Screen()
janela.bgpic()
janela.bgcolor('black')

turtle.penup()

chegada()

#criando 4 tartaruga
vitor = turtle.Turtle()
vitor.setpos(-200,50)
vitor.fillcolor('Blue')
vitor.shape('turtle')


lais = turtle.Turtle()
lais.setpos(-200, 100)
lais.fillcolor('purple')
lais.shape('turtle')


vitoria = turtle.Turtle()
vitoria.setpos(-200, -50)
vitoria.fillcolor('Pink')
vitoria.shape('turtle')


theo = turtle.Turtle()
theo.setpos(-200, -100)
theo.fillcolor('red')
theo.shape('turtle')


janela.title('Corrida de Tartarugas')
turtle.pendown()




tartarugas = [vitor, lais, vitoria, theo]
posicao = 250
while posicao:
    for _ in range(0, 30):
        for tartaruga in tartarugas:
            foward(tartaruga, random.randrange(1,30))  

    if theo.pos() > lais.pos():
        if theo.pos() > vitor.pos():
            if theo.pos() > vitoria.pos():
                print("O ganhador é o Theo")
                theo.pencolor('white')
                theo.color('gold')
                tkinter.messagebox.showinfo(title=None, message='Theo Ganhou')
    
    if lais.pos() > vitor.pos():
        if lais.pos() > vitoria.pos():
            if lais.pos() >  theo.pos():
                print("A ganhadora é a Lais")
                lais.pencolor('white')
                lais.color('gold')
                tkinter.messagebox.showinfo(title=None, message='Lais Ganhou')

    if vitor.pos() > vitoria.pos():
        if vitor.pos() > theo.pos():
            if vitor.pos() > lais.pos():
                print("O ganhador é o Vitor")
                vitor.pencolor('white')
                vitor.color('gold')
                tkinter.messagebox.showinfo(title=None, message='Vitor Ganhou')

    if vitoria.pos() > theo.pos():
        if vitoria.pos() > lais.pos():
            if vitoria.pos() > vitor.pos():
                print("A ganhadora é a Vitoria")
                vitoria.pencolor('white')
                vitoria.color('gold')
                tkinter.messagebox.showinfo(title=None, message='Vitoria ganhou')
    break           
        
    
    
       

janela.onkeypress(exit, 'q')
janela.listen()
turtle.done()


