list3 = [34,54,67,34,98]
list3 = list(dict.fromkeys(list3))
print(list3)

# Task 3
list4 = [35,54,67,35,97]
list4 = list(set(list4))
print(list4)

list5 = [45,12,56,98,34,65]
list5.sort()
list5.reverse()
print(list5) 
list5.sort(reverse=True)            #To sort descending
print(list5) 
conc = list4 + list5      #Concatenation
print(conc)

list4.extend(list5)
print(list4)

list6 = ["abc","pqr","al","pm","pp","dm"]
c = list6.count("pqr")
if c >=1:
    print("found!")



#Set : Set can't take duplicate values
st = {12,14,16.5,12,"abc","pqr","xyz",(34,85)}
print(st)
st.add("prem")
print(st)
st.remove("prem") # To remove particular element
print(st)
# del(st)   #to delete set 
print(st)

st2 = {12,45,67,23,47,19,"prem","dm"}
st3 = {62,90,89,12,45,"al","prem"}
print(st2 | st3)        #Union of two set
print(st2.intersection(st3))    #Intersection of two set
print(st2.symmetric_difference(st3))    #To remove common values


#Dictionary
dict1 = {1: 'pp',2:'pm',3:'al'}
print(dict1)
print(dict1[1])
print(dict1.get(2))
print(dict1.keys())     #O/p: dict_keys([1, 2, 3])
print(dict1.values())   #O/p: dict_values(['pp', 'pm', 'al'])
print(dict1.items())   #O/p: dict_items([(1, 'pp'), (2, 'pm'), (3, 'al')])
dict1[4]='yl'
print(dict1)            # {1: 'pp', 2: 'pm', 3: 'al', 4: 'yl'}
dict1.update({5:'xyz'})
print(dict1)            # {1: 'pp', 2: 'pm', 3: 'al', 4: 'yl', 5: 'xyz'}
dict1[5] = 'prem'
print(dict1) 
dict1.pop(5)    #Delete key 5 element
print(dict1)

#Task 4 : To print item using loop
for i in dict1.items():
    print(i)

dict2 = {11:'as',12:'df',13:'gh',14:'jk'}
obj2 = {"var1":dict1,"var2":dict2}      #O/p: {'var1': {1: 'pp', 2: 'pm', 3: 'al', 4: 'yl'}, 'var2': {11: 'as', 12: 'df', 13: 'gh', 14: 'jk'}}
print(obj2)
