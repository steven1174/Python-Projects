def my_gen():

    """Ejemplo de un generador"""

    print("Hello world!")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n

def run():

    a = my_gen()

    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

if __name__ == "__main__":
    
    run()

