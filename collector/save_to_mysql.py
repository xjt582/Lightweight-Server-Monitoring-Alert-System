import pymysql
from datetime import datetime

def save_to_mysql(cpu, mem, disk):
    now = datetime.now()

    conn = pymysql.connect(
        host='localhost',
        user='monitor',
        password='monitor123',
        database='monitor_db'
    )

    cursor = conn.cursor()

    sql = """
    INSERT INTO system_metrics (cpu_usage, mem_usage, disk_usage, created_at)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (cpu, mem, disk, now))
    conn.commit()

    cursor.close()
    conn.close()

