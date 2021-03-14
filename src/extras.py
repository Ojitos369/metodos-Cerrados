import os
def limpiar():
    try:
        os.system('clear')
    except:
        os.system('cls')

def pausar():
    input('Presiona Enter para continuar')

def convertir(num):
    try:
        num = int(num)
    except:
        if num == '0' or num == 0:
            num = 0
        else:
            num = False
    return num

def convertirFloat(num):
    try:
        num = float(num)
    except:
        if num == '0' or num == 0:
            num = 0
        else:
            num = False
    return num