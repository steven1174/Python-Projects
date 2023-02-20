import random
    
def mixed_sorting(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        
        print(left, '*' * 5,right)

        mixed_sorting(left)
        mixed_sorting(right)

        # Iterator for sublists
        i = 0
        j = 0
        # Iteraror for main list
        k = 0

        print(len(left), len(right))
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        
        print(f'Left list: {left}', f'Right list: {right}', sep = '\n')
        print(list)
        print('-' * 50)

    return list


def run():
    list_size = int(input('What is the size of the list? '))
    list = [random.randint(0, 100) for i in range(list_size)]

    print(list,'\n')
    
    sorted_list = mixed_sorting(list)
    
    print(sorted_list)

if __name__ == "__main__":
    run()