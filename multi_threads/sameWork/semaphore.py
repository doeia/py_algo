import threading
import time

# 创建信号量，允许最多 3 个线程同时运行
semaphore = threading.Semaphore(3)


def worker(thread_id):
    with semaphore:  # 自动 acquire 和 release
        print(f"Thread-{thread_id} is running...")
        time.sleep(2)  # 模拟任务
        print(f"Thread-{thread_id} is done!")


# 创建 5 个线程
threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]

# 启动线程
for t in threads:
    t.start()

# 等待线程完成
for t in threads:
    t.join()
