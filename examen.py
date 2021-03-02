

#ejercicio 1
def descuentosegunelKilo(kilos):
    print(kilos)
    if (kilos >= 0) & (kilos < 2):
        print("Se descuenta el 0%")
    elif (kilos >= 2) & (kilos < 5):
        print("Se descuenta el 10%")
    elif (kilos >= 5) & (kilos < 10):
        print("Se descuenta el 15%")
    elif kilos >= 10:
        print("Se descuenta el 20%")

#ejercico 2
def ultimovalor(neto, clave):
    if clave == "010":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.2)}")
    elif clave == "020":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.4)}")
    elif clave == "030":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.55)}")
    elif clave == "040":
        print(f"El valor final por la compra de abanicos es de: {neto-(neto*0.75)}")

#Punto 3
def Estereos(marca, precio):
    precio_desc = precio
    if precio >= 4000:
        precio_desc = precio_desc - (precio_desc * 0.2)
    total = precio_desc + (precio_desc*0.3)
    if marca == "NOSY":
        total = total - (total*0.1)
    print(f"El monto total que debe pagar el cliente es: {total}")

#Punto 4
def hectareasaReforestar(hectareas):
    if hectareas > 5:
        pino = hectareas*0.8
        oyamel = hectareas*0.15
        cedro = hectareas*0.5
    else:
        pino = hectareas*0.45
        oyamel = hectareas*0.25
        cedro = hectareas*0.3
    print(f"Se sembrarán {pino} hectareas de Pino, {oyamel} hectareas de Oyamel y {cedro} hectareas de cedro")

#Punto 5
def numerosDiferentes(n1, n2, n3):
    if (n1 > n2) & (n1 > n3):
        print(f"El numero mayor es n1: {n1}")
    elif (n2 > n1) & (n2 > n3):
        print(f"El numero mayor es n2: {n2}")
    elif (n3 > n1) & (n3 > n2):
        print(f"El numero mayor es n3: {n3}")
    else:
        print("Los números son iguales")

#Prueba ejercicio 1
descuentosegunelKilo(4)
descuentosegunelKilo(6)
descuentosegunelKilo(8)
descuentosegunelKilo(25)

#Prueba ejercicio 2
ultimovalor(200000,"010")
ultimovalor(300000,"020")
ultimovalor(200000,"030")
ultimovalor(500000,"040")
ultimovalor(500000,"050")

#Prueba ejercicio 3
Estereos("NOSY",10000)
Estereos("CASIO",2000)



