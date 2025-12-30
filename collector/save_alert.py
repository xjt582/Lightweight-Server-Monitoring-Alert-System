import pymysql

def save_alert(alert_type, alert_msg, metric_value):
    conn = pymysql.connect(
        host='localhost',
        user='monitor',
        password='monitor123',
        database='monitor_db'
    )

    cursor = conn.cursor()

    sql = """
    INSERT INTO alert_logs (alert_type, alert_msg, metric_value)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (alert_type, alert_msg, metric_value))
    conn.commit()

    cursor.close()
    conn.close()

