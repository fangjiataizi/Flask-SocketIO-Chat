from flask import Flask, request, render_template
from llm_caipu import Role,call_with_prompt,simple_call


def generate_response(user_input):
    user_input = user_input.strip()
    text_prompt= "你是一个菜谱专家，为用户提供专业菜谱，现在用户的食材及相关要求是:{},请返回符合用户要求的菜谱，注意除了菜谱内容，不要返回其它内容".format(user_input)
    print(text_prompt)
    response=call_with_prompt(text_prompt)
    pic_name=simple_call(response)
    print(pic_name)
    return response,pic_name



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_caipu.html')

@app.route('/generate_recipe', methods=['GET'])
def generate_recipe():
    # 获取用户输入的食材
    ingredients = request.args.get('ingredients')
    print("用户输入是：", ingredients)
    # 生成菜谱文本和图片
    recipe_text, recipe_image = generate_response(ingredients)  # 这是您自己的函数
    # 返回一个包含菜谱文本和图片的HTML页面
    return render_template('recipe.html', text=recipe_text, image=recipe_image)





if __name__ == "__main__":
    app.run(port=5005,host='0.0.0.0')
