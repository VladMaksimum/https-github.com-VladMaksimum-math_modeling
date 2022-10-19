a=int(input('Введите a: '))
b=int(input('Введите b: '))
c=int(input('Введите c: '))
d=b**2-4*a*c
if d<0:
  print('Корней нет')
elif d==0:
  x=(-1*b)/(2*a)
  print('Корень ', x)
elif d>0:
  x1=(-1*b+d**(1/2))/(2*a)
  x2=(-1*b-d**(1/2))/(2*a)
  print('Корни ', x1, x2)