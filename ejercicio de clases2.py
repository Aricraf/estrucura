pcion=0
def menu():
    opc= int(input("MENU PRINCIPAL \n " +
                   "1.-  CALCULO DE LA FUNCION FACTORIAL  \n " +
                   "2.-  INGRESE CONTRASEÑA \n " +
                   "3.-  VALOR MAYOR Y MENOS  \n " +
                   "4.-   \n " +
                   "5.-  TABLA DE MULTIPLICAR \n " +
                   "6.-  FICHAS DE DOMINO   \n " +
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
        #Construya un programa que dado un valor entero N, haga el cálculo de la función
        # factorial utilizando estructuras iterativas.
        n=int(input("INGRESE VALOR  "))
        if n >=0 :
            x=1
            f=1
            while x <=n:
                f=f*x
                x+=1
                print(" EL FACTORIAL DE ",n, " E: ",f,)   
            else:
                print("NO SE PUEDE CALCULAR EL FACTORIAL" )     
    elif opcion ==2:
        # Dado un número entero N que representa una contraseña y asumiendo que una
        # contraseña debe tener al menos 10 dígitos para ser segura, determine si la
        # contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
        # nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
        # mostrar un mensaje de éxito al usuario, por salida estándar.
        print("TIENE TRES INTENTOS PARA INGRESAR LOS DATOS CORRECTOS ")
        contador =1 
        while contador <=3:
            usuario= int(input("INGRESE SU USUARIO  " ))
            contraseña=int(input("INGRESE SU CONTRASEÑA"))
        
    elif opcion==3:
        # Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
        # informe al usuario qué valor tiene el número mayor y qué valor tiene el número
        # menor, sin contar el cero (0).
        lista =[]
        cantidad= int(input("CANTIDAD:  "))
        mayor=0
        menor=0 
        i=1
        while(cantidad>=1):
            numero= float(input("NUMERO #" + str(i) + ": " ))
            i=i+1
            cantidad=cantidad-1
            mayor = max(lista)
            menor = min(lista)
            print(" LISTA :", str(lista))           
            print(" MAYOR :", str(mayor))
            print("MENOR  :", str(menor))   
            
        
    elif opcion==4:
        # Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
        # peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
        # base en dicha secuencia se desea realizar un estudio a fin de conocer:
        # • Edad promedio de todas las personas en la muestra.
        # • Peso promedio de todas las personas en la muestra.
        # • Estatura promedio de todas las personas en la muestra.
        # • Cuántas personas hay con edad entre los 18 y 25 años.
        # # • Cuántas personas son mayores a 36 años.
        # • Cuál es el promedio de peso de las personas con edades entre 18 y 35 años.
        numero=int (input("INGRESE NUMERO "))
        
    elif opcion ==5:
       #  Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
       # del 1 hasta la del 10.
       numero= int(input("INGRESE EL NUMERO DE LA TABLA DE MULTIPLICAR QUE DESEE \n"))
       if numero ==1:
           print("TABLA DE MULTIPLICAR DEL 1 \n 1x1=1 \n 1x2=2 \n  1x3=3 \n 1x4=4 \n 1x5=5 \n  1x6=6 \n 1x7=7  \n 1x8=8  \n 1x9=9  \n  1x10x10  \n 1x11=11  \n 1x12=12 ")
       elif numero == 2:
           print("TABLA DE MULTIPLICAR DEL 2 \n 2x1=2 \n  2x2=4 \n  2x3=6  \n  2x4=8 \n 2x5=10 \n 2x6=12 \n 2x7=14 \n 2x8=16  \n  2x9=18 \n 2x10=20 \n  2x11=22 \n   2x12=24")
       elif numero ==3:            
           print("TABLA DE MULTIPLICAR DEL 3 \n 3x1=3 \n  3x2=6 \n  3x3=9 \n  3x4=12 \n 3x5=15 \n 3x6=18 \n 3x7=21 \n 3 x=24 \n 3x9=27 \n 3x10=30 \n 3x11=33 \n 3x12=36")
       elif numero ==4:           
           print("TABLA DE MULTIPLICAR DEL 4 \n 4x1=4 \n 4x2=8 \n 4x3=12 \n 4x4=16 \n  4x5=20 \n 4x6=24 \n 4x7=28 \n 4x8=32 \n 4x9=36 \n 4x10=40 \n 4x11=44 \n 4x12=48")
       elif numero ==5:           
           print("TABLA DE MULTIPLICAR DEL 5 \n 5x1=5 \n 5x2=10 \n 5x3=15 \n 5x4=20 \n  5x5=25 \n 5x6=30 \n 5x7=35 \n 5x8=40 \n 5x9=45 \n 5x10=50 \n 5x11=55 \n 5x12=60")
       elif numero ==6:           
           print("TABLA DE MULTIPLICAR DEL 6 \n 6x1=6 \n 6x2=12 \n 6x3=18 \n 6x4=24 \n 6x5=30 \n 6x6=36 \n 6x7=42 \n 6x8=48 \n 6x9=54 \n 6x10=60 \n 6x11=66 \n 6x12=72 ")
       elif numero ==7:           
           print("TABLA DE MULTIPLICAR DEL  7 \n 7x1=7 \n 7x2=14 \n 7x3=21 \n 7x4=28 \n  7x5=35 \n 7x6=42 \n 7x7=49 \n 7x8=56 \n 7x9=63  \n 7x10=70 \n 7x11=77 \n 7x12=85  ")
       elif numero ==8:           
           print("TABLA DE MULTIPLICAR DEL  8 \n 8x1=8 \n 8x2=16 \n 8x3=24 \n 8x4=32 \n  8x5=40 \n 8x6=48 \n 8x7=56 \n 8x8=64 \n 8x9=72  \n 8x10=80 \n 8x11=88 \n 8x12=96 ")
       elif numero ==9:           
           print("TABLA DE MULTIPLICAR DEL  9 \n 9x1=9 \n 9x2=18 \n 9x3=27 \n 9x4=36 \n  9x5=45 \n 9x6=54 \n 9x7=63 \n 9x8=72 \n 9x9=81 \n 9x10=90 \n 9x11=99 \n 9x12=108")
       elif numero ==10:           
           print("TABLA DE MULTIPLICAR DEL  10 \n 10x1=10 \n 10x2=20 \n 10x3=30 \n 10x4=40 \n  10x5=50 \n 10x6=60 \n 10x7=70 \n 10x8=80 \n 10x9=90 \n 10x10=100 \n 10x11=110 \n 10x12=120 ")
       elif numero ==11:           
           print("TABLA DE MULTIPLICAR DEL 11 \n 11x1=11 \n 11x2=22 \n 11x3=33 \n 11x4=44 \n  11x5=55 \n 11x6=66 \n 11x7=77 \n 11x8=88 \n 11x9=99 \n 11x10=110 \n 11x11=121 \n 11x12=132 ")
       elif numero ==12:           
           print("TABLA DE MULTIPLICAR DEL  12 \n 12x1=12 \n 12x2=24 \n 12x3=36 \n 12x4=48 \n  12x5=60 \n 12x6=72\n 12x7=84 \n 12x8=96 \n 12x9=108 \n 12x10=120 \n 12x11=132 \n 12x12=144")
       elif numero >=13:
           print("NO EXISTE ESA TABLA DE MULTIPICAR EN EL SISTEMA \n INGRESE UN NUMERO DEL 1 AL  12 \n ")   
           
    elif opcion ==6:
        #Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.
        print("LAS FICHAS DE DOMISO SON : ....... \n [0/0] [0/1] [0/2] [0/3] [0/4] [0/5]\n  [0/6] [1/1] [1/2] [1/3] [1/4] [1/5] \n [1/6] [2/2] [2/3] [2/4] [2/5] [2/6] \n [3/3] [3/4] [3/6] [4/4] [4/5] [4/6] [5/5] [6/6]" )
    
    elif  opcion == 7 :
        #Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
        #la serie termina al leer un 0.   
        nuemro =int(input("ndndn"))    

    elif opcion == 8:
        #Construya una función que solicite edades al usuario y determine el promedio de
        # las edades mayores a 18 años. El usuario indicará cuando desea dejar de
        # suministrar datos de entrada. En la Acción Principal se informará el promedio
        # calculado.
        n1=int(input("INGRESE EL PRIMER VALOS "))
