import array as arr
var=arr.array( 'B',[1,2,3,4,5])
print(var[2])
var[2]=12
print(var)

lis=[1,2,3,4]
for i in lis:
    print(i)


#Prime number task
print("Prime numbers are:")
for i in range(2,11):
    count=0
    for j in range(2,i):
        if(i%j)==0:
            count=count+1
    if count==0:
        print(i)
    else:
        count=0
print("Using continue")
lis2=[2,3,4,5,6,7]
for i in lis2:
    if i==5:
        continue
    print(i)