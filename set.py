# st={33,5,23,"pppp","high",(25,55)}
# print(st)




st={33,5,23,"pppp","high",(25,55)}
print(st)
st.add("kgf")
print(st)
st.remove("high")
print(st)



# str1={33,5,23,55,"pppp","high",}
# str2={11,33,44,5,8,"IKJ""tuv"}
# print(str1 | str2)
# print(str1.intersection(str2))

str1={33,5,23,55,"pppp","high",}
str2={11,33,44,5,8,"IKJ""tuv"}
print(str1 | str2)
print(str1.intersection(str2))
print(str1.symmetric_difference(str2))

#dict
dict={11:'pq',22:'pm',33:'ab'}
print(dict)
print(dict[11])
print(dict.get(33))
print(dict.keys())
print(dict.values())
print(dict.items())
dict[44]="AA"
print(dict)
dict.update({55:'BB'})
print(dict)
dict[55]='cc'
print(dict)                          #pop #clear #del
dict.pop(55)
print(dict)


#taks
for i in dict.items():
    print(i)

#nested dict
dict1={11:'QQ',22:'WW',33:'KK',44:'LL'}
dict2={12:'pq',23:'pm',66:'ab'}
obj1={"var1":dict1,"var2":dict2}
print(obj1)












