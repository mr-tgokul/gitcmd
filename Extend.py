# Script to Study about Extend Operation using append 

a=[20,10,5,'c','azure',True]

b="Testing Example"

print("Before adding Variable b to A")
print(a)

for i in b:
    a.append(i)   # Its equal to a.extend(b). We are using for loop instead of using append

print("After adding Variable b to A")
print(a)
