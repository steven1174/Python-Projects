import sys

# Handling the ZeroDivisionError Exception
def exception_1():
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)

# Handling the FileNotFoundError Exception
def exception_2():
    print("Choose an option")
    print("\ta. Filepath: pi_digits.txt")
    print("\tb. Filepath: NO-FILE")

    option = input('\n')
 
    if option.lower() == 'a':
        filepath = './Datasets/pi_digits.txt'
    elif option.lower() == 'b':
        filepath = ''
    else:
        print('No valid option')
        option = input('\n')

    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        msg = "Sorry, the file " + filepath + " does not exist."
        print(msg)

def run():
    thismodule = sys.modules[__name__]

    for i in range(1,3):
        print(f'\nException {i}:')
        function = getattr(thismodule,f'exception_{i}')
        function()

if __name__ == '__main__':
    run()