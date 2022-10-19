a=int(input('Введите первое число: '))
b=int(input('Ведите второе число: '))
c=a%b
if b==0:
  print('Деление невозможно')
elif c==0:
  print(f'{a} делится на {b}')
  print('Получается ', a//b)
else:
  print(f'{a} не делится на {b}')
  print('Целая часть ', a//b)
  print('Остаток ', a%b)