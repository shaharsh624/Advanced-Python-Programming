import threading
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_primes(start, end):
    sum_result = 0
    for num in range(start, end + 1):
        if is_prime(num):
            sum_result += num
    return sum_result


def threaded_sum_primes(start, end, result):
    result[0] = sum_primes(start, end)


if __name__ == "__main__":
    start_time = time.time()

    result = [0]
    threads = []

    for i in range(4):
        thread_start = i * 250000 + 2
        thread_end = (i + 1) * 250000 if i != 3 else 500000
        thread = threading.Thread(
            target=threaded_sum_primes, args=(thread_start, thread_end, result)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(f"Sum of prime numbers from 2 to 1 million: {result[0]}")
    print(f"Time taken: {end_time - start_time} seconds")
