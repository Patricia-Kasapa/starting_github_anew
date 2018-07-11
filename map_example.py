##def is_even():
##      numbers = [1,56,234,87,4,76,24,69,90,135]
##      t = [number for numbers % 2 in numbers]

##def is_even(x): return (x % 2 ==0)
##t = [1,56,234,87,4,76,24,69,90,135]
##g = list(filter(is_even, t))
##
##print(g)


## Not working yet
items = [1, 2, 3, 4, 5]
squares = map((lambda x: x % 2 == 0 ), items)
print(list(squares))
