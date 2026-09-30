import psutil
import os
import time

def show_stats():
    print("*"*30)
    print("System Resource Monitor")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"CPU : {cpu}%")
    print(f"RAM : {ram.used}% ( {round(ram.used / 1e9, 2)} GB used of {round(ram.total / 1e9, 2)} GB)")
    print(f"Disk: {disk.used}% ( {round(disk.used / 1e9, 2)} GB used of {round(disk.total / 1e9, 2)} GB)")
    print("*"*30)

if __name__ == '__main__':
    try:
        while True:
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Exit the program")