# Script to Print only the methods of an Data Type

user_input=input("Enter the Data Type:")

l=[k for k in dir(user_input)if k.startswith("__")is False]
i=1

for x in l:
    print(i,x)
    i=i+1

    
    
