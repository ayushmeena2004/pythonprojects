'''fact =int(input("Enter the number to get its factorial:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        
        return n*factorial(n-1)
a=factorial(fact)
print(a)'''
#0 1 1 2 3 4 5
letn=int(input("Enter the length of fibonacci sereis: "))


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
fibonacci(letn)
for i in range(letn):
    print( fibonacci(i) ,end="")
