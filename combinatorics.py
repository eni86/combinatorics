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
			option = int("Que opcion elijes?")
		except ValueError:
			print ('No entiendo que desear hacer')
		else:
			pass



		pass
if __name__ == '__main__':
	main()