#from the math library imports the factorial function
from math import factorial

################Check integrity of the data########


def m_greater_than_n (m,n):
    '''It checks that the first number is greater than the second'''
    return m >= n

##################################################################

##################Pregunta si desea continuar ##################

def keepGoing():
    '''This function asks the user if he wants to keep operating.
    It contemplates 3 options: yes, no or I don't get
    wht do you want me to do'''
    sigo = input("Desea continuar? Si/nO ")
    if sigo.lower() == 'no':
        return False
    elif sigo.lower() == 'si':
        return True
    else:
        print("No entiendo lo que se pide")
        keepGoing()



################Operations: one clas for every operation########################################
class calcuComb:
  '''Here calculates the combinations of m in n and saves it in a variable called arr
  and returns a string with the given variables and the calculated value'''

  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.arr = factorial(m)/(factorial (n) * factorial (m-n))
  
  def __str__(self):
    return f'Los arreglos de {self.m} en {self.n} son: {self.arr}'

class calcuArr:
  '''Here calculates the arrays of m in n and saves it in a variable called comb
  and returns a string with the given variables and the calculated value'''

  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.comb=factorial(m)/factorial (m-n)
  
  def __str__(self):
    return f'Los arreglos de {self.m} en {self.n} son: {self.comb}'

class calcuPer():
  '''Here calculates the permutations of m and saves it in a variable called fact
  and returns a string with the given variables and the calculated value'''

  def __init__(self, m):
    self.m= m
    self.fac= factorial(m)

  def __str__(self):
    return f'Las permutaciones de {self.m} son: {self.fac}'



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
                    primer_nro=int(input("Inserta el primer numero para realizar el calculo: (en el caso de permutaciones, solo se pide este numero) "))

                except ValueError:
                    print ('Lo ingresado no es un numero')
                    primer_nro=int(input("Inserta el primer numero para realizar el calculo: (en el caso de permutaciones, solo se pide este numero)"))
                else:

                    #if the order is 2, the program will calculate the permutations
                    #of that number
                    if option == 2:
                        per=calcuPer(primer_nro)
                        print(per.__str__())

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
                                per=calcuComb(primer_nro,segundo_nro)
                                print(per.__str__())
                                sigo = keepGoing()

                            
                            #combination of segundo_nro of primer_nro

                            elif option == 1 and primer_nro < segundo_nro:
                                per=calcuComb(segundo_nro,primer_nro)
                                print(per.__str__())
                                sigo = keepGoing()


                            #arrangements of primer_nro in segundo_nro

                            elif option == 3 and primer_nro >= segundo_nro:
                                per=calcuArr(primer_nro,segundo_nro)
                                print(per.__str__())
                                sigo = keepGoing()


                            #combination of segundo_nro in primer_nro

                            elif option == 1 and primer_nro < segundo_nro:
                                per=calcuArr(segundo_nro,primer_nro)
                                print(per.__str__())
                                sigo = keepGoing()

                            else:
                                print("No deberia entrar aca")



                    
                    
                    #this else closes the if in line 94 that checks the options
                    #after printing the main menu
                    else:
                        print("La orden no existe")




  




if __name__ == '__main__':
    main()
    print("Gracias por usar combinatorics")    