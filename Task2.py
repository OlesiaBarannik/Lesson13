import random

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def calculate(func, x, y):
  result = func(x, y)
  return result

func_list = {1: add, 2: sub, 3: mult, 4: div}


f = func_list[random.randint(1,4)]
x = random.randint(0,100)
y = random.randint(0,100)

result = calculate(f, x, y)

print(x, f.__name__, y, " = ", result)
