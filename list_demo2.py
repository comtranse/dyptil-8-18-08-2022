lis=[1,3,4,5,5]
set1=set(lis)
lis=list(set1)
print(lis)

lis2=[1,2,3,3,4]
lis2=list(dict.fromkeys(lis2))
print(lis2)

list3=[1,3,2,4,5,8,7]
list3.sort(reverse=True)
print(list3)

print(lis2+list3)
lis2.extend(list3)
print(lis2)

list5=['AL','YL','PM','PP','DM']
for i in list5:
    if i=='AL':
        print("Found")

set1={1,2,3,3,4,4,5,'AL','YL','PM','PP','DM'}
print(set1)
set1.add(6)
print(set1)
set1.remove(1)
print(set1)
#del(set1)
print(set1)
set2={1,2,3,4,5}
set3={6,7,8,9,1}
print(set2|set3)
print(set2.intersection(set3))
print(set2.symmetric_difference(set3))

#Dictonary
dict={1:'AL',2:'YL'}
print(dict)
dict[1]='PP'
print(dict)
print(dict.get(2))
print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({3:'AL'})
print(dict)
dict.pop(3)
print(dict)

for i in dict.items():
    print(i)

dict2={3:'AL',4:'PM'}
obj={"var1":dict,"var2":dict2}
print(obj)

