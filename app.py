from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 内存列表，用于临时存储留言
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取前端表单发来的数据
        content = request.form.get('content')
        
        if content:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            
            # --- 核心功能：在 SSH 控制台打印留言 ---
            # 截图时，这里显示的内容就是证据
            print(f"[{current_time}] 收到一条新留言: {content}")
            
            # 将留言存入列表，插到最前面
            messages.insert(0, {'text': content, 'time': current_time})
            
    # Flask 会自动去 templates 文件夹里找 index.html
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    print("--- 系统启动成功 ---")
    print("正在监听端口 5000...")
    # debug=True 可以在报错时显示具体原因，方便调试
    app.run(host='0.0.0.0', port=5000, debug=True)