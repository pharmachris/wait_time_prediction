document.getElementById('prediction-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const checkInOrder = document.getElementById('check-in-order').value;

    const response = await fetch('https://your-username-wait-time-prediction.hf.space/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ check_in_order: checkInOrder })
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.prediction;
});
