a=input("Enter your DataType")
count=1

l=[x for x in dir(a) if x.startswith("__") is False]

for temp in l:
    print(count,temp)
    count +=1
