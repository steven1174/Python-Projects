import random
    
def binary_sort(list, start, stop, objective):
    
    print(f'The target number {objective} is between {list[start]} and {list[stop - 1]}')

    if start > stop:
        return False

    middle = (start + stop) // 2

    if list[middle] == objective:
        return True
    elif list[middle] < objective:
        return binary_sort(list, middle + 1, stop, objective)
    else:
        return binary_sort(list, start, middle - 1, objective)

def run():
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number would you like to find? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])
    finding = binary_sort(list, 0, len(list), objective)

    print(list)
    print(f'The target number {objective} {"is" if finding else "is not"} in the list')

if __name__ == "__main__":
    run()