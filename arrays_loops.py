# array
import array as arr

a=arr.array("B",[12,15])
print(a[1])
a[0]=10
print(a)

#looping
lst=[25,"abc","kgf",25,123]
for x in lst:
    print(x)
for x in lst:
    if(x==25):
        continue
    print(x)
