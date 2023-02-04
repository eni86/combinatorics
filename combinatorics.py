#from the math library imports the factorial function
from math import factorial

################Check integrity of the data########

def isNumber(m):
    '''This function is used if the type of the data received 
    is a number'''
    return type(m) == int

def m_greater_than_n (m,n):
    '''It checks that the first number is greater than the second'''
    return m >= n

##################################################################

##################Pregunta si desea continuar ##################

def keepGoing():
    '''This function asks the user if he wants to keep operating.
    It contemplates 3 options: yes, no or I don't get
    wht do you want me to do'''
    sigo = input("Desea continuar? Si/nO")
    if sigo.lower() == 'no':
        return False
    elif sigo.lower() == 'si':
        return True
    else:
        print("No entiendo lo que se pide")
        keepGoing()



################Operations########################################
def calc_combinations(m, n):
    ''' This function returns the combinations
    of two numbers'''
    return factorial(m)/(factorial (n) * factorial (m-n))

def calc_arrengements(m, n):
    ''' This function returns the combinations
    of two numbers'''
    return factorial(m)/factorial (m-n)

def calc_permutations(m):
    ''' This function returns the permutations of
    a given number'''
    return factorial(m)

################################################################

##########################MENU PRINCIPAL####################
def Menu():
    print ("Opciones del programa:")
    print("1) Calcular arreglos")
    print("2) Calcular permutaciones")
    print("3) Calcular combinaciones")
    print("4) Salir")




###################MAIN############################
def main ():
    print ("Bienvenido a Combinatorics")
    sigo = True
    while sigo:
        Menu()
#################################################


        try:
            option = int(input("Que opcion elijes? "))
        except ValueError:
            print ('No entiendo que deseas hacer')
        else:

            #If the user wants to go out, here is the option
            if option == 4:
                sigo = False

            else:
                try:
                    #here the program will prompt to the user to get a number
                    #which is required for all calculation options
                    primer_nro=int(input("Inserta el primer numero para \
                    realizar el calculo: (en el caso de permutaciones, solo se pide este numero)"))

                except ValueError:
                    print ('Lo ingresado no es un numero')
                    primer_nro=int(input("Inserta el primer numero para realizar el calculo: (en el caso de permutaciones, solo se \
                    pide este numero)"))
                else:

                    #if the order is 2, the program will calculate the permutations
                    #of that number
                    if option == 2:
                        print("Las permutaciones de {} son: ".format(calc_permutations(primer_nro)))

                        print(calc_permutations(primer_nro))
                    #since in both cases, it will ask for 2 numbers and Ive already asked for
                    #the first, here it will ask for the secon one

                    elif option == 1 or option == 3:
                        try:

                            segundo_nro=int(input("Inserta el segundo numero para realizar el calculo:"))

                        #Closes the try on line 102 where it asks for the first number to operate 
                        except ValueError:
                            print('el primer numero ingresado no es valido')
                            segundo_nro=int(input("Inserta el segundo numero para realizar el calculo:"))
                        else:
                            #combination of primer_nro in segundo_nro

                            if option == 1 and primer_nro >= segundo_nro:
                                print('Las combinaciones {} de {} en son:'.format(primer_nro, segundo_nro, calc_combinations(primer_nro,segundo_nro)))

                            
                            #combination of segundo_nro of primer_nro

                            elif option == 1 and primer_nro < segundo_nro:
                                print('Las combinaciones de {} en {} son:'.format(segundo_nro,primer_nro, calc_combinations(segundo_nro,primer_nro)))


                            #arrangements of primer_nro in segundo_nro

                            elif option == 3 and primer_nro >= segundo_nro:
                                print('Los arreglos de {} en {} son:'.format(segundo_nro,primer_nro, calc_arrengements(primer_nro,segundo_nro)))


                            #combination of segundo_nro in primer_nro

                            elif option == 1 and primer_nro < segundo_nro:
                                print('Las combinaciones de {} en {} son:'.format(segundo_nro,primer_nro, calc_arrengements(segundo_nro,primer_nro)))

                            else:
                                print("No deberia entrar aca")



                    
                    
                    #this else closes the if in line 94 that checks the options
                    #after printing the main menu
                    else:
                        print("La orden no existe")


        sigo = keepGoing()

  




if __name__ == '__main__':
    main()
    print("Gracias por usar combinatorics")