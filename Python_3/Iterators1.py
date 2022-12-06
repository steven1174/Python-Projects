# Creando un Iterador
my_list = range(1,11)
my_iter = iter(my_list)

# Iterando un iterador
def run():
    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

if __name__ == "__main__":
    run()


