# Script to Print the Directory Files Count and Display their Names 

import os

req_dir=input("Enter the Directory Name :")

result=os.listdir(req_dir)

print(f"The Result type is {type(result)}")

print ("No of Objects in {} is {}".format(req_dir,len(result)))


for x in result:
    print(f"The file or Directory name is : {x}")


print("Program Completed :)")
    
