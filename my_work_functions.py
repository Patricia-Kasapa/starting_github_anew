i = 0
while(i < 10):
          i = i + 1
          print(i)


i = 7
while(i < 19):
	print(i)
	i = i + 1

i = 12
while(i < 20):
	if i % 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1
       

def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    mylist = []
    while(a < b):
        if a % 2 == 0:
            mylist.append(a)
            a = a + 1
        else: a = a + 1
    print(mylist[::-1])
