Flask==2.3.3
pymysql==1.1.0
psutil==5.9.8
🖥️ Lightweight Server Monitoring & Alert System

一个基于 Python + Flask + MySQL + ECharts 的轻量级服务器性能监控与告警系统，用于实时采集服务器 CPU / 内存 / 磁盘使用率，并通过 Web 看板进行可视化展示，同时支持阈值告警。

适合：Linux 运维 / 初级 DevOps / Python 自动化方向展示项目

📌 项目功能

✅ 实时采集服务器性能指标

CPU 使用率

内存使用率

磁盘使用率

✅ 数据持久化存储到 MySQL

✅ Web API 提供监控数据（Flask）

✅ ECharts 构建可视化监控看板

✅ 支持阈值告警（CPU / 内存 / 磁盘）

✅ 定时任务（crontab）自动采集数据

🧱 技术栈
模块	技术
后端	Python 3
Web 框架	Flask
数据库	MySQL
数据采集	psutil
数据可视化	ECharts
定时任务	crontab
数据交互	REST API（JSON）
📂 项目结构
monitor/
├── app.py                  # Flask Web 服务
├── requirements.txt        # Python 依赖清单
├── templates/
│   └── index.html          # 监控看板页面（ECharts）
├── collector/
│   ├── collect_metrics.py  # 性能指标采集
│   ├── save_to_mysql.py    # 数据写入 MySQL
│   ├── alert.py            # 告警逻辑
│   └── run_collector.py    # 采集主入口（供 crontab 调用）
└── README.md

⚙️ 环境要求

Python 3.8+

MySQL 8.x

Linux / 虚拟机 / 云服务器（推荐 Ubuntu）

📦 安装依赖

建议使用 虚拟环境：

python3 -m venv venv
source venv/bin/activate


安装依赖：

pip install -r requirements.txt

🗄️ MySQL 数据库初始化
1️⃣ 创建数据库
CREATE DATABASE monitor_db DEFAULT CHARSET utf8mb4;

2️⃣ 创建用户并授权
CREATE USER 'monitor'@'localhost' IDENTIFIED BY 'monitor123';
GRANT ALL PRIVILEGES ON monitor_db.* TO 'monitor'@'localhost';
FLUSH PRIVILEGES;

3️⃣ 创建数据表
系统指标表
CREATE TABLE system_metrics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cpu_usage FLOAT NOT NULL,
    mem_usage FLOAT NOT NULL,
    disk_usage FLOAT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

告警记录表（可选）
CREATE TABLE alert_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    alert_type VARCHAR(20),
    alert_msg VARCHAR(255),
    metric_value FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

▶️ 启动项目
1️⃣ 启动采集程序（测试）
python collector/run_collector.py

2️⃣ 配置定时采集（每分钟）
crontab -e


添加：

* * * * * /home/tt/monitor/venv/bin/python /home/tt/monitor/collector/run_collector.py

3️⃣ 启动 Web 服务
python app.py


访问浏览器：

http://127.0.0.1:5000/

📊 监控看板效果

折线图实时展示 CPU / 内存 / 磁盘使用率

数据来源：Flask API /metrics

前端：ECharts 动态渲染

🚨 告警机制说明

在 collector/alert.py 中可配置告警阈值：

CPU_THRESHOLD = 50
MEM_THRESHOLD = 85
DISK_THRESHOLD = 90


当指标超过阈值时：

控制台输出告警信息

可扩展为写入数据库 / 邮件 / Webhook 通知
📈 项目亮点

✔ 从 系统层（psutil）→ 数据层（MySQL）→ Web 层（Flask）→ 可视化层（ECharts） 的完整链路

✔ 使用 crontab 实现自动化采集

✔ 前后端分离，REST API 设计

✔ 可扩展性强（告警、用户、权限、Docker）

🚀 可扩展方向

 告警信息写入数据库并在页面展示

 接入邮件 / 企业微信 / Telegram 告警

 Docker Compose 一键部署

 多服务器节点监控

 WebSocket 实时刷新

👤 作者

xjt582
方向：Linux 运维 / Python 自动化 / DevOps
GitHub：https://github.com/xjt582
