#from the math library imports the factorial function
from math import factorial

################Check integrity of the data########

def isNumber(m):
	'''This function is used if the type of the data received 
	is a number'''
	return type(m) == int

def m_greater_than_n (m,n):
	'''It checks that the first number '''




################Operations######################################
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