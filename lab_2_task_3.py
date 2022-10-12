a = int(input('Год '))
b = a % 4
if b == 0:
  print(f'{a} - високосный')
else:
  print(f'{a} - невисокосный')