import psutil
import time

def collect_metrics():
    # 获取 CPU 使用率，interval=1 表示 1 秒内平均值
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("===== System Metrics =====")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("==========================")

if __name__ == "__main__":
    collect_metrics()
