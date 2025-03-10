import gradio as gr
import lightgbm as lgb
import joblib
import datetime

# 載入模型和 LabelEncoder
model = lgb.Booster(model_file='wait_time_lgbm_model.txt')  # 替換為您的模型檔案名稱

# 預測函式
def predict_wait_time(check_in_order, date):
    try:
        # 將日期轉換為星期（0 表示星期日，1 表示星期一...）
        weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()

        # 模型需要的特徵
        features = [weekday, check_in_order]

        # 預測
        wait_time = model.predict([features])[0]  # 模型返回的預測值

        return f"預測的等待時間為：{round(wait_time, 2)} 分鐘"
    except Exception as e:
        return f"發生錯誤：{str(e)}"

# 建立 Gradio 介面
with gr.Blocks() as demo:
    gr.Markdown("# 看診等待時間預測")
    
    with gr.Row():
        check_in_order_input = gr.Number(label="輸入您的看診序號", value=1)
        date_input = gr.Textbox(label="輸入日期 (YYYY-MM-DD)", value=datetime.date.today().strftime('%Y-%m-%d'))
    
    predict_button = gr.Button("預測等待時間")
    output = gr.Textbox(label="預測結果")

    predict_button.click(
        predict_wait_time,
        inputs=[check_in_order_input, date_input],
        outputs=output
    )

# 啟動 Gradio 應用程式
if __name__ == "__main__":
    demo.launch()
