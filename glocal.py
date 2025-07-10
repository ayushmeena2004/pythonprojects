x=5 #local
print(f"before value of x={x}")
def glb():
    global x #global variable change
    x=4
glb()
print(f"After value of x={x}")