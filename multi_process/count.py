from multiprocessing import Process, Value, Lock
import time


def increment(counter, lock):
    for _ in range(100000):
        with lock:  # 使用锁来保护共享数据
            counter.value += 1  # 无锁操作，确保原子性


if __name__ == '__main__':
    counter = Value('i', 0)  # 共享资源
    lock = Lock()  # 创建锁

    # 创建进程
    process1 = Process(target=increment, args=(counter, lock))
    process2 = Process(target=increment, args=(counter, lock))

    # 记录开始时间
    start_time = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    # 记录结束时间
    end_time = time.time()

    print(f"Final counter value: {counter.value}")
    print(
        f"Execution time with multiprocessing: {end_time - start_time} seconds")
