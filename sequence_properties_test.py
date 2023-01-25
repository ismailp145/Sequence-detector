import my_sequence

import sequence_properties

# sequence option constants
GENERIC = '1'
ARITHMETIC = '2'
GEOMETRIC = '3'
QUADRATIC = '4'
EXIT_1 = '5'
# a list containing the sequence options as string constants
SEQUENCE_OPTIONS = ['GENERIC','ARITHMETIC','GEOMETRIC','QUADRATIC','EXIT']

# properties option constants 
GET_DIFFERENCES = '1'
GET_RATIOS = '2'
IS_LINEAR = '3'
IS_GEOMETRIC = '4'
IS_QUADRATIC = '5'
LINEAR_TRANSFORMATION = '6'
EXIT_2 = '7'
# a list containing the sequence properties as string constants	
PROPERTIES_OPTIONS = ['Differences','Ratios','Linear Test','Geometric Test', 
			  		  'Quadratic Test','Linear Transformation','EXIT']

# linear sequence option constants
CREATE_LINEAR_SEQUENCE = '1'
GET_LINEAR_EQUATION = '2'
# a list containing the linear sequence options as string constants	
LINEAR_SEQUENCE_OPTIONS = ['Create from mx + b rule','Get Linear Rule']

# @param a list of menu options
# Displays options from the list
# @return void
def print_menu_options(menu_list):
	num = 1
	for option in menu_list:
		print(num, ") ", option, sep = '', end = '\n')
		num += 1;
	print()	   
		
# @param a list of menu options 
# Prompts user to choose an option and displays the menu choices
# @return a string containing the menus option 		
def get_user_input(menu_list):
	print_menu_options(menu_list)
	return input('')		
	
# @param void 
# Precondition: User string is a valid numerical sequence of numbers
# each separated by a whitespace
# @return a list created from the user input string 
	
def generic_sequence():
	#prompt user for a sequence of numbers
	print("Enter a sequence of numbers each",
			      "separated by a whitespace") 
	the_sequence = (input('')).split()
	
	#convert list of string numbers to list of numbers
	the_sequence = [float(i) for i in the_sequence] 
	
	#if floats are integral, convert to integers
	index = 0
	
	while index < len(the_sequence):
		if(the_sequence[index].is_integer()):
			the_sequence[index] = int(the_sequence[index])
		index += 1
	
	return the_sequence	


def sequence_options():
	more_sequences = True
	
	while(more_sequences):
		print("Choose from the following by entering a valid number choice.")
		sequence_choice = get_user_input(SEQUENCE_OPTIONS)
		
		if(sequence_choice == GENERIC):
			choice = input('Create linear sequence from equation? (y/n): ')
			if(choice == 'y'):
				num_terms = num_terms = int(input('Enter the number of terms for this sequence: '))
				linear_exp = input('Enter a linear expression in the form mx + b: ')
				generic = sequence_properties.linearSequence(num_terms, linear_exp)
			else:	
				generic = generic_sequence()
			properties_options(generic)						
		elif(sequence_choice == ARITHMETIC):
			arithmetic = my_sequence.Arithmetic()	
			expression = input('Enter a linear expression in the form mx + b: ')
			num_terms = int(input('Enter the number of terms for this sequence: '))
			arithmetic.reset(expression,num_terms)
			properties_options(arithmetic.asList())
		elif(sequence_choice == GEOMETRIC):
			geometric = my_sequence.Geometric()
			expression = input('Enter an expontial expression in the form r^n or a(r)^n: ')
			num_terms = int(input('Enter the number of terms for this sequence: '))
			geometric.reset(expression,num_terms)
			properties_options(geometric.asList())	
		elif(sequence_choice == QUADRATIC):	
			params = input('Enter the parameters A, B, and C each seperated by whitespace: ').split(' ')
			num_terms = int(input('Enter the number of terms for this sequence: '))
			A = float(params[0])                  
			B = float(params[1])
			C = float(params[2])	 
			quadratic = my_sequence.Quadratic(A, B, C, num_terms)								  
			properties_options(quadratic.asList())	
		elif(sequence_choice == EXIT_1):
			more_sequences = False	
		else:
			print("INVALID CHOICE. TRY AGAIN")


def properties_options(seq):
	more_options = True
	
	while(more_options):
		print('Choose a sequence property to apply to:', seq)
		choice = get_user_input(PROPERTIES_OPTIONS)
			
		if(choice == GET_DIFFERENCES):
			diffs = sequence_properties.getDiffs(seq)
			print("The differences of:", seq, ' are', diffs)
		elif(choice == GET_RATIOS):
			ratios = sequence_properties.getRatios(seq)	
			print("The ratios of:", seq, ' are', ratios)
		elif(choice == IS_LINEAR):
			if(sequence_properties.isLinear(seq)):
				print(seq, " is linear")
				choice = input('Get linear equation? (y/n): ')
				if(choice == 'y'):
					equation = sequence_properties.getLinearEquation(seq)
					print('Linear equation is',equation)
			else:
				print(seq, " is NOT linear")
			
		elif(choice == IS_GEOMETRIC):
			if(sequence_properties.isGeometric(seq)):
				print(seq, " is geometric")
			else:
				print(seq, " is NOT geometric")	
		elif(choice == IS_QUADRATIC):
			if(sequence_properties.isQuadratic(seq)):
				print(seq, " is quadratic")
			else:
				print(seq, " is NOT quadratic")	
		elif(choice == LINEAR_TRANSFORMATION):
			linear_exp = input('Enter a linear expression in the form mx + b: ')
			new_sequence = sequence_properties.linearTransformation(seq, linear_exp)
			print("The linear transformation of the sequence")
			print(seq)
			print("with rule",linear_exp, "is")
			print(new_sequence)		
		elif(choice == EXIT_2):
				more_options = False


def main():
	sequence_options()
						
main()	
	