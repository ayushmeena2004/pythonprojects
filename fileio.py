#without using with
#f=open('data/demo.txt','r')
#text=f.read()
#print(text)
#f.close()

#with 
'''with open('data/demo.txt','w') as f:
    f.write("hello baby")

#append
with open('data/demo.txt','a') as f:
    f.write("\nhello babes")

#read
with open('data/demo.txt','r') as f:
    print(f.read())'''

with open('data/demo.txt', 'r') as f:
    f.seek(5)
    print(f.tell())
    a = f.read(5)
    print(a)