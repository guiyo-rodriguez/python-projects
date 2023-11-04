
def permutar(N, cadena):
    if N > 0:
        return permutar(N-1, cadena + '1') + permutar(N-1, cadena + '0')
    else:
        return cadena + ' '

def particionar_en_lineas(N, cadena):
    print(cadena.split())
    print(len(cadena.split()))
    cadena_particionada = []
    mensaje = ''
    contador = 1
    for palabra in cadena.split():
        if contador < N:
            #print(palabra)
            cadena_particionada.append(palabra)
            mensaje += palabra + ' '
            contador += 1
        else:
            cadena_particionada.append('\n')
            mensaje += '\n'
            contador = 1
    print(mensaje)
    return cadena_particionada

words = permutar(5, '')
print(particionar_en_lineas(6, words))
print(len(particionar_en_lineas(6, words)))