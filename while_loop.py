Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 

i = 0
while(i < 10):
    i = i + 1
    print(i)
    

k = 1
for i in range(0, 4):
    for j in range(0, k):
        print("* ", end ="")
    k = k + 1
    print()
    k = 4
    for i in range(0, 4):
        for j in range(0, k):
            print("* ", end = "")
        k = k - 1
        print()

