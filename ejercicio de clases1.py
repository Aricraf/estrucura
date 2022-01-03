#Estructuras De Control de Flujo de Datos
opcion=0
def menu():
    opc= int(input("MENU PRINCIPAL \n " +
                   "1.-  AÑO BISIESTO  \n " +
                   "2.-  NUMERO CAPICUA \n " +
                   "3.-  HORAS A SEGUNDOS  \n " +
                   "4.- sSEGUNDOS A DIAS HORAS Y MINUTOS \n " +
                   "5.-  NUMERO MAYOR  \n " +
                   "6.-  VALOR A PAGAR DE UN ESTACIONAMIENTO  \n " +
                   "7.-  CALCULO DEL IMC \n" +
                   "8.-  CALCULO DE FECHA DEL AÑO 2014 \n " +
                   "9.-  MESES DEL AÑO \n " +
                   "10.- MONTO A PAGAR \n " + 
                   "11.- CALCULO DE ENTERO \n " +
                   "12.- CALCULO DE CAPICUA DE TRES CIFRAS \n " + 
                   "13.- NUMERO PRIMO \N " + 
                   "ELIJA UNA OPCION:\n "))
    return opc
while opcion !=7:
    opcion = menu ()
    if opcion==1 :
        # Todos los años que se dividen exactamente entre 400, o que son divisibles
        # exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
        # Usando estas premisas crea un algoritmo que lea una fecha como un número
        # entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
        # el mismo es un año bisiesto o no.
        añio=int(input("INGRESE AÑO  "))
        if añio%4==0:
            print("EL AÑIO QUE INGRESO " + str(añio) + " ES BISIESTO")
        else:
            print("EL AÑO QUE INGRESO " + str(añio) + " NO BISIESTO")   
    elif opcion ==2:
        #Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
        # Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
        numero1= int(input("INGRESE UN NUMERO "))
        digito1= numero1 // 10000
        digito2= (numero1 // 1000 ) % 10 
        digito3= (numero1 // 100) % 10
        digito4= (numero1 //10) % 10
        digito5= (numero1 %10) 
        if digito1 == digito5 and digito2 == digito4:
            print(" EL NUMERO " + str(numero1 ) + " ES CAPICUAL")
        else:
            print(" EL NUMERO " + str(numero1 ) + " NO ES CAPICUAL")    
    elif opcion==3:
        #Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
        #resultado su equivalente en segundos.
        horas= int(input("INGRESE LA CANTIDAD DE HORAS HORAS  "  )) 
        minutos= int(input("INGRESE LA CANTIDAD DE MINUTOS   " ))
        if minutos <=59:
             h1= horas * 60 
             m1= minutos * 60 
             suma= h1 + m1
             segundos= suma * 60 
             print(" EL RESULTADO DE LOS EN SEGUNDOS ES " + str(segundos))
        else:
            print("INGRESE EL VALOR DE LOS MINUTOS ")    
    elif opcion==4 :
        # Para un valor entero positivo que representa una cantidad en segundos, indicar
        # su equivalente en minutos, horas y días.
        segundos= int(input(" INGRESE LA CANTIDAD DE SEGUNDOS  "))
        dia= segundos / ( 24 * 60 * 60 )
        segundos = segundos % (24 * 60 *60) 
        horas = segundos % (60 * 60)
        segundos = segundos % (60 * 60)
        minutos= segundos // 60
        segundos= segundos % 60
        print("DIAS: {}  \n HORAS {} \n MINUTOS {}".fortmat(dia,horas,minutos))
    elif opcion==5:
        #  Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
        #  mayor? y ¿cuál es el segundo mayor
        n1= int(input("INGRESE EL PRIMER NUMERO  "))
        n2=int(input("INGRESE EL SEGUNDO NUMERO  "))
        n3= int(input("INGRESE EL TERCER NUMERO  "))
        if n2 < n1 > n3:
            print(" EL NUMERO MAYOR ES EL PRIMER NUMEROB" + str(n1 ))
        elif n1 < n2 > n3 :
            print(" EL NUMERO YAYOR ES EL SEGUNDO NUMERO " + str(n2))
        elif n1 < n3 > n2 :
            print("EL NUMERO MAYOT ES EL TERCER NUMERO " + str(n3))
        else:
            print( " TODOS LOS NUMEROS SON IGUALES ")
    elif opcion ==6:
        # En un estacionamiento el monto a pagar se calcula multiplicando el número de
        # horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
        # incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
        # Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
        # y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
        # calcule el monto a pagar por el dueño del vehículo.
        # La entrada vendrá dada por dos enteros positivos el primero representa las horas
        # y el segundo los minutos, además por último se debe leer un carácter (A o P) que
        # indica si la hora es AM o PM.
        hora=int(input("INGRESE LA HORA DE ENTRADA  "))
        hora1=int(input("INGRESE LA HORA DE SALIDA  "))
        
    elif opcion==7:
        #El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
        # cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
        # del peso de una persona en relación con su altura.
        # Clasificación del IMC de acuerdo con la OMS de la ONU:
        # a. Menor a 16: Criterio de ingreso.
        # b. 16 a 16.9: infra peso.
        # c. 17 a 18.4: bajo peso.
        # d. 18.5 a 24.9: peso normal.
        # e. 25 a 29.9: sobrepeso.
        # f. 30 a 34.9: obesidad pre-mórbida.
        # g. 40 a 45: obesidad mórbida.
        # h. Mayor a 45: obesidad híper-mórbida.
        # Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
        # centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
        # de IMC de la persona y la categoría en la cual fue clasificado.
        masa=int(input("INGRESE SU PESO EN LIBRAS "))
        estatura=int(input("INGRESE SU ESTATURA CENTIMETROS  "))    
        peso= masa *  0.453591 
        imc= peso /estatura
        if imc > 45 :
            print("SU IMC ES " + str(imc) + "POR ENDE USTED SUBRE DE OBECIDAD HIPER-MORBIDA")
        elif  imc <=45 and  (imc>=40):
            print("SU IMC ES " + str(imc) + " POR ENDE USTED TIENE OBESIDAD-MORBIDA ")
        elif  imc <= 35 and imc >= 30:
            print("SE IMC ES " + str(imc) + "POR ENDE USTED TIENE PRE-MORBIDA " )
        elif imc  <=29 and imc  >=25:
            print("SU IM CES " + str(imc) + "POR ENDE USTED TIENE  SOBREPESO ")   
        elif imc <=25 and imc  >=18:
            print("SU IMC ES " + str(imc) + "POR ENDE USTED TIENE PESO NORMAL ")
        elif imc == 17:
            print("SU IMC ES " + str(imc) + "POR ENDE USTED TIENE PESO BAJO  ")
        elif imc ==19:
            print("SU IMC ES " + str(imc) + "POR ENDE USTED TIENE INFRA PESO ")
    elif opcion==8:
        #Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
        # 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
        # Enero de 2014 hasta la fecha dada
        dia=int(input("INGRESE DIA     "))
        mes=int(input("INGRESE EL MES  "))
        enero=1
        fbrero=2  
        mazo=3 
        abril=4
        mayo=5
        jumio=6
        julio=7
        agosto=8
        septiembre=9
        octubre=10
        noviembre=11
        diciembre=12
        resolucion=1
    elif opcion == 9:
       # Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho número.
       
        mes=int(input("INGRESE UN VALOR DEL 1 AL 12 \n  "))        
        if mes==1:
            print("ENERO ")
        elif mes ==2:
            print("FEBRERO")
        elif mes ==3:
            print("MARZO")    
        elif mes ==4:
            print("ABRIL")
        elif mes ==5:
            print("MAYO")        
        elif mes ==6:
            print("JUNIO")
        elif mes ==7:
            print("JULIO")    
        elif mes ==8:
            print("AGOSTO")
        elif mes ==9:
            print("SEPTIEMBRE")
        elif mes ==10:
            print("OCTUBRE")
        elif mes ==11:
            print("NOBIEMBRE")    
        elif mes ==12:
            print("DICIEMBRE")
        elif mes  > 12:
            print("NO EXISTE NINGUN MES CON ESE NUMERO")                   
    elif opcion==10:
        #En un almacén se hace un 20% de descuento a los clientes cuya compra supere
        # los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
        # pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
        # necesario.
        valor= int(input("INGRESE EL VALOR DE SU COMPRA  "))
        if valor  >=1000:
            costo= valor % 20 
            print("EL MONTO A PAGAR AOLICANDOLE EL 20% DE DESCUENTO ES " + str(costo))
        elif valor  < 1000 :
            print(" EL VALOR A PAGAR ES DE " + str(valor) )
            print("NO APLICA DESCUENTO")
    elif opcion == 11:
        #Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene dicho número.
        numero=int(input("INGRESE IN VALOR"))
        
        
        
    elif opcion ==12 : 
        # Dado un número, determine si es capicúa.
        # Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.
        numero= int(input("INGRESE UN NUMERO DE TRE DIJITOS "))
        digito1= (numero1 // 100) % 10
        digito2= (numero1 //10) % 10
        digito3= (numero1 %10) 
        if digito1 == digito3:
            print(" EL NUMERO " + str(numero1 ) + " ES CAPICUAL")
        else:
            print(" EL NUMERO " + str(numero1 ) + " NO ES CAPICUAL")
    elif opcion==13:
       # Dado un número N determinar si es un número primo.
       # Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo
       numero=int(input("INGRESE UN NUMERO"))    
       n1=1
       n2=0
       while n1  < numero:
           if numero % n1 ==0:
               n2=n2 + 1 
               n1 = n1 + 1    
           if n2 == 2:
            print(" es numero primo ") 
           else:
            print("NO ES NUMERO PRIMO ")