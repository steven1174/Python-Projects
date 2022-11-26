import sys

def reading_v1(filepath):
    with open(filepath) as file_object:
        contents = file_object.read()
        print(contents)

def reading_v2(filepath):
    with open(filepath) as file_object:
        for line in file_object:
            print(line.rstrip())

def reading_v3(filepath):
    with open(filepath) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

def reading_v4(filepath):
    with open(filepath) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    
    print(pi_string)

def run():
    thismodule = sys.modules[__name__]
    filepath = './Datasets/pi_digits.txt'

    for i in range(1,5):
        print(f'\nReading Version {i}:')
        function = getattr(thismodule,f'reading_v{i}')
        function(filepath)

if __name__ == '__main__':
    run()