import threading
import time


def download_data():
    print("Starting data download...")
    time.sleep(2)
    print("Data download completed.")


def process_data():
    print("Starting data processing...")
    time.sleep(3)
    print("Data processing completed.")


# 创建线程
download_thread = threading.Thread(target=download_data)
process_thread = threading.Thread(target=process_data)

# 启动线程
download_thread.start()
process_thread.start()

# 等待线程完成
download_thread.join()
process_thread.join()

print("Both tasks completed.")
