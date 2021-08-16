#Nested For
brand = ['Toyota', 'Honda', 1234, 9000, 'BMW']
num= [1,2,3,4]
x=0

for a in brand:
  x=x+1
  print("Index #:",x," is ",a)
  for elem in num:
    print(elem)

