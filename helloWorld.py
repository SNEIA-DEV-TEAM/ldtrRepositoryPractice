import time
from tkinter import Y

helloList = ['H','e','l','l','o',' ','w','o','r','l','d']

runOrNot = True

while runOrNot == True:
    for i in range(len(helloList)):
        print(helloList[i])
        time.sleep(0.1)
    print(" ")

def funcionDePrueba2(a, b):
    try:
        return(a + b)
    except:
        print('???????????????????????????????????????????????')

print funcionDePrueba2(1, 2)

def sumar(a, b):
    return a + b
z = sumar(1, 2)
def dividir(a, b):
    return a / b
p = dividir(1, 2)
