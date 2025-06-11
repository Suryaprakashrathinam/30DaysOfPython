import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function '{func.__name__}' executed in {(end - start)*1000} seconds")
        return result

    return wrapper


@log_execution_time
def factorial(n):
    def inner_fact(n):
        if n == 0 or n == 1:
            return 1
        return n * inner_fact(n - 1)

    return inner_fact(n)


print(factorial(10))
