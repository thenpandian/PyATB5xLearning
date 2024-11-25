import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by func ->", end_time - start_time)
    return wrapper


def print_logs(func):
    def wrapper():
        print("Starting Log")
        func()
        print("Ending Log")
    return wrapper


@time_decorator
@print_logs
def test_UI_1():
    print("Add a function, time taken by this function")
    time.sleep(2)


test_UI_1()

@time_decorator
@print_logs
def test_UI_2():
    print("Add a function, time taken by this function")
    time.sleep(5)

test_UI_2() 