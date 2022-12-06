def make_repeater_of(n):
    
    def repeat(string):
        assert type(string) == str, "Solo se aceptan cadenas"
        return string*n
    return repeat

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola "))

if __name__ == "__main__":
    run() 