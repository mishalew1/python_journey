# Python learning journey


## Documenting methods I have learned

**methods**

Methods are functions only available to a specific object.  
my_list.append()  
my_string.format()  
append only exists for lists and the format function only exists for strings.  



# format()
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

# range()
"""
	range() creates a sequence of numbers, starting at 0 by default and incrementing by1 (by default) and stops at a specified number.

	Syntax:  range(start, stop, step)
	start=optional, default=0
	stop=required, (up to, but not including, a stop of 9 will count to 8) 
	step=optional default=1

	Examples:
	x = range(3, 6)
	for n in x:
		print(n)
"""


