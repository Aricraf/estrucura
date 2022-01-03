#ejercicios de estructura de datos del 1 al 10
#Tipos de datos y acciones elementales


from typing import Match


opcion=0
def menu():
    opc= int(input("MENU PRINCIPAL \n " +
                   "1.- OPERACIONES MATEMATIAS BASICAS \n " +
                   "2.- CALCULO DE LA RESOLVENTE \n " +
                   "3.- CALCULAR LA HIPOTENUZA \n " +
                   "4.- PAR O IMPAR \n " +
                   "5.- NUMERO BINARIO A BIT \n " +
                   "6.- NUMERO BINARIO \n " +
                   "7.- SEPARACION DE NUMEROS \n " +
                   "ELIJA UNA OPCION: "))
    return opc
while opcion !=7:
    opcion = menu ()
    if opcion==1 :
        #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.
       print(" INGRESE DOS NUMEROS PARA REALIZAR LAS OPERACIONES MATEMTICAS")
       numero1=int(input("INGRESE EL PRIMER NUMERO:   "  ))
       numero2= int(input("INGRESE EL SEGUNDO NUMERO:   "  ))
       resultado= numero1 + numero2
       resultado1= numero1 - numero2
       resultado2= numero1 * numero2
       resultado3= numero1 // numero2
       resultado4= numero1 % numero2
       print("EL RESULTADO DE LA SUMA DE LOS DOS NUMEROS ES.." + str(resultado))
       print("EL RESULTADO DE LA RESTA DE LOS DOS NUMEROS ES.." + str(resultado1))
       print("EL RESULTADO DE LA MULTIPLICASION DE LOS DOS NUMEROS ES.." + str(resultado2))
       print("EL RESULTADO DE LA DIVISION DE LOS DOS NUMEROS ES.." + str(resultado3))
       print("EL RESULTADO DEL MODULO DE LOS DOS NUMEROS ES.." + str(resultado4)) 
    elif opcion==2 :
        #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
        print("INGRESE TRES VALORES")
        n1= int(input("INGRESE EL VALOR DE A:  "))
        n2= int(input("INGRESE EL VALOR DE B:  "))
        n3= int(input("INGRESE EL VALOR DE C:  "))
        o1= (n2*n2)
        o2=  n1*n3
        p1= 4 - o2
        o3=2*n1
        o4=o1 -p1
        o5= n2 + o4
        o6= o5/o3
        o7= n2 ** +o4
        o8= n2 ** -o4
        o9=o7/o3
        ob= o8/o3
        print(" EÑ RESULTADO POSITIVO DE LA OPERACION  ES  " + str(o9) )
        print(" EÑ RESULTADO NEGATIVO DE LA OPERACION  ES  " + str(ob) )
    elif opcion==3 :
        import math 
        #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
        print("INGRESE DOS VALORES ")    
        ancho= int(input("ingrese el cateto 1:   "))
        alto= int(input("ingrese el catetp 2:   "))
        hipotenusa= math.sqrt(ancho**2 + alto**2)
        print("LA HIPOTENUSA  ES :  " + str(hipotenusa))
    elif opcion==4 :
        #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
        pritn(" 0 ES PAR Y 1 ES IMPAR ")
        numero1=int(input("INGRESE UN NUMERO  "))
        if numero1%2==0:
            print("00000000000000000000000000000000000000000000000000000000000000000000 ")
        else:
            print("11111111111111111111111111111111111111111111111111111111111111111111 ")
    elif  opcion==5 :    
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit
        #de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
        num= int(input("INGRESE UN NUMERO "))
        if num==0:
           re=num//2
           print("EL BIT DE PARIDAD ES : ", str(re))
        else:
            re=num//2-1 
            print("EL BIT DE PARIDAD ES ", str(re) )
    elif  opcion ==6 :     
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor
        numero=int(input("INGRESE UN NUMERO "))
        print("EL VALOR  INGRESADO FUE " + numero)        
    elif opcion ==7 :   
        #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
        #decenas, centenas y unidades de mil.
        #Entrada: 1234
        # salida:
        # Unidades: 4
        # decena:3
        # Centenas: 2
        # Unidades de mil: 1
        numero1= int(input("INGRESE UN NUMERO "))
        n= str(numero1)
        print(" ANALISANDO EL NUMERO {} ". format(numero1))
        print("UNIDAD:         {}" . format(n[3]))
        print("DECENA:         {}" . format(n[2]))
        print("CENTENA:        {}" . format(n[1]))
        print("UNIDAD DE MIL:  {}" . format(n[0]))
    

            