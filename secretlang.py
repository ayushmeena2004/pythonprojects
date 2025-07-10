import random
import string

random_chars = ''.join(random.choices(string.ascii_letters, k=3))
#encoding
text=input("Enter your text:")
n=len(text)
if len(text)>3:
    text1=text[3:]+text[:3]
    a=random_chars+text1+random_chars
    
else:
    a=text[::-1]
    
print(f"our Encoded string is: {a}\n\n")
#decoding
if len(a)<3:
    b=a[::-1]
    
else:
    b=a[3:]
    b=b[:n]
    b=b[n-3:]+b[:n-3]
    
print(f"our decoded string is: {b}")