from multiprocessing import Pool, cpu_count
import time

def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        factors = pool.map(factorize_sync, numbers)
    return factors

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def test_factorize():
    numbers = [128, 255, 99999, 10651060]
    result, execution_time = measure_time(factorize_parallel, numbers)

    a, b, c, d = result

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    test_factorize()
