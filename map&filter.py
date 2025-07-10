from functools import reduce
l=[2,3,4,5,77,8,80]
'''
def cube(x):
    return x*x*x
newl=list(map(cube,l))
print(newl)

def great(b):
    return b>8

newfl=list(filter(great,l))
print(newfl)'''
def mysum(x,y):
    return x+y
sum=reduce(mysum,l)
print(sum)