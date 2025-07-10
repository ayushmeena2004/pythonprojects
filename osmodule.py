import os
folders=os.listdir("data")
i=1
for file in folders:
    
    if file.endswith(".png"):
        print(file)
        os.rename(f"data/{file}",f"data/{i}.png")
        i+=1
    
#print(os.getcwd())
#for i in folders:
    #print(os.listdir(f"data/{i}"))