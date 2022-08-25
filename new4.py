from site import removeduppaths


var1=[-65427,"soham", "xyz",10,20,23j,65.42,{23:"hdgfht"}]
#var1.insert(1,12)
#print(var1)
#print(var1.index)
#var1[2]="abc"
#print(var1)
#var1.remove("abc")
#print(var1)
#var1.pop()
#print(var1)
#var1.pop(2)
#print(var1)
#var1.clear()
#print(var1)
#del var1
#print(var1)
mylist=["a","b","c","d","j","k","l","a"]
mylist=list(dict.fromkeys(mylist))
#print(mylist)
#mylist=list(set(mylist))
#mylist=[*set(mylist)]
#mylist.sort(reverse=True)
mylist.reverse()
print(mylist+var1)
# print(mylist)
mylist.extend(var1)
print(mylist)

var2=[]