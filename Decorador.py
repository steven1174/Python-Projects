from datetime import datetime

def execution_time(func):
    
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time

        print("Pasaron " + str(time_elapse.total_seconds()) + " segundos")

    return wrapper

@execution_time
def random_func():

    for _ in range(1,1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b 

# random_func()


