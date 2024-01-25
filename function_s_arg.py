def add(a,b):
    return a + b
def sub (a , b ):
    return a - b
def mul(a,b):
    return a *b
def div(a,b):
    return a/b

# * multiple arg
def sum(* args):
    total = 0
    for i in args:
        print(i)
    return total
print(add(10,10))
print(sum(10,20,220,222,"jashpal",555))


#  *arg collect arg in tupple
# **arg collect arg in dictionary