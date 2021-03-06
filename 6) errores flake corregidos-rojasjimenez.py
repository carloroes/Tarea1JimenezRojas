#import pytest
r=int(0);
b=float(0);
v=str(0);
#pytest.main()
i=input("Ingrese un parámetro: ") #se ingresa el parámetro solicitado para verificar posteriormente.
print("El parámetro ingresado es: ",i) #se muestra el parámetro introducido.
print(" ")   #imprime espacio
#explicación del sistema
print("A continuación, se empleará el método check-char para verificar el parámetro ingresado donde: ")
print("   - Una respuesta igual a 0 significa que se ingresó un único caracter alfabético.")
print("   - Un Code error 1: EFBIG (file too large); no es un solo caracter  alfabético.")
print("   - Un Code error 2: ERANGE (math result not representable; no es un solo caracter numérico (se necesita alfabetico)")
print("   - Un Code error 3: EINVAL (invalid argument), parámetro vacío.")
print("   - Un Code error 4: EILSEQ (ilegal byte sequence), no es alfabético (alfanúmerico, float, array, int...)")
print(" ")  #imprime espacio

            #PRIMERA PARTE
    #MÉTODO Check_char, para verificar caracteres ingresados:

while i.isalpha()== True:  #mientras el input sea alfanumérico

    if len(i)==1:  #si la longitud del input es igual a solo un caracter entonces imprime el siguiente resultado
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Resultado: 0 |")
        print("          |_____________|")

    if len(i)>1:  #si la longitud del input ingresado es mayor a un caracter tira el siguiente error único
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Respuesta: Code error 1: EFBIG (file too large); no es un solo caracter |")
        print("          |________________________________________________________________________|")
        
    break  #Termina el while
   
while i.isalpha()==False:  #mientras el input no sea alfanumerico
    if len(i)>1:   #si la longitud es más de un caracter no alfabético tira el siguente error único
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Respuesta: Code error 2: ERANGE (math result not representable; no es un solo caracter |")
        print("          |_______________________________________________________________________________________|")
        
    if not i:      #si no hay entrada en el input (sin espacio) muestra el siguiente error único 
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Respuesta: Code error 3: EINVAL (invalid argument), parámetro vacío |")
        print("          |____________________________________________________________________|")
        
    else:          #si no cumple ninguno de los dos if anteriores (un caracter no alfabético), entonces muestra el siguiente error único
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Respuesta: Code error 4: EILSEQ (ilegal byte sequence), no es alfabético|")
        print("          |________________________________________________________________________|")
    break  #termina el while
    
print(" ")  #imprime espacios
print(" ")  #imprime espacio
#segunda parte

            #METODO 2:
    #METODO caps_switch, en base a check_char, permite cambiar el tamaño de la letra de mayúscula a minúscula o viceversa.
print("A continuación, se empleará el método caps_switch para cambiar el tamaño del parámetro ingresado: ")  #muestra el mensaje
print(" ")  #imprime espacio

if i.isalpha()==False:   # si la entrada ingresada no es alfanumérica imprime el mismo error del método 1
    print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("          |Respuesta: Code error 4: EILSEQ (ilegal byte sequence), no es alfabético|")
    print("          |________________________________________________________________________|")
    print(" ")  #imprime espacio
   
       
else:  #sino hace esto (si la entrada es alfanumérica (solo letras))
    if len(i)==1:    #si la longitud del input es de 1 solo caracter hace lo siguiente:
        if i.upper()==True:   #si el input está en mayúscula entonces imprime lo siguiente
            print("          Respuesta:",i.swapcase())   #imprime la letra ingresada pero en mínúscula (swapcase hace el cambio automático)
            print("")   #imprime espacio

        else:  #si el input no está en mayúscula entonces imprime lo siguinte:
            print("          Respuesta:",i.swapcase())  #imprime la letra ingresada pero en mayúscula (swapcase hace el cambio automático)
            print(" ")   #imprime espacio

    else:   #si no hace nada de lo anterior entonces imprime el siguiente error que corresponde al primer método:
        print(" ")   #imprime espacio
        print("          |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("          |Respuesta: Code error 2: ERANGE (math result not representable; no es un solo caracter |")
        print("          |_______________________________________________________________________________________|")
    print(" ")  #imprime espacio
print("                                  FIN ") 
    #FIN#

