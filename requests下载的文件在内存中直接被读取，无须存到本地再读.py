# author: ZhaoKun
# contact: 1161678627@qq.com
# datetime: 2020-11-06 15:47
# software: PyCharm

import requests
from fontTools.ttLib import TTFont
import re
import base64
import io

rank_list = []


def get_page(page_num):
    url = 'http://match.yuanrenxue.com/api/match/7?page={}'.format(page_num)
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'http://match.yuanrenxue.com/match/6',
    }
    if page_num > 3:
        headers['User-Agent'] = 'yuanrenxue.project'
    response = requests.get(url=url, headers=headers)
    # print(response.json())
    woff_data = response.json()['woff']
    font_bytes = download_woff(woff_data)
    value_data = response.json()['data']
    value_data = [__['value'].replace('&#x', '').replace(' ', '') for __ in value_data]
    return value_data, font_bytes


def download_woff(woff_data):
    font_data = base64.b64decode(woff_data)
    font_bytes = io.BytesIO(font_data)
    return font_bytes


def parse_online_woff_data(font_bytes):
    online_font = TTFont(font_bytes)
    # online_font.saveXML('./online_font.xml')
    extraNames = str(online_font.getTableData('post') + b'\0x2')
    # print(extraNames)
    number_pattern = re.compile(r'uni(.*?)\\x0')
    number_value = number_pattern.findall(extraNames)
    return number_value


def parse_real_data(value_data, number_value):
    print(value_data)
    print(number_value)
    new_number_value = [number_value[9]]
    new_number_value.extend(number_value[0:9])
    print(new_number_value)
    number_dict = {new_number_value[i]: i for i in range(10)}
    print(number_dict)
    for numbers in value_data:
        rank_list.append(int(''.join([str(__) for __ in [number_dict[numbers[index * 4: (index + 1) * 4]] for index in
                                                         range(int(len(numbers) / 4))]])))


if __name__ == '__main__':
    for page_num in range(1, 6):
        value_data, font_bytes = get_page(page_num)
        number_value = parse_online_woff_data(font_bytes)
        parse_real_data(value_data, number_value)
    print(rank_list)
    max_rank_point = max(rank_list)
    print('当前最高的rank分数为：{}'.format(max_rank_point), '他的位置在{}'.format(rank_list.index(max_rank_point) + 1) + '位')
