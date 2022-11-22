## List of Numbers
numbers_v1 = [1, 2, 3, 4]

numbers_v2 = []

## Transform with for
for i in numbers_v1:
  numbers_v2.append(i * 2)

## Transform with map
numbers_v3 = list(map(lambda i: i * 2, numbers_v1))

print('Numbers_v1 ---> ',numbers_v1)
print('Numbers_v2 ---> ',numbers_v2)
print('Numbers_v1 ---> ',numbers_v3,'\n')

## Map with list of different length
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print('Numbers_1 ---> ',numbers_1)
print('Numbers_2 ---> ',numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print('Results ---> ', result,'\n')

## Map with Dictionary
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('- New list')
print(new_items,'\n')
print('- Old list')
print(items)