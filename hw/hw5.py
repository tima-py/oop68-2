import time

def timer(func):
    def wrapper(*args, **kwargs):
        t_start = time.perf_counter()
        result_f = func(*args, **kwargs)
        print(f'Функция calculate_sum работала {round(time.perf_counter() - t_start, 2)} секунды')
        return result_f

    return wrapper

@timer
def calculate_sum(n):
    return sum(range(n))


result = calculate_sum(1_000_000)

print(result)
