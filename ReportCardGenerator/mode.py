import sys

def prompt_for_mode():

	'''Asks the user to choose a mode. Accepts KeyboardInterrupt and EOFError.'''
	
	return raw_input("\nEnter 'location' to generate reports by proximity and 'name' to search schools by name. \nType 'top10' to enter Top 10 mode. ")


def interpret_mode(input):
	
	'''Interprets str as a mode. Accepts "quit".'''
	if input.strip().lower() == 'quit':
		sys.exit()	
	elif input.strip().lower() in ['location', 'name', 'top10'] :
		return input.strip().lower()
	else:
		print "\nInvalid Mode."
		return None


def get_mode():

	'''Recursively asks the user to choose a mode and interprets it.'''
	mode = interpret_mode(prompt_for_mode())
	if mode is not None:
		return mode
	else:
		return get_mode()
