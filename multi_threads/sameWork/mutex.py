import threading
import time

# 共享资源
counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        lock.acquire()  # 获取锁
        try:
            counter += 1
        finally:
            lock.release()  # 释放锁


# 创建线程
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# 记录开始时间
start_time = time.time()

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

# 记录结束时间
end_time = time.time()

print(f"Final counter value: {counter}")
print(f"Execution time with concurrency: {end_time - start_time} seconds")
