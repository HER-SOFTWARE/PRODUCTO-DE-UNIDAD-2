
#--------- LIBRERIAS ------------------------------------------------------------------------

import numpy as np

import board    # Esta libreria sirve para asignar constantes fijas a los pines
                # del tablero, esto hace que usar el módulo de la placa sea
                # más seguro y confiable 
                
import digitalio   # Este módulo sirve utilizar la pantalla LCD con una
                   # retroalimentación de un solo color, en el caso que se
                   # desee una retroalimentación RGB (varios colores) se debe
                   # definir los pines de salida según su ubicación en el board 
                   # y el color 

import adafruit_character_lcd.character_lcd as characterlcd
            # Este módulo permite escribir fácilmente el código de Python que
            # que controla una LCD de caracteres (ya sea con luz de fondo
            # individual o con luz de fondo RGB)


#------ TAMAÑO DE LA PANTALLA LCD --------
            
lcd_columns = 16   # Estas líneas de código definen el tamaño de caracteres de
lcd_rows = 2       # nuestra LCD, en este caso la pnatalla LCD es de 16 columas
                   # y 2 filas, si se tiene una LCD de caracteres de diferente
                   # tamaño se debe modificar estos valores
                   
#---- ASIGNACIÓN DE LOS PINES DE CONFIGURACIÓN DE LA RASPBERRY PI Y LCD --------                  
                   
#Según la ubicación en la placa :           -LCD-   -RASPBERRY PI 3-MODELO B-                
lcd_rs = digitalio.DigitalInOut(board.D22) # pin 4          pin 15    
lcd_en = digitalio.DigitalInOut(board.D17) # pin 6          pin 11                                                                                      
lcd_d4 = digitalio.DigitalInOut(board.D25) # pin 11         pin 22
lcd_d5 = digitalio.DigitalInOut(board.D24) # pin 12         pin 18
lcd_d6 = digitalio.DigitalInOut(board.D23) # pin 13         pin 16
lcd_d7 = digitalio.DigitalInOut(board.D18) # pin 14         pin 12
 
 
# INICIALIZAMOS LA CLASE LCD

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

# Esta línea de código especifica el tipo de retroalimentación de la pantalla
# reconociendo la función de cada pin de la LCD, la retroalimentacion
# es de un solo color, esto queda especificado en el argumento "Mono", para varios
# colores el argumento sería "RGB"


#--------- CLASES --------------------------------------------------------------------------

class menu:

    saludo="\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>> BIENVENIDO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    margenInf=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    advertencia="                !! NO SE ACEPTAN MONEDAS DE 1 ctvs !! \n"



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
        return listaProducto

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
                lcd.clear()
                lcd.message = "Ingrese el \n dinero:" 
                monedaIn = int(input("\nIngrese el dinero: "))
                
                if opcionP==1:
                    if monedaIn % 5 == 0 and monedaIn == costo1:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:" 
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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo1:

                        cambio = monedaIn - costo1
                        print("\n Su cambio es: ", cambio,"ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")


                elif opcionP==2 or opcionP==6 or opcionP==9 or opcionP==10 :
                    if monedaIn % 5 == 0 and monedaIn == costo2:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo2:

                        cambio = monedaIn - costo2
                        print("\n Su cambio es: ", cambio, "ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")



                elif opcionP==3 or opcionP==8 or opcionP==11:
                    if monedaIn % 5 == 0 and monedaIn == costo3:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo3:

                        cambio = monedaIn - costo3
                        print("\n Su cambio es: ", cambio, "ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")



                elif opcionP==4 or opcionP==7:
                    if monedaIn % 5 == 0 and monedaIn == costo4:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo4:

                        cambio = monedaIn - costo4
                        print("\n Su cambio es: ", cambio, "ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")



                elif opcionP==5:
                    if monedaIn % 5 == 0 and monedaIn == costo5:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")
                        

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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo5:

                        cambio = monedaIn - costo5
                        print("\n Su cambio es: ", cambio, "ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")


                elif opcionP==12:
                    if monedaIn % 5 == 0 and monedaIn == costo6:
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
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

                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")

                    elif monedaIn % 5 == 0 and monedaIn > costo6:

                        cambio = monedaIn - costo6
                        print("\n Su cambio es: ", cambio, "ctvs")
                        lcd.clear()
                        lcd.message = "Retire su \nproducto:"
                        print("\n------------- Retire su producto --------------\n ")


            else:
                print("\nOpcion incorrecta \n\n")

            print("\n\nDigite '0' para realizar una nueva compra o digite '1' para salir\n ")
            descision1=int(input())
            
        pass

#-------------------------------------VOID---------------------------------------------------

#------ OBJETOS  ----------------------

#------ ENCABEZADO --------
producto=menu
print(producto.saludo)
lcd.message = ">> BIENVENIDO <<" 
print(producto.matrizProducto())
print(producto.margenInf)
print(producto.advertencia)

#------ EJECUCION ---------
instruccion=operacion
print(instruccion.ingresoOpc())
print(instruccion.gracias)
lcd.clear()
lcd.message = "!! GRACIAS POR \nSU COMPRA !!"
