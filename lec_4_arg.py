def my_func(a, b):
  x = 3 * a - b
  return x
#tmp = my_func()
  
def my_func1(a=1, b=0):
  x = 3 * a - b
  return x  
#print(my_func())
print(my_func(3, 4))
#print(my_func(3))
print(my_func(b = 3))
print(my_func(b = 3, a = 9))

def my_func2(a, b=0):
  x = 3 * a - b
  return x  

def my_func3(*args):
  x = 3 * args[0] - args[1]
  return x
print(my_func(3, 4))
print(my_func(3, 4, 8))

def my_func4(**kwrqs):
  x = 3 * kwrqs['obj_1'] - kwrqs['obj_2']
  return x
print(my_func(obj_1 = 3, obj_2 = 4))
print(my_func(obj_1 = 3, obj_2 = 4, obj_3 = 8))

