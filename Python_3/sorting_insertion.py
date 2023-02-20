import random
    
def insertion_sort(list):
    for index in range(1, len(list)):
        current_value = list[index]
        current_position = index

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value

    return list

def run():
    list_size = int(input('What is the size of the list? '))
    list = [random.randint(0, 100) for i in range(list_size)]
    sorted_list = insertion_sort(list)
    
    print(list)
    print(sorted_list)

if __name__ == "__main__":
    run()

