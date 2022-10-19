a = int(input("Число "))
b1=b2=1
print(b1, b2)
i=2
while i<a:
  b3=b1+b2
  b1=b2
  b2=b3
  print(b2)
  i+=1