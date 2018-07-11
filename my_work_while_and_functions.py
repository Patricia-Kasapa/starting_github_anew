#To print numbers from 0 to 10
i = 0
while(i < 10):
          i = i + 1
          print(i)


#To print the numbers from 7 to 19
i = 7
while(i < 19):
	print(i)
	i = i + 1

	
#Printing all the even numbers between 12 and 20
i = 12
while(i < 20):
	if i % 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1

       
#To Write a function called evens that takes two
#numbers and prints all the even numbers between them.
def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    while(a < b):
        if a % 2 == 0:
            print(a)
            a = a + 1
        else: a = a + 1


#To Write a function called evens that takes two
#numbers and prints all the even numbers between them in reverse.
def reverse_evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    mylist = []
    while(a < b):
        if a % 2 == 0:
            mylist.append(a)
            a = a + 1
        else: a = a + 1
    print(mylist[::-1])

