a=[]
b=[]
count=0

z1=int(input("Enter Number of elemnts in Set A : "))
z2=int(input("Enter Number of elemnts in Set B : "))

for i in range(z1):
    x=int(input("Enter element : "))
    a.append(x)

for i in range(z2):
    x=int(input("Enter element : "))
    b.append(x)

for i in range(z1):
    for j in range(z2):
        if(a[i]==b[j]):
            count=count+1

Pab=count/z2
Pba=count/z1
print(Pab)
print(Pba)
