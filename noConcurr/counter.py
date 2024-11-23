import time


def no_concurrency_sum():
    counter = 100000
    for _ in range(100000000):
        try:
            counter += 1
        except Exception as e:
            print(f"An error occurred: {e}")
    return counter


start_time = time.time()
total_sum_no_concurrency = no_concurrency_sum()
end_time = time.time()

print(f"Result without concurrency: {total_sum_no_concurrency}")
print(f"Execution time without concurrency: {end_time - start_time} seconds")
