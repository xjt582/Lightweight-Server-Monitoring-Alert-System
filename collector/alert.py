from datetime import datetime

CPU_THRESHOLD = 3
MEM_THRESHOLD = 85
DISK_THRESHOLD = 90

def check_alert(cpu, mem, disk):
    alerts = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cpu > CPU_THRESHOLD:
        alerts.append({
            "type": "CPU",
            "msg": f"[{now}] CPU 使用率过高: {cpu}%",
            "value": cpu
        })

    if mem > MEM_THRESHOLD:
        alerts.append({
            "type": "MEM",
            "msg": f"[{now}] 内存使用率过高: {mem}%",
            "value": mem
        })

    if disk > DISK_THRESHOLD:
        alerts.append({
            "type": "DISK",
            "msg": f"[{now}] 磁盘使用率过高: {disk}%",
            "value": disk
        })

    return alerts

