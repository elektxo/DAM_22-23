# ejercicio 02 

def obtenerPosicion(palabra, clave):
    return palabra.find(clave)

def obtenerPalabra(palabra, clave):
    caso = obtenerPosicion(palabra, clave)
    if caso == -1:
        a_devolver = caso
    else:
        a_devolver = palabra[:caso] + palabra[caso+len(clave):]
    return a_devolver

def descifraMensaje(mensaje, clave):
    mensaje_cortado = mensaje.split(' ')
    mensaje_final = ''
    for i in mensaje_cortado:
        resultado = obtenerPalabra(i, clave)
        if resultado != -1:
            mensaje_final += resultado + ' '
    return mensaje_final

mensaje = "i wana be feliiwices programar public python iwilos class primavera cuatroiwi cuenca i win .iwi out"

clave = "iwi"

# resultado = obtenerPalabra('feliiwices', clave)

resultado = descifraMensaje(mensaje, clave)

print(resultado)