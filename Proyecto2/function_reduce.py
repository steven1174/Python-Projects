import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('Counter => ', counter, ' Item => ', item, ' Accum => ', counter + item)
  return counter + item

result = functools.reduce(accum, numbers)
print(' \n','Result: ',result)

