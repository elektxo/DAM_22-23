tiempo = input("Introduce una contidad de tiempo: ")
tiempo_aux = tiempo
if tiempo.isdigit():
    tiempo = int(tiempo)

    if tiempo>60:
        print("Segundos:", tiempo%60)
        tiempo = tiempo // 60
        if tiempo>60:
            print("Minutos:", tiempo%60)
            tiempo = tiempo // 60
            if tiempo>24:
                print("Horas:", tiempo%24)
                tiempo = tiempo // 24
                if tiempo>30:
                    print("Dias:", tiempo%30)
                    tiempo = tiempo // 30
                    if tiempo>12:
                        print("Meses:", tiempo%12)
                        tiempo = tiempo // 12
                        print("Años:", tiempo)
                    else:
                        print("Meses:", tiempo)
                else:
                    print("Dias:", tiempo)
                
            else:
                print("Horas:", tiempo)
                
        else:
            print("Minutos:", tiempo)

    else:
        print("Segundos:", tiempo)
else:
    print("Aprende a escribir numeros maquina.")