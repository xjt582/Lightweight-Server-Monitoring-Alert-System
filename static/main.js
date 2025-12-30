fetch("/metrics")
    .then(response => response.json())
    .then(data => {
        console.log("后端返回的数据：", data);

        const div = document.getElementById("data");
        let html = "";

        data.forEach(item => {
            html += `
                <p>
                    时间：${item.created_at}<br>
                    CPU：${item.cpu_usage}%<br>
                    内存：${item.mem_usage}%<br>
                    磁盘：${item.disk_usage}%
                </p>
                <hr>
            `;
        });

        div.innerHTML = html;
    })
    .catch(err => {
        console.error(err);
        document.getElementById("data").innerText = "加载失败";
    });

