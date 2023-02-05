#Combinatorics, by Jenifer

#from the math library imports the factorial function
from math import factorial


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
class CalcuComb:
  '''Here calculates the combinations of m in n and saves it in a variable called arr
  and returns a string with the given variables and the calculated value'''

  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.arr = factorial(m)/(factorial (n) * factorial (m-n))
  
  def __str__(self):
    return f'Los arreglos de {self.m} en {self.n} son: {self.arr}'

class CalcuArr:
  '''Here calculates the arrays of m in n and saves it in a variable called comb
  and returns a string with the given variables and the calculated value'''

  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.comb=factorial(m)/factorial (m-n)
  
  def __str__(self):
    return f'Los arreglos de {self.m} en {self.n} son: {self.comb}'

class CalcuPer():
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
                    primerNro=int(input("Inserta el primer numero para realizar el calculo: (en el caso de permutaciones, solo se pide este numero) "))

                except ValueError:
                    print ('Lo ingresado no es un numero')
                    primerNro=int(input("Inserta el primer numero para realizar el calculo: (en el caso de permutaciones, solo se pide este numero)"))
                else:

                    #if the order is 2, the program will calculate the permutations
                    #of that number
                    if option == 2:
                        per=CalcuPer(primerNro)
                        print(per.__str__())

                    #since in both cases, it will ask for 2 numbers and Ive already asked for
                    #the first, here it will ask for the secon one

                    elif option == 1 or option == 3:
                        try:

                            segundoNro=int(input("Inserta el segundo numero para realizar el calculo:"))

                        #Closes the try on line 102 where it asks for the first number to operate 
                        except ValueError:
                            print('el primer numero ingresado no es valido')
                            segundoNro=int(input("Inserta el segundo numero para realizar el calculo:"))
                        else:
                            #combination of primerNro in segundoNro

                            if option == 1 and primerNro >= segundoNro:
                                per=CalcuComb(primerNro,segundoNro)
                                print(per.__str__())
                                sigo = keepGoing()

                            
                            #combination of segundoNro of primerNro

                            elif option == 1 and primerNro < segundoNro:
                                per=CalcuComb(segundoNro,primerNro)
                                print(per.__str__())
                                sigo = keepGoing()


                            #arrangements of primerNro in segundoNro

                            elif option == 3 and primerNro >= segundoNro:
                                per=CalcuArr(primerNro,segundoNro)
                                print(per.__str__())
                                sigo = keepGoing()


                            #combination of segundoNro in primerNro

                            elif option == 1 and primerNro < segundoNro:
                                per=CalcuArr(segundoNro,primerNro)
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
