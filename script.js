// 等待網頁載入完成後執行
document.addEventListener('DOMContentLoaded', () => {
    // 設定日期欄位的預設值為今天
    const dateInput = document.getElementById('date');
    const today = new Date().toISOString().split('T')[0]; // 格式化為 YYYY-MM-DD
    dateInput.value = today;

    // 綁定表單提交事件
    document.getElementById('prediction-form').addEventListener('submit', async (event) => {
        event.preventDefault(); // 防止頁面重新載入

        // 獲取使用者輸入
        const checkInOrder = document.getElementById('check-in-order').value;
        const date = document.getElementById('date').value;
        const timeSlot = document.getElementById('time-slot').value;
        const roomCode = document.getElementById('room-code').value;
        const departmentName = document.getElementById('department-name').value;

        // 發送請求到 Hugging Face API
        try {
            const response = await fetch('https://your-username-wait-time-prediction.hf.space/api', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    check_in_order: checkInOrder,
                    date: date,
                    time_slot: timeSlot,
                    room_code: roomCode,
                    department_name: departmentName
                })
            });

            // 處理 API 回應
            const result = await response.json();
            document.getElementById('result').innerText = result.prediction;
        } catch (error) {
            document.getElementById('result').innerText = `發生錯誤：${error.message}`;
        }
    });
});
