from collect_metrics import collect_metrics
from save_to_mysql import save_to_mysql
from alert import check_alert
from save_alert import save_alert

def main():
    cpu, mem, disk = collect_metrics()

    # 1. 保存指标
    save_to_mysql(cpu, mem, disk)

    # 2. 检查告警
    alerts = check_alert(cpu, mem, disk)

    # 3. 告警写入数据库
    for alert in alerts:
        save_alert(
            alert["type"],
            alert["msg"],
            alert["value"]
        )
        print("告警已记录：", alert["msg"])

if __name__ == "__main__":
    main()

