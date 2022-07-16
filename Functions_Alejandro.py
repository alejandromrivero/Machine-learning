

def contador_positivos(x):#cuenta los numeros positivos en una determinada serie
    countp=0
    for row in x:
        if row>0:
            countp+=1
        else:
            countp+=0
    return countp

def contador_positivosprinting(x):
    countp=0
    for row in x:
        if row>0:
            countp+=1
            print(row,' positivo')
        else:
            print(row,' negativo')
            countp+=0
    return countp

def contador_negativos(x):#cuenta los numeros negativos en una determinada serie.
    countn = 0
    for row in x:
        if row < 0:
            countn += 1
        else:
            countn += 0
    return countn

format=lambda x: '%.2f' %x #funcion anonima para formatear los numeros a dos lugares decimales.


