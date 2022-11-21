num=int(input("la posicion inicial"))
num2=int(input("la posicion final"))
num3=int(input("El numero que quiere multiplicar"))
opt=str(input("quieres un salto  si o no"))
if opt=="si":
    answ=int(input("Ingrese el salto"))

    for i in range(num, num2, answ):
        print("La tabla de multiplicaion es", num3, "*", i, " = ", num3 * i,"Ya que el salto fue de:" , answ)
else:
    for i in range(num,num2,2):
        print("La tabla de multiplicaion es",num3,"*",i," = ",num3*i)