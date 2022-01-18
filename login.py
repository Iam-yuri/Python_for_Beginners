from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Head
Label(root, text="Seu registro aqui", font="ar 15 bold").grid(row=0, column=3)

#Nome dos atributos
name = Label(root, text="Nome")
phone = Label(root, text="Telefone")
gender = Label(root, text="Gênero")
emergency = Label(root, text="Emergencia")
paymentmood = Label(root, text="Forma de pagamento")

# Caixa para digitar
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variavel para amarzenar dados
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#Criando entrada para os dados
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)

#Pacotes de entrada
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#Criando uma caixa de seleção
checkbnt = Checkbutton(text="Me lembrar?", variable = checkvalue)
checkbnt.grid(row=6, column= 3)

#Botão de entrada
Button(text="Entar", command=getvals).grid(row=7, column=3)

root.mainloop()