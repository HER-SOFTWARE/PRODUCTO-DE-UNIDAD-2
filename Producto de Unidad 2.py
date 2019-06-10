
#--------- LIBRERIAS ------------------------------------------------------------------------

import numpy as np # Esta libreria permite realizar arreglos bidimensionales o
                   # matrices sin necesidad de utilizar ciclos de repetición
                   # para su impresión


#--------- CLASES --------------------------------------------------------------------------

class menu: # En esta clase se va ha estructurar la matriz de productos o lista de productos
            # que indica al usuario las opciones que puede elegir

    #-----Atributos------------
    # Los atributos definidos en la clase menu sirven para estructurar el encabezado
    # que es una guía visual para el usuario
    saludo="\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BIENVENIDO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    margenInf=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    advertencia="                !! NO SE ACEPTAN MONEDAS DE 1 ctvs !! \n"

    # -----Metodos----------------
    # Este metodo contiene todas las opciones de productos que puede elegir el usuario
    def matrizProducto():
        listaProducto = np.array(
            [["'''''''''''''''", "'''''''''''''''''", "''''''''''''''''", "''''''''''''"],
             [" 1. Festival   ", " 2.  Oreo        ", " 3. Nestle      ", " 4. Ricas   "],
             ["  40 ctvs      ", "  50 ctvs        ", "  35 ctvs       ", "  45 ctvs   "],
             ["'''''''''''''''", "'''''''''''''''''", "''''''''''''''''", "''''''''''''"],
             [" 5.  Kit Kat   ", " 6.  Galak       ", " 7. Manicho     ", " 8. Snickers"],
             ["  75 ctvs      ", "  50 ctvs        ", "  45 ctvs       ", "   35 ctvs  "],
             ["'''''''''''''''", "'''''''''''''''''", "''''''''''''''''", "''''''''''''"],
             [" 9. Doritos    ", " 10. Rufles      ", " 11. Kchitos    ", "12. DeTodito"],
             ["   50 ctvs     ", "  50 ctvs        ", "   35 ctvs      ", "   70 ctvs  "],
             ["'''''''''''''''", "'''''''''''''''''", "''''''''''''''''", "''''''''''''"]])
        return listaProducto    #El retorno nos sirve para guardar en una variable la
                                # matriz listaProducto y posteriormente invocarla en el
                                # void o cuerpo


class operacion:

    gracias=" \n         !!! GRACIAS POR SU COMPRA !!!"

    def ingresoOpc():
        descision1 = 0
        while descision1 == 0:
            print("\nDigite el numero del producto deseado: ")
            opcionP = int(input())

            costo1 = 40
            costo2 = 50
            costo3 = 35
            costo4 = 45
            costo5 = 75
            costo6 = 70


            if opcionP > 0 and opcionP <= 12:

                monedaIn = int(input("\nIngrese el dinero: "))

                if opcionP==1:
                    if monedaIn % 5 == 0 and monedaIn == costo1:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 40 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo1:

                        valorT = 0
                        cond = 40 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn


                            if monedaIn % 5 == 0 and  costoIng> costo1:
                                cambio = costoIng - costo1
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo1:

                        cambio = monedaIn - costo1
                        print("\n Su cambio es: ", cambio,"ctvs")
                        print("\n------------- Retire su producto --------------\n ")


                elif opcionP==2 or opcionP==6 or opcionP==9 or opcionP==10 :
                    if monedaIn % 5 == 0 and monedaIn == costo2:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 50 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo2:

                        valorT = 0
                        cond = 50 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn


                            if monedaIn % 5 == 0 and costoIng > costo2:
                                cambio = costoIng - costo2
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo2:

                        cambio = monedaIn - costo2
                        print("\n Su cambio es: ", cambio, "ctvs")
                        print("\n------------- Retire su producto --------------\n ")



                elif opcionP==3 or opcionP==8 or opcionP==11:
                    if monedaIn % 5 == 0 and monedaIn == costo3:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 35 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo3:

                        valorT = 0
                        cond = 35 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn


                            if monedaIn % 5 == 0 and costoIng > costo3:
                                cambio = costoIng - costo3
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo3:

                        cambio = monedaIn - costo3
                        print("\n Su cambio es: ", cambio, "ctvs")
                        print("\n------------- Retire su producto --------------\n ")



                elif opcionP==4 or opcionP==7:
                    if monedaIn % 5 == 0 and monedaIn == costo4:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 45 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo4:

                        valorT = 0
                        cond = 45 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn


                            if monedaIn % 5 == 0 and costoIng > costo4:
                                cambio = costoIng - costo4
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo4:

                        cambio = monedaIn - costo4
                        print("\n Su cambio es: ", cambio, "ctvs")
                        print("\n------------- Retire su producto --------------\n ")




                elif opcionP==5:
                    if monedaIn % 5 == 0 and monedaIn == costo5:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 75 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo5:

                        valorT = 0
                        cond = 75 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn


                            if monedaIn % 5 == 0 and costoIng > costo5:
                                cambio = costoIng - costo5
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo5:

                        cambio = monedaIn - costo5
                        print("\n Su cambio es: ", cambio, "ctvs")
                        print("\n------------- Retire su producto --------------\n ")


                elif opcionP==12:
                    if monedaIn % 5 == 0 and monedaIn == costo6:
                        print("\n------------- Retire su producto --------------\n ")
                        print("El producto tiene un costo de: 70 ctvs ")

                    elif monedaIn % 5 == 0 and monedaIn < costo6:

                        valorT = 0
                        cond = 70 - monedaIn
                        while valorT < cond:
                            monedaIn2 = int(input("\nPor favor ingrese el valor restante: "))
                            valorT = valorT + monedaIn2
                            costoIng = valorT + monedaIn

                            if monedaIn % 5 == 0 and costoIng > costo6:
                                cambio = costoIng - costo6
                                print("\n Valor ingresado es: ", costoIng, "ctvs")
                                print("\n Su cambio es: ", cambio, "ctvs")

                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo6:

                        cambio = monedaIn - costo6
                        print("\n Su cambio es: ", cambio, "ctvs")
                        print("\n------------- Retire su producto --------------\n ")


            else:
                print("\nOpcion incorrecta \n\n")

            print("\n\nDigite '0' para realizar una nueva compra o digite '1' para salir\n ")
            descision1 = int(input())



        pass

#-------------------------------------VOID---------------------------------------------------

#------ OBJETOS  ----------------------
#Los objetos se utilizan para invocar a las funciones , métodos, atributos
# e imprimir los procesos efectuados en cada clase segun corresponda

#------ ENCABEZADO --------
producto=menu
print(producto.saludo)
print(producto.matrizProducto())
print(producto.margenInf)
print(producto.advertencia)


#------ EJECUCION ---------
instruccion=operacion
print(instruccion.ingresoOpc())
print(instruccion.gracias)
