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
    #print(f'Vector de entrada a suma: {vector}')
    resultado = 0
    aux = 0
    n =  len(vector)
    while aux < n:
        restemp = 0
        #print(f'Vector {vector} en aux de suma: {vector[aux]}')
        try:
            if (('-*' in vector[aux] or '+*' in vector[aux])or ('-/' in vector[aux] or '+/' in vector[aux])) and len(vector[aux]) > 5:
                #print(f'Entrada en -* or +* de: {vector[aux]}')
                try:
                    cantidades = separacionSumaResta(vector[aux])
                    vector[aux] = separacionVector(vector[aux],cantidades)
                    #print(f'Vector despues de separar: {vector[aux]}')
                    vector[aux] = sumaVector(vector[aux])
                except:
                    pass
                #print(vector[aux])
                #print(f'Vector Final despues de separacion en suma: {vector[aux]}')
        except: pass
        try:
            #print('Try 1')
            #print(f'vector[aux+1]: {vector[aux+1]}')
            if '^' in vector[aux+1]:
                aux1 = float(vector[aux])
                aux2 = float(vector[aux+1][2:])
                """ if vector[aux][0] == '-':
                    aux1 *= -1 """
                potencia = pow(aux1,aux2)
                restemp = potencia
                resultado += restemp
                aux += 1
            elif '*' in vector[aux+1]:
                #print(f'entrada en * in vector[aux+1]')
                try:
                    if '^' in vector[aux+2]:
                        aux1 = vector[aux+1][2:]
                        aux2 = vector[aux+2][2:]
                        #print(f'Potencia * aux1: {aux1}; aux2: {aux2}')
                        aux1 = float(aux1)
                        aux2 = float(aux2)
                        if vector[aux+1][0] == '-':
                            aux1 *= -1
                        potencia = pow(aux1,aux2)
                        restemp = float(vector[aux])*potencia
                        resultado += restemp
                        aux += 2
                    else:
                        #print(f'vector[aux]: {vector[aux]}')
                        #print(f'vector[aux+1]: {vector[aux+1]}')
                        aux1 = vector[aux]
                        aux2 = vector[aux+1][2:]
                        #print(f'Multipplicacion aux1: {aux1}; aux2: {aux2}')
                        aux1 = float(aux1)
                        aux2 = float(aux2)
                        if vector[aux+1][0] == '-':
                            aux2 *= -1
                        restemp = aux1 * aux2
                        resultado += restemp
                        aux += 1
                except:
                    #print(f'vector[aux]: {vector[aux]}')
                    #print(f'vector[aux+1]: {vector[aux+1]}')
                    aux1 = vector[aux]
                    aux2 = vector[aux+1][2:]
                    #print(f'Multipplicacion aux1: {aux1}; aux2: {aux2}')
                    aux1 = float(aux1)
                    aux2 = float(aux2)
                    if vector[aux+1][0] == '-':
                        aux2 *= -1
                    restemp = aux1 * aux2
                    resultado += restemp
                    aux += 1
            elif '/' in vector[aux+1]:
                #print(f'entrada en / in vector[aux+1]')
                try:
                    if '^' in vector[aux+2]:
                        aux1 = vector[aux+1][2:]
                        aux2 = vector[aux+2][2:]
                        #print(f'Potencia / aux1: {aux1}; aux2: {aux2}')
                        aux1 = float(aux1)
                        aux2 = float(aux2)
                        if vector[aux+1][0] == '-':
                            aux1 *= -1
                        potencia = pow(aux1,aux2)
                        restemp = float(vector[aux])/potencia
                        resultado += restemp
                        aux += 2
                    else:
                        #print(f'vector[aux]: {vector[aux]}')
                        #print(f'vector[aux+1]: {vector[aux+1]}')
                        aux1 = vector[aux]
                        aux2 = vector[aux+1][2:]
                        #print(f'Multipplicacion aux1: {aux1}; aux2: {aux2}')
                        aux1 = float(aux1)
                        aux2 = float(aux2)
                        if vector[aux+1][0] == '-':
                            aux2 *= -1
                        restemp = aux1 / aux2
                        resultado += restemp
                        aux += 1
                except:
                    #print(f'vector[aux]: {vector[aux]}')
                    #print(f'vector[aux+1]: {vector[aux+1]}')
                    aux1 = vector[aux]
                    aux2 = vector[aux+1][2:]
                    #print(f'Multipplicacion aux1: {aux1}; aux2: {aux2}')
                    aux1 = float(aux1)
                    aux2 = float(aux2)
                    if vector[aux+1][0] == '-':
                        aux2 *= -1
                    restemp = aux1 / aux2
                    resultado += restemp
                    aux += 1
            else:
                restemp = float(vector[aux])
                resultado += restemp
        except:
            try:
                restemp = float(vector[aux])
                resultado += restemp
            except:pass
        #print(f'Resultado de {vector[aux]}: {restemp}')
        #print(f'Resultado de la suma despues de {vector[aux]}: {resultado}')
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
            #print(f'Suma en potencias')
            #print(f'Vector {vector} separado en potencias: {vector[i]}')
            vector[i] = sumaVector(vector[i])
            #print(f'Resultado de vector[i] en potencias: {vector[i]}')
    return vector

def calculos(texto):
    #print(texto)
    cantidades = separacionSumaResta(texto)
    vector = separacionVector(texto,cantidades)
    #print(f'Vector separado: {vector}')
    vector = separarCorchetes(vector)
    #print(f'Vector separado de corchetes: {vector}')
    vector = separacionParentesis(vector)
    #print(f'Vector separado de parentesis: {vector}')
    for i in range(len(vector)):
        vector[i] = vector[i].replace('^+*','^')
        
    vector = solucionPotencias(vector)
    #print(vector)
    #print('----------------------------------')
    suma = sumaVector(vector)
    #print(suma)
    return suma

def main(texto = '(1)^4-3{-(1)+5}^2-2'):
    texto = texto.replace(' ','')
    texto = texto.replace('*','+*')
    texto = texto.replace('/','+/')
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
#2x-3x^2+4
#4x^3+4^2-5x
#x^4-3(-x+5)^2-2
#x^4-3/(-x+5)^2-2
#(1)^4-3(-(1)+5)^2-2
#1+5-3(8+1-4)+1-4
