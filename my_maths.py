 Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> def calculate("add", a, b):
	
SyntaxError: invalid syntax
>>> 
>>> def calculate("add",a,b):
	
SyntaxError: invalid syntax
>>> 
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))
	
	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)

	
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal = "Add":
		
SyntaxError: invalid syntax
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal = "Add":
		
SyntaxError: invalid syntax
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal = "Add": add()
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal == "Add":
		return add
		elif cal == "Subtract":
			
SyntaxError: invalid syntax
>>> 
>>> 
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal == "Add":
		return add
		else if cal == "Subtract":
			
SyntaxError: invalid syntax
>>> 
>>> 
>>> def calculate():
	a = int(input("First value"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal == "Add":
		return add
		elif cal == "Subtract":
			
SyntaxError: invalid syntax
>>> 
>>> 
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal == "Add":
		return add
	elif cal == "Subtract":
		return subtract
	elif cal == "Multiply":
		return multiply
	elif cal == "Divide":
		return divide
	else:
		print("Not that math")

		
>>> calculate()
First value?2
Second Value3
Add, Subtract, Multiply or DivideAdd
<function calculate.<locals>.add at 0x75b9f0c0>
>>> 
>>> 
>>> def calculate():
	a = int(input("First value?"))
	b = int(input("Second Value"))
	cal = str(input("Add, Subtract, Multiply or Divide"))

	def add():
		ans = a + b
		return(ans)
	def multiply():
		ans = a * b
		return(ans)
	def subtract():
		ans = a - b
		return(ans)
	def divide():
		ans = a / b
		return(ans)
	if cal == "Add":
		return add()
	elif cal == "Subtract":
		return subtract()
	elif cal == "Multiply":
		return multiply()
	elif cal == "Divide":
		return divide()
	else:
		print("Not that math")

		
>>> calculate()
First value?3
Second Value2
Add, Subtract, Multiply or DivideAdd
5
>>> calculate()
First value?2
Second Value3
Add, Subtract, Multiply or DivideMultiply
6
>>> 
