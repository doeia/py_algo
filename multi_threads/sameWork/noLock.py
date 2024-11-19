from multiprocessing import Process, Value


def increment(counter):
    for _ in range(100000):
        counter.value += 1  # 无锁操作


if __name__ == '__main__':
    # 使用 Value 来共享数据
    counter = Value('i', 0)

    # 创建进程
    process1 = Process(target=increment, args=(counter,))
    process2 = Process(target=increment, args=(counter,))

    # 启动进程
    process1.start()
    process2.start()

    # 等待进程完成
    process1.join()
    process2.join()

    print(f"Final counter value: {counter.value}")
