b1 = int(input('Первый член '))
q = int(input('Знаменатель '))
n = int(input('Количество членов прогрессии '))
for i in range(0, n, 1):
  b = b1 * q
  print(b)
  b1 = b