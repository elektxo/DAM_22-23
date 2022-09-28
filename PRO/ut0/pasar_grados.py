escala_origen = input("Introduce una escala de origen[C/F/K]: ")
grados_origen = float(input("Grados de origen: "))

if escala_origen == "C":
    escala_destino = input("Introduce una escala de destino[F/K]: ")
    if escala_destino == "K":
        temperatura_final = grados_origen + 273.15
        print("Son", temperatura_final, "grados kelvin")
    else:
        if escala_destino == "F":
            temperatura_final = grados_origen * 1.8 + 32
            print("Son", temperatura_final, "grados fahrenheit")
        else:
            print("No se introdujo correctamente la escala de destino, vuelva a intentarlo.")
else:
    if escala_origen == "K":
        escala_destino = input("Introduce una escala de destino[F/C]: ")
        if escala_destino == "C":
            temperatura_final = grados_origen - 273.15
            print("Son", temperatura_final, "grados celcius")
        else:
            if escala_destino == "F":
                temperatura_final = (grados_origen - 273.15) * 1.8 +32
                print("Son", temperatura_final, "grados fahrenheit")
            else:
                print("No se introdujo correctamente la escala de destino, vuelva a intentarlo.")
    else:
        if escala_origen == "F":
            escala_destino = input("Introduce una escala de destino[K/C]: ")
            if escala_destino == "C":
                temperatura_final = (grados_origen - 32) / 1.8
                print("Son", temperatura_final, "grados celcius")
            else:
                if escala_destino == "K":
                    temperatura_final = ((grados_origen - 32) / 1.8) + 273.15
                    print("Son", temperatura_final, "grados kelvin")
                else:
                    print("No se introdujo correctamente la escala de destino, vuelva a intentarlo.")
        else:
            print("No se introdujo correctamente la escala, intentelo de nuevo.")