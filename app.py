from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 内存列表
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. 获取昵称和内容
        nickname = request.form.get('nickname')
        content = request.form.get('content')
        
        # 只有两个都填了才处理
        if nickname and content:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            
            # --- 控制台打印日志 ---
            print(f"[{current_time}] 用户[{nickname}] 发送了: {content}")
            
            # 2. 存入字典，新增 name 字段
            messages.insert(0, {
                'name': nickname,
                'text': content,
                'time': current_time
            })
            
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    print("--- 留言板已启动 ---")
    app.run(host='0.0.0.0', port=5000, debug=False)