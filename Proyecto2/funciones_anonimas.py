## Normal Function
def increment_v1(x):
  return x + 1

## Function with Lambda
increment_v2 = lambda x: x + 1

result = increment_v1(10)
print('increment_v1 ---> ', result)

result = increment_v2(20)
print('increment_v2 ---> ',result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)