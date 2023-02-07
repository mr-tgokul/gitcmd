a=[]

count=int(input("Enter the number of Items do you want to Enter"))


for t in range(count):
    b=input("Enter the Index {0} Index Item:".format(t))

if b.isalpha():
    a.append(b)

else:
    a.append(float(b))
    
print(a)
