Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> def get_age()
SyntaxError: invalid syntax
>>> def get_age(a):
	a = int(raw_input("Please enter your age"))
		return(a)
	
SyntaxError: unexpected indent
>>> def get_age(a):
	a = int(raw_input("Please enter your age"))
	return(a)

>>> def get_name(name):
	name = str(raw_input("Please enter your name"))
	return (name)

>>> def i_know_this_about_you():
	get_name():
		
SyntaxError: invalid syntax
>>> def i_know_this_about_you():
	get_name()
	get_age()
	
