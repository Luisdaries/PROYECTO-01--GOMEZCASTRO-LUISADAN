
# Funcion principal de ejecucion
def main():
    Bienvenida()
    presentacion()

# Mensaje de Bienvenida
def Bienvenida():
    mensaje = "██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░\n██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗\n██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║\n██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║\n██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝\n╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░\n"
    return print(mensaje)

# Pantalla de Presentacion
def presentacion():
    print("Hola Bienvenido al CRM de ventas")
    print("1: Iniciar sesion")
    print("2: Registrarse")
    print("3: Salir")
    print("¿Qué deseas hacer?")
    respuesta = input()
    if validar_entrada(respuesta):
        respuesta = int(respuesta)
        
        if respuesta == 1:
            iniciar_sesion()
        elif respuesta == 2:
            registrarse()
        elif respuesta == 3:
            finalizar()
        else:
            limpiar(1)
            print("Opcion incorrecta")
        presentacion()
    else:
        print("Solo se aceptan numeros enteros, vuelvelo a intentar en...")
        espera(5)
        limpiar(1)
        presentacion()

# Imprimir el menu de navegacion
def limpiar(x):
    for i in range(x):
        print(" ")

# Pregunta de continuacion con cada una de las opciones
def continuar(user):
    print("¿Deseas continuar " + user + "?")
    print("1 : Si")
    print("2 : No")
    Respuesta = int(input())

    if Respuesta == 1:
        limpiar(1)
        menu(user)
    elif Respuesta == 2:
        finalizar()
    else:
        limpiar(1)
        print("Opcion incorrectar, intenta nuevamente")
        continuar(user)



# Validacion de solo numeros en los menus de numeros
def validar_entrada(entrada):
    respuesta = 0
    if entrada.isdigit():
        respuesta = True
    else:
        respuesta = False 
    return respuesta

# Funcion pata el inicio de sesion
def iniciar_sesion():
    user = input("Ingresa su nombre de usuario: ")
    password = input("Ingresa su contraseña: ")

    from lifestore_file import lifestore_users
    for users in lifestore_users:
        if users[1] == user.lower():
            if users[3] == password.lower():
                menu(users[1])
            else:
                print("La contraseña es incorrecta, intentalo nuevamente en...")
                espera(5)
                iniciar_sesion()
        else: 
            print("El usuario no existe, por favor resgistrate")
            registrarse()


# Funcion para registrar nuevos usuarios
def registrarse():
    user = input("Ingresa su nombre de usuario: ")
    mail = input("Ingresa su correo: ")
    password = input("Ingresa su contraseña: ")
    confirmar_password = input("Confirma su contraseña: ")
    if validar_pass(password, confirmar_password):
        if validar_usuario(user) == False:
            print("El usuario ya existe, intenta nuevamente en...")
            espera(5)
            registrarse()
        else:
            añadir_usuario(user.lower(),mail.lower(),password.lower())
            menu(user)
        
    else:
        print("Las contraseñas no coinciden intentalo nuevamente")
        registrarse()
        
# Funcion para insertar el añadir un numero usuario
def añadir_usuario(username, mail, password):
    from lifestore_file import lifestore_users
    lifestore_users.append([numero_usuarios,username, mail ,password])
    
def numero_usuarios():
    from lifestore_file import lifestore_users
    usuarios = len(lifestore_users)
    return usuarios
# Funcion para validacion que no exista el usuario a registrar
def validar_usuario(user):
    from lifestore_file import lifestore_users
    
    for users in lifestore_users:
        if users[0] == user:
            return False
        else:
            True

# Imprimir usuarios
def imprimir_usuario(usuario):
    from lifestore_file import lifestore_users
    for users in lifestore_users:
        if users[1] == usuario:
            print("Nombre: "+ users[1])
            print("Email: "+ users[3])
        limpiar(1)
    continuar(users[1])
    
# Validar que las contraseñs coinciden
def validar_pass(x, y):
    respuesta = 0
    if x == y:
        respuesta = True
    else:
        respuesta = False
    return respuesta

# Tiempo de espera
def espera(x):
    import time
    j = x
    for i in range(5):
        print("Tiempo restante : " + str(j))
        j -= 1
        time.sleep(1)

# Finalizar el programa
def finalizar():
    print("¡Hasta luego!")
    print("El programa se terminara....")
    espera(5)
    quit()

# Imprimir menu de opciones
def menu(usuario):
    limpiar(5)
    print("¿Qué deseas hacer "+ usuario)
    print("--------Productos---------")
    print("| 1: Productos más vendidos")
    print("| 2: Productos con mayor búsquedas")
    print("| 3: Productos con menores ventas")
    print("| 4: Productos con menores búsquedas")
    print("--------Reseñas-----------")
    print("| 5: Productos con las mejores reseñas")
    print("| 6: Productos con las peores, reseñas")
    print("--------Contabilidad------------")
    print("| 7: Total de ingresos general")
    print("| 8: Ventas promedio mensuales")
    print("| 9: Meses con más ventas al año")
    print("--------Otros------------")
    print("| 10: Mis datos")
    print("| 11: Salir")

    respuesta = int(input("¿Qué deseas consultar? "))

    if respuesta == 1:
        imprimir_Mayores_Ventas()
        continuar(usuario)
    elif respuesta == 2:
        imprimir_mayores_busquedas()
        continuar(usuario)
    elif respuesta == 3:
        imprimir_menores_busquedas()
        continuar(usuario)
    elif respuesta == 4:
        imprimir_menores_busquedas()
        continuar(usuario)
    elif respuesta == 5:
        imprimir_mejores_reseñas()
        continuar(usuario)
    elif respuesta == 6:
        imprimir_peores_reseñas()
        continuar(usuario)
    elif respuesta == 7:
        imprimir_ingresos()
        continuar(usuario)
    elif respuesta == 8:
        imprimir_ventas_prom()
        continuar(usuario)
    elif respuesta == 9:
        imprimir_meses_con_mas_ventas()
        continuar(usuario)
    elif respuesta ==10:
        limpiar(1)
        imprimir_usuario(usuario)
    elif respuesta == 11:
        limpiar(1)
        finalizar()
    else:
        limpiar()
        print("Opcion incorrecta, intentalo nuevamente.")
        menu(usuario)

# Obtener mayores ventas
def mayores_ventas():
    nombres = []
    mejor_vendidos = []
    from collections import Counter
    from lifestore_file import lifestore_sales, lifestore_products
    for ventas in lifestore_sales:
        mejor_vendidos.append(ventas[1])
    mejor_vendidos = Counter(mejor_vendidos).most_common(5)

# id del producto y despues numero de ventas

    for productos in lifestore_products:
        i = 0
        for datos in mejor_vendidos:
            if productos[0] == datos[0]:
                nombres.insert(i, [datos[0], productos[1], datos[1]])
                i = i + 1
                
    return nombres

# Imprimir meyores ventas
def imprimir_Mayores_Ventas():
    limpiar(1)
    print("Mejores Vendidos")
    for venta in mayores_ventas():
        print("--------------------")
        print(" ID: " + str(venta[0]) + "\n Nombre del Producto: " + str(venta[1]) + "\n Numero de Ventas: " + str(venta[2]))
        print(" \n")

# Obtener productos con mayores busquedas
def mayores_busquedas():
    from lifestore_file import lifestore_searches,lifestore_products
    from collections import Counter
    mejor_buscados = []
    nombres = []
    for ventas in lifestore_searches:
        mejor_buscados.append(ventas[1])
# articulo y despues cantidad de busquedas
    mejor_buscados = Counter(mejor_buscados).most_common(5)
    i = 0
    for productos in lifestore_products:
        for busquedas in mejor_buscados:
            if productos[0] == busquedas[0]:
                nombres.insert(i, [busquedas[0], productos[1],busquedas[1]])
                i += 1
    return nombres
    
def imprimir_mayores_busquedas():
    limpiar(1)
    print("¨Productos con mayor búsquedas")
    for busquedas in mayores_busquedas():
        print("--------------------")
        print(" ID: " + str(busquedas[0]) + "\n Nombre del Producto: " + busquedas[1]+ "\n Numero de busquedas: " + str(busquedas[2]))
        print(" \n")


# Obtener menores ventas
def menores_ventas():
    from operator import itemgetter
    nombres = [] 
    menor_vendidos = []
    from collections import Counter
    from lifestore_file import lifestore_sales, lifestore_products
    for ventas in lifestore_sales:
        menor_vendidos.append(ventas[1])
    menor_vendidos = Counter(menor_vendidos).most_common()
    menor_vendidos = sorted(menor_vendidos, key=itemgetter(0))
# id del producto y despues numero de ventas

    for productos in lifestore_products:
        i = 0
        for datos in menor_vendidos:
            if productos[0] == datos[0]:
                nombres.insert(i, [datos[0], productos[1], datos[1]])
                i = i + 1

    nombres = sorted(nombres, key=itemgetter(2))
    return nombres
# imprimir menores ventas
def imprimir_menores_ventas():
    limpiar(1)
    print("¨Productos con menores ventas")
    i = 1
    
    for ventas in menores_ventas():
        if i == 5:
            break
        print("--------------------")
        print(" ID: " + str(ventas[0]) + "\n Nombre del Producto: " + ventas[1]+ "\n Numero de ventas: " + str(ventas[2]))
        print(" \n")
        i += 1



# Obtener menores busquedas
def menores_busquedas():
    
    from lifestore_file import lifestore_searches,lifestore_products
    from collections import Counter
    from operator import itemgetter
    nombres = [] 
    menor_busqueda = []
    for ventas in lifestore_searches:
        menor_busqueda.append(ventas[1])
    menor_busqueda = Counter(menor_busqueda).most_common()
    menor_busqueda = sorted(menor_busqueda, key=itemgetter(1))
# id del producto y despues numero de ventas

    for productos in lifestore_products:
        i = 0
        for datos in menor_busqueda:
            if productos[0] == datos[0]:
                nombres.insert(i, [datos[0], productos[1], datos[1]])
                i = i + 1

    nombres = sorted(nombres, key=itemgetter(2))
    return nombres

# imprimir menores busquedas
def imprimir_menores_busquedas():
    limpiar(1)
    print("¨Productos con menores busquedas")
    i = 1
    
    for ventas in menores_busquedas():
        if i == 5:
            break
        print("--------------------")
        print(" ID: " + str(ventas[0]) + "\n Nombre del Producto: " + ventas[1]+ "\n Numero de busquedas: " + str(ventas[2]))
        print(" \n")
        i += 1

def mejores_reseñas():
    from lifestore_file import lifestore_sales, lifestore_products
    from operator import itemgetter
    sumas = []
    i = 1
    total = 0
    for productos in lifestore_products:
        for reseñas in lifestore_sales:
            if reseñas[1] == productos[0]:
                total = total + reseñas[2]
        # producto, reseña en puntos acumuilado y nombre del producto
        sumas.insert(i,[productos[0],total,productos[1]])
        total = 0

    sumas = sorted(sumas, key=itemgetter(1), reverse=True)
    return sumas

# imprimir mejores reseñas
def imprimir_mejores_reseñas():
    
    limpiar(1)
    print("¨Productos con mejores reseñas")
    i = 1
    
    for ventas in mejores_reseñas():
        if i == 5:
            break
        print("--------------------")
        print(" ID: " + str(ventas[0]) + "\n Nombre del Producto: " + ventas[2]+ "\n Numero de reseñas: " + str(ventas[1]))
        print(" \n")
        i += 1



def peores_reseñas():
    from lifestore_file import lifestore_sales, lifestore_products
    from operator import itemgetter
    sumas = []
    nombres= []
    
    i= 0
    total = 0
    for reseñas in lifestore_sales:
            if reseñas[4] == True:
                total = total + reseñas[2]
                # id venta, id del producto y total de reseña en punto
                sumas.insert(i,[reseñas[0],reseñas[1],total])
            total = 0
            
    i = 0

    for productos in lifestore_products:
        for datos in sumas:
            if productos[0] == datos[1]:
                # id el producto con peor reseña, nombre y puntos de reseña
                nombres.insert(i, [datos[0], productos[1], datos[2]])
            i = i + 1
                
        
    nombres = sorted(nombres, key=itemgetter(1))
    return nombres

# imprimir mejores reseñas
def imprimir_peores_reseñas():
    
    limpiar(1)
    print("¨Productos con mejores reseñas")
    i = 1
    
    for ventas in peores_reseñas():
        if i == 5:
            break
        print("--------------------")
        print(" ID: " + str(ventas[0]) + "\n Nombre del Producto: " + ventas[1]+ "\n Numero de reseñas: " + str(ventas[2]))
        print(" \n")
        i += 1

def total_ingresos():
    from lifestore_file import lifestore_sales, lifestore_products
    total = 0
    cantidad_ventas = 0
    for productos in lifestore_products:
        for ventas in lifestore_sales:
            if ventas[4] == 0:
                if ventas[1] == productos[0]:
                    cantidad_ventas = cantidad_ventas + 1
                    total = total + productos[2]
        # producto, reseña en puntos acumuilado y nombre del producto
    
    resultado = ("Ventas totales: " + str(cantidad_ventas) + "\n"+ "Ingresos totales: " + str(total))
    return resultado

def imprimir_ingresos():
    limpiar(1)
    print("Ingresos totales")
    print("--------------------")
    print(total_ingresos())

def ventas_promedio_mes():
    from lifestore_file import lifestore_sales, lifestore_products
    from collections import Counter
    
    solo_mese = []
    
    for ventas in lifestore_sales:
        meses = ventas[3].split("/")
        solo_mese.append(meses[1])
    
    ventas_por_mes = Counter(solo_mese).most_common()

    return ventas_por_mes
    
def imprimir_ventas_prom():
    promedio = 0
    print("Ventas promedio")
    for i in ventas_promedio_mes():
        promedio = promedio + i[1]
        if i[0] == "01":
            print("Ventas de Enero: " + str(i[1]))
        if i[0] == "02":
            print("Ventas de Febrero: " + str(i[1]))
        if i[0] == "03":
            print("Ventas de Marzo: " + str(i[1]))
        if i[0] == "04":
            print("Ventas de Abril: " + str(i[1]))
        if i[0] == "05":
            print("Ventas de Mayo: " + str(i[1]))
        if i[0] == "06":
            print("Ventas de Junio: " + str(i[1]))
        if i[0] == "07":
            print("Ventas de Julio: " + str(i[1]))
        if i[0] == "08":
            print("Ventas de Agosto: " + str(i[1]))
        if i[0] == "09":
            print("Ventas de Septiembre: " + str(i[1]))
        if i[0] == "10":
            print("Ventas de Octubre: " + str(i[1]))
        if i[0] == "11":
            print("Ventas de Noviembre: " + str(i[1]))
        if i[0] == "12":
            print("Ventas de Diciembre: " + str(i[1]))
    print("Promedio por mes : "+ str(int(promedio/12)))
    
    

    
def meses_mayor_ventas():
    from lifestore_file import lifestore_sales, lifestore_products
    from collections import Counter
    from operator import itemgetter
    
    
    solo_mese = []
    
    for ventas in lifestore_sales:
        meses = ventas[3].split("/")
        solo_mese.append(meses[1])
    
    ventas_por_mes = Counter(solo_mese).most_common(5)
    sorted(ventas_por_mes, key=itemgetter(1))
    return ventas_por_mes

def imprimir_meses_con_mas_ventas():
    for i in meses_mayor_ventas():
        if i[0] == "01":
            print("Ventas de Enero: " + str(i[1]))
        if i[0] == "02":
            print("Ventas de Febrero: " + str(i[1]))
        if i[0] == "03":
            print("Ventas de Marzo: " + str(i[1]))
        if i[0] == "04":
            print("Ventas de Abril: " + str(i[1]))
        if i[0] == "05":
            print("Ventas de Mayo: " + str(i[1]))
        if i[0] == "06":
            print("Ventas de Junio: " + str(i[1]))
        if i[0] == "07":
            print("Ventas de Julio: " + str(i[1]))
        if i[0] == "08":
            print("Ventas de Agosto: " + str(i[1]))
        if i[0] == "09":
            print("Ventas de Septiembre: " + str(i[1]))
        if i[0] == "10":
            print("Ventas de Octubre: " + str(i[1]))
        if i[0] == "11":
            print("Ventas de Noviembre: " + str(i[1]))
        if i[0] == "12":
            print("Ventas de Diciembre: " + str(i[1]))
# ejecucion
main()