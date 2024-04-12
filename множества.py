
import random

a={b:b**2 for b in range(100)}
c=str(a)
b="".join(c)
print(b)

a={b:random.randint(1,100) for b in["a",'b']}
print(a)