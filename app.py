import gradio as gr
import lightgbm as lgb
import joblib
import datetime

# 載入模型和 LabelEncoder
model = lgb.Booster(model_file='wait_time_lgbm_model.txt')
time_slot_encoder = joblib.load('time_slot_label_encoder.pkl')
room_code_encoder = joblib.load('room_code_label_encoder.pkl')
department_name_encoder = joblib.load('department_name_label_encoder.pkl')

# 預測函式
def predict_wait_time(check_in_order, date, time_slot, room_code, department_name):
    try:
        # 將日期轉換為星期（0 表示星期日，1 表示星期一...）
        weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        
        # 使用 LabelEncoder 將輸入轉換為模型需要的數值
        time_slot_encoded = time_slot_encoder.transform([time_slot])[0]
        room_code_encoded = room_code_encoder.transform([room_code])[0]
        department_name_encoded = department_name_encoder.transform([department_name])[0]

        # 模型需要的特徵
        features = [
            weekday,
            check_in_order,
            time_slot_encoded,
            room_code_encoded,
            department_name_encoded
        ]

        # 預測等待時間
        wait_time = model.predict([features])[0]

        return f"預測的等待時間為：{round(wait_time, 2)} 分鐘"
    except Exception as e:
        return f"發生錯誤：{str(e)}"

# 建立 Gradio 介面
with gr.Blocks() as demo:
    gr.Markdown("# 看診等待時間預測")
    
    with gr.Row():
        check_in_order_input = gr.Number(label="輸入您的看診序號", value=1)
        date_input = gr.Textbox(label="輸入日期 (YYYY-MM-DD)", value=datetime.date.today().strftime('%Y-%m-%d'))
        time_slot_input = gr.Textbox(label="輸入時段", placeholder="例如：上午")
        room_code_input = gr.Textbox(label="輸入診間代碼", placeholder="例如：A101")
        department_name_input = gr.Textbox(label="輸入科別名稱", placeholder="例如：內科")
    
    predict_button = gr.Button("預測等待時間")
    output = gr.Textbox(label="預測結果")

    predict_button.click(
        predict_wait_time,
        inputs=[check_in_order_input, date_input, time_slot_input, room_code_input, department_name_input],
        outputs=output
    )

# 啟動 Gradio 應用程式
if __name__ == "__main__":
    demo.launch()
