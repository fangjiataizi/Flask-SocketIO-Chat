from flask import Flask, request, render_template
from llm import init_message,Role,get_response


def generate_response(user_input):
    messages.append({'role': Role.USER, 'content': user_input}) # 将用户输入添加到messages中
    response = get_response(user_input, messages) # 调用模型得到回复
    return response



app = Flask(__name__)

messages = []
@app.route('/')
def home():
    messages=init_message()
    return render_template('home.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    # 在这里添加你的模型代码，将userText作为输入，得到botResponse
    botResponse = generate_response(userText)
    print(messages)
    # botResponse = "这是模型的响应"  # 这只是一个示例，你需要将其替换为你的模型的响应
    return botResponse

if __name__ == "__main__":
    app.run()
