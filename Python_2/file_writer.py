import sys

def writting_v1(filepath):
    with open(filepath, 'w') as file_object:
        file_object.write("I love programming.")

def writting_v2(filepath):
    with open(filepath, 'w') as file_object:
        file_object.write("I love programming.\n")
        file_object.write("I love creating new games.\n")

def writting_v3(filepath):
    with open(filepath, 'a') as file_object:
        file_object.write("I also love finding meaning in large datasets.\n")
        file_object.write("I love creating apps that can run in a browser.\n")

def run():
    thismodule = sys.modules[__name__]
    filepath = './Datasets/programming.txt'
    
    i= 1
    while i <= 3:
        print(f'Writting Version {i}')
        function = getattr(thismodule,f'writting_v{i}')
        function(filepath)
        i += 1

        option = input('Continue Y/N ')
 
        if option.upper() == 'Y':
            continue
        elif option.upper() == 'N':
            i = 4
        else:
            print('No valid option')
            option = input('Continue Y/N ')

if __name__ == '__main__':
    run()