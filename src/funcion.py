from math import pow
from src.extras import limpiar
from src.operaciones import main as operaciones

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

def raphson(funcion,derivada,veces,no_decimales,inicial, n=1):
    aux = funcion.replace('(','{')
    aux = aux.replace(')','}')
    sustitucion = aux.replace('x',f'({inicial})')
    aux2 = derivada.replace('(','{')
    aux2 = aux2.replace(')','}')
    sustitucion2 = aux2.replace('x',f'({inicial})')
    func = round(operaciones(sustitucion),no_decimales)
    deriv = round(operaciones(sustitucion2),no_decimales)
    if deriv != 0 and veces > 0 and func!=0:
        #print(f'inicial: {inicial}')
        #print(f'func: {func}')
        #print(f'deriv: {deriv}')
        resultado = round(inicial-(func/deriv),no_decimales)
        #print(f'resultado: {resultado}')
        print(f'{n}: x={inicial}; funcion={func}')
        raphson(funcion,derivada,veces-1,no_decimales,resultado,n+1)
    elif deriv == 0:
        print('Derivada da 0')
    elif veces == 0:
        print('Termino')
