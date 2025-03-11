document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("https://your-huggingface-space-url/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("result").innerHTML = `預測等待時間為：${result.prediction} 秒`;
    } catch (error) {
        document.getElementById("result").innerHTML = "發生錯誤，請稍後重試。";
    }
});
