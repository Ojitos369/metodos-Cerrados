from math import pow
from src.extras import limpiar
from src.operaciones import main as operaciones
import os
os.system('clear')
no_decimales = 5
""" def funcion(xr):
    # x^4-3x^2-2
    a = math.pow(xr,4)
    b = 3*(math.pow(xr,3))
    res = a + b -2

    # x^3+2^2-10x-20
    a = pow(xr,3)
    b = 2*(pow(xr,2))
    c = 10 * xr
    res = a+b-c-20

    # 3x^2+4x-10
    a = 3*(pow(xr,2))
    b = 4*xr
    res = a-b-10
    res = round(res,no_decimales)
    return res

def derivada(xr):
    # x^4-3x^2-2
    a = math.pow(xr,4)
    b = 3*(math.pow(xr,3))
    res = a + b -2

    # x^3+2^2-10x-20
    a = pow(xr,3)
    b = 2*(pow(xr,2))
    c = 10 * xr
    res = a+b-c-20

    # 3x^2+4x-10
    a = 3*(pow(xr,2))
    b = 4*xr
    res = a-b-10
    res = round(res,no_decimales)
    return res """

def bifurcacion(ax,bx,veces,operacion, no_decimales):
    opc = 1
    limpiar()
    print(f'Funcion {operacion} por bifurcacion')
    print('------------------------------------')
    for i in range(veces):
        
        xr = round(((ax+bx)/2),no_decimales)
        aux = operacion.replace('(','{')
        aux = aux.replace(')','}')
        sustitucion = aux.replace('x',f'({xr})')
        res = round(operaciones(sustitucion),no_decimales)
        print(f'{i+1}.- ax\tbx\txr\tresultado')
        print(f'{i+1}.- {ax}\t{bx}\t{xr}\t{res}')
        print()
        if opc == 1:
            if res < 0:
                ax = xr
            elif res > 0:
                bx = xr
            else:
                print(f'Final: ax\tbx\txr\tresultado')
                print(f'Final: {ax}\t{bx}\t{xr}\t{res}')
                break
        elif opc == 2:
            if res > 0:
                bx = xr
            elif res < 0:
                ax = xr
            else:
                print(f'Final: ax\tbx\txr\tresultado')
                print(f'Final: {ax}\t{bx}\t{xr}\t{res}')
                break
""" def raphson(x,n):
    func = funcion(x)
    deriv = derivada(x)
    if deriv != 0 and n > 0 and func!=0:
        x2 = round(x-(func/deriv),no_decimales)
        print(f'x={x}; funcion={func}')
        raphson(x2,n-1)
    elif deriv == 0:
        print('Derivada da 0')
    elif n == 0:
        print('Termino') """
