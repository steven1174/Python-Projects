import random
    
def linear_sort(list, objective):
    match = False

    for element in list:
        if element == objective:
            match = True
            break

    return match


def run():
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number would you like to find? '))

    list = [random.randint(0, 100) for i in range(list_size)]
    finding = linear_sort(list, objective)

    print(list)
    print(f'The target number {objective} {"is" if finding else "is not"} in the list')

if __name__ == "__main__":
    run()