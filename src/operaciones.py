from math import pow
def separacionSumaResta(texto):
    apperturaParentesis = False
    aux = 0
    cantidades = []
    if '{' in texto:
        for i in range(len(texto)):
            if apperturaParentesis:
                if texto[i] == '}':
                    apperturaParentesis = False
            else:
                if texto[i] == '{':
                    apperturaParentesis = True
            #print(f'{texto[i]}: {apperturaParentesis}')
            if (texto[i] == '+' or texto[i] == '-') and not(apperturaParentesis):
                cantidades.append(aux)
            aux += 1
    else:
        for i in range(len(texto)):
            if apperturaParentesis:
                if texto[i] == ')':
                    apperturaParentesis = False
            else:
                if texto[i] == '(':
                    apperturaParentesis = True
            #print(f'{texto[i]}: {apperturaParentesis}')
            if (texto[i] == '+' or texto[i] == '-') and not(apperturaParentesis):
                cantidades.append(aux)
            aux += 1
    cantidades.append(aux)
    if cantidades[0] == 0:
        cantidades.pop(0)
    return cantidades

def separacionParentesis(vector):
    for i in range(len(vector)):
        if len(vector[i]) > 1:
            if '(' in vector[i]:
                aux = ''
                aux2 = 0
                aux3 = 0
                for k in range(len(vector[i])):
                    aux2 += 1
                    if vector[i][k] == '(':
                        break
                for k in range(len(vector[i])):
                    aux3 += 1
                    if vector[i][k] == ')':
                        break
                apertura = False
                for j in range(len(vector[i])):
                    turno = True
                    if apertura:
                        if vector[i][j] == ')':
                            apertura = False
                            turno = False
                    else:
                        if vector[i][j] == '(':
                            apertura = True
                            turno = False
                    if apertura and turno:
                        aux = f'{aux}{vector[i][j]}'

                cant = separacionSumaResta(aux)
                aux = separacionVector(aux,cant)
                aux = sumaVector(aux)
                aux3 -= 1
                if vector[i][0] != '(':
                    vector[i] = f'{vector[i][:aux2]}{aux}{vector[i][aux3:]}'
                else:
                    vector[i] = f'{vector[i][1:aux2]}{aux}{vector[i][aux3:]}'
                vector[i] = vector[i].replace('-(', '-1+*')
                vector[i] = vector[i].replace('+(', '+1+*')
                vector[i] = vector[i].replace(')', '')
                if '(-' in vector[i]:
                    vector[i] = vector[i].replace('(-', '-*')
                else:
                    vector[i] = vector[i].replace('(', '+*')

    return vector

def separarCorchetes(vector):
    for i in range(len(vector)):
        if len(vector[i]) > 1:
            if '{' in vector[i]:
                aux = ''
                aux2 = 0
                aux3 = 0
                for k in range(len(vector[i])):
                    aux2 += 1
                    if vector[i][k] == '{':
                        break
                for k in range(len(vector[i])):
                    aux3 += 1
                    if vector[i][k] == '}':
                        break
                apertura = False
                for j in range(len(vector[i])):
                    turno = True
                    if apertura:
                        if vector[i][j] == '}':
                            apertura = False
                            turno = False
                    else:
                        if vector[i][j] == '{':
                            apertura = True
                            turno = False
                    if apertura and turno:
                        aux = f'{aux}{vector[i][j]}'

                cant = separacionSumaResta(aux)
                aux = separacionVector(aux,cant)
                aux = sumaVector(aux)
                aux3 -= 1
                vector[i] = f'{vector[i][:aux2]}{aux}{vector[i][aux3:]}'
                vector[i] = vector[i].replace('-{', '-1+*')
                vector[i] = vector[i].replace('+}', '+1+*')
                vector[i] = vector[i].replace('}', '')
                if '{-' in vector[i]:
                    vector[i] = vector[i].replace('{-', '-*')
                else:
                    vector[i] = vector[i].replace('{', '+*')
    return vector

def separacionVector(texto,cantidades):
    vector = []
    #print(texto)
    #print(cantidades)
    vector.append(texto[:cantidades[0]])
    try:
        for i in range(len(cantidades)):
            vector.append(texto[cantidades[i]:cantidades[i+1]])
    except:
        pass
    return vector

def sumaVector(vector):
    resultado = 0
    aux = 0
    n =  len(vector)
    while aux < n:
        try:
            if '^' in vector[aux+1]:
                aux1 = vector[aux]
                aux2 = vector[aux+1][2:]
                potencia = pow(float(aux1),float(aux2))
                resultado += potencia
                aux += 1
            elif '*' in vector[aux+1]:
                if '^' in vector[aux+2]:
                    aux1 = vector[aux+1][2:]
                    aux2 = vector[aux+2][2:]
                    potencia = pow(float(aux1),float(aux2))
                    resultado += float(vector[aux])*potencia
                    aux += 2
                else:
                    resultado += float(vector[aux]) * float(vector[aux+1][2:])
                    aux += 1
            else:
                resultado += float(vector[aux])
        except:
            try:
                resultado += float(vector[aux])
            except:pass
        aux += 1
    return resultado

def solucionPotencias(vector):
    for i in range(len(vector)):
        if '^' in vector[i]:
            vector[i] = vector[i].replace('^','+^')
            cantidades = separacionSumaResta(vector[i])
            vector[i] = separacionVector(vector[i],cantidades)
            vector[i] = separarCorchetes(vector[i])
            vector[i] = separacionParentesis(vector[i])
            vector[i] = sumaVector(vector[i])
    return vector

def calculos(texto):
    #print(texto)
    cantidades = separacionSumaResta(texto)
    vector = separacionVector(texto,cantidades)
    #print(vector)
    vector = separacionParentesis(vector)
    #print(vector)
    vector = separarCorchetes(vector)
    #print(vector)
    vector = solucionPotencias(vector)
    #print(vector)
    #print('----------------------------------')
    suma = sumaVector(vector)
    #print(suma)
    return suma

def main(texto = '(1)^4-3{-(1)+5}^2-2'):
    texto = texto.replace(' ','')
    texto = texto.replace('*','+*')
    resultado = calculos(texto)
    return resultado

def validarFuncion(texto):
    aux = texto.replace('(','{')
    aux = texto.replace(')','}')
    aux = texto.replace('x','(1)')
    valida = False
    try:
        if main(aux):
            valida = True
        else:
            aux = texto.replace('x','(-2)')
            if main(aux):
                valida = True
    except:
        pass
    return valida

main()
#x^4-3(-x+5)^2-2
#(1)^4-3(-(1)+5)^2-2
#1+5-3(8+1-4)+1-4
