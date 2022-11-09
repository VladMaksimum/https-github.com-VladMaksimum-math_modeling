pi = 3.14
def s_circle(r):
  s = pi * r**2
  return s
def s_pryam(a, b):
  s = a * b
  return s
def s_triug(a, h):
  s = (a * h)/ 2
  return s
c = input()
if c == 'circle':
  r = int(input())
  print(s_circle(r))
if c == 'pryam':
  a = int(input())
  b = int(input())
  print(s_pryam(a, b))
if c == 'triug':
  a = int(input())
  h = int(input())
  print(s_triug(a, h))