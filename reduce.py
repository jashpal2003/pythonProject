from functools import reduce
number = [1,2,3,4,5,6,7]
product= reduce(lambda x,y:x*y,number)
print(product)