


var1=(12,11,33,44)
print(var1)
print(var1[2])

var2=("Pratham",4249,9,(6567),[12,22])
print(var2)
print(var2[3])
print(var2[-1])
print(var2[1:3])


#var3=([1,55,99,22][2,5,88,99])
#print(var3[0][0])
#print(var3[0][1])
#print(var3[0][2])
#print(var3[1][0])
#print(var3[1][1])

var4 =("PP","PP")
var5 =(("PP ")*5)
print(var5)
print(var4)
 
a=("DYP",99,"Pratham")
b=("KIT",55,"Sai")
(college,rollno,name)=a
(clg,rno,nm)=b
print(college)
print(rollno)
print(name)


var6 =list(var2)
print(var6)
var6[1]="Hello"
x= tuple(var6)
print(x)

conc = var6+var6
print(var6.count(9))
print(conc)
print(var6.index(9))

#astrik
tupd=(12,14,15,78j,"mno","pqr",[789,"demo"],(65,67))
(a,b,*c)=tupd
print(a)
print(b)
print(c)

#forloop
# for p in var6:
#     print(p)
#while loop
# i= 0
# while(i<len(var6)):
#     print(var6[i])
#     i=i+1
    
for i in range(0,3):
    print(var6[i])
    
    #task'
    i=0
    while(1<50):
      print(i)
      i= i + 3









