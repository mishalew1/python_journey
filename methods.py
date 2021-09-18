# Documenting methods I have learned

"""
	format() was introduced in Python 3 to handle complex string formatting more efficiently
	
	Syntax:  string.format() 
	Syntax:  string.format(value1, value2...)
	The values are placeholders, and they can be identified using 
		named indexes {price}, {age}
		numbered indexes {0}, {1}, {2}
		or emoty placeholders {}, {}

	Examples:
	txt1 = 'My name is {fname}, I am {age}'.format(fname = "John", age = 36)
	txt2 = 'My name is {0}, I am {1}'.format('John',36)
	txt3 = 'My name is {}, I'm {}'.format('John',36)
"""
