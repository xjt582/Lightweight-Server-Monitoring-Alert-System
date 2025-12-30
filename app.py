from flask import Flask, jsonify, render_template
import pymysql

app = Flask(__name__)

def get_db_conn():
    return pymysql.connect(
        host='localhost',
        user='monitor',
        password='monitor123',
        database='monitor_db',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    conn = get_db_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT cpu_usage, mem_usage, disk_usage, created_at
        FROM system_metrics
        ORDER BY created_at DESC
        LIMIT 10
    """)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)


# ✅ 新增：告警接口
@app.route("/alerts")
def alerts():
    conn = get_db_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT alert_type, alert_msg, metric_value, created_at
        FROM alert_logs
        ORDER BY created_at DESC
        LIMIT 10
    """)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

