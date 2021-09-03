import MySQLdb
from flask import Flask, request, jsonify
from main import run_2, run_3
import time
import json
from urllib.parse import unquote
# from cookie import cookie

app = Flask(__name__)


@app.route("/", methods=['POST'])
def run():
    # print(request.data)
    # 校验数据是否空
    if not request.data:
        return 'sorry, not get the post data.'

    # 获取前端post传入参数
    ori_data = request.data.decode('utf-8')
    json_data = json.loads(ori_data)

    # 校验关键字
    keyword = json_data.get('key')
    if not keyword:
        return 'sorry, please enter isbn number.'
    # 安全效验
    code = json_data.get('code')  # 校验码
    if code != 'password':
        return 'sorry, error requests!'

    # error_cookie = json_data.get('tbcookie')  # 淘宝cookie
    # if not cookie:
    #     return 'sorry, please enter taobao cookie.'
    # cookie = unquote(cookie).replace('+', ' ')

    print('this request time: {} '.format(int(time.time())), keyword, code)

    # 数据请求
    # try:
    #     final_data = run_2(keyword=keyword, cookie=cookie)
    # except:
    #     return 'requests error!'
    final_data = run_2(keyword=keyword, cookie='')

    # 执行数据库数据插入
    run_3(final_data, keyword)
    return 'true'

if __name__ == '__main__':
    # 请在此处定义您的校验码
    SAFETY_CODE = 'password'
    # host
    host = '0.0.0.0'
    # port
    port = 5001
    app.run(host=host, port=port)
