import requests
from requests_toolbelt import MultipartEncoder
import re
import random


with open(r'./cookie.txt', mode='r', encoding='utf-8') as f:
    cookie = f.read()
    print(cookie)

def generate_random_str(randomlength=8):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def get_pic_url(file_path):
    post_url = 'https://s.taobao.com/image'
    headers = {
        'Host': 's.taobao.com',
        'Connection': 'keep-alive',
        'Content-Length': '5095',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"GoogleChrome";v="89","Chromium";v="89",";NotABrand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://www.taobao.com',
        # 'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundaryM9jGHaaEhi1xCuO8',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.82Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'iframe',
        'Referer': 'https://www.taobao.com/',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie,
    }
    if '.png' in file_path:
        type = 'image/png'
        file_name = generate_random_str() + '.png'
    else:
        type = 'image/jpg'
        file_name = generate_random_str() + '.jpg'

    print(file_name)
    multipart_encoder = MultipartEncoder(
        fields={  # 这里根据需要进行参数格式设置
            'cross': 'taobao', 'type': 'iframe', 'imgfile': (file_name, open(file_path, 'rb'), type)
        })
    headers['Content-Type'] = multipart_encoder.content_type
    print(headers['Content-Type'])
    r = requests.post(post_url, data=multipart_encoder, headers=headers)
    print(r.text)
    url_pattern = re.compile(r'"url":"(.*?)"')
    pic_url = url_pattern.findall(r.text)
    pic_url2 = 'http:' + pic_url[0]
    print(pic_url2)
    return pic_url2


if __name__ == '__main__':
    get_pic_url(r'C:\Users\Z\Desktop\QQ截图20210314192432.png')
