# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-07-29 16:17
# software: PyCharm

from fontTools.ttLib import TTFont
from os import remove
import re, requests, time
import numpy as np

# 存放已经解析好的 猫眼数字和font name对应字典
offline_dict = {
    "uniE3ED": '6',
    "uniEEF2": '7',
    "uniEF24": '9',
    "uniF5C8": '8',
    "uniE517": '0',
    "uniE104": '2',
    "uniEF3D": '3',
    "uniE6BE": '1',
    "uniE46C": '5',
    "uniF52F": '4'
}

# 存放新的 font name对应字典
online_dict = {}


def getAxis(font):
    '''font:用TTFont解析woff后的结果
        :return:存放所有font的坐标'''
    font_name_list = font.getGlyphOrder()[2:]  # 前两位无效，返回font name
    fonts_axis = []
    for name in font_name_list:
        font_axis = []
        for axis in font['glyf'][name].coordinates:  # 遍历某个name的所有坐标
            font_axis.append(axis)
        fonts_axis.append(font_axis)
    return fonts_axis, font_name_list


def downOnlineFont(url):
    '''url:传入woff字体的url即可'''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    file_name = r'./online_font_file/' + str(int(time.time())) + '.woff'
    with open(r'{}'.format(file_name), 'wb') as f:
        f.write(response.content)
    return file_name


def getMaoyanWoffUrl(url):
    ''' on fit maoyan,in other website you should alter this function'''
    headers = {
        'Host':'maoyan.com',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/84.0.4147.89Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).text
    font_url = 'http:' + re.search(r"url\('(.*\.woff)'\)", response).group(1)
    movies_name_list_pattern = re.compile(r'title="(.*?)"')
    movies_name_list = movies_name_list_pattern.findall(response)
    movies_boxoffice_list_pattern = re.compile(r'class="stonefont">(.*?)</span>')
    movies_boxoffice_list = movies_boxoffice_list_pattern.findall(response)
    movies_danwei_list_pattern = re.compile(r'</span></span>(.)')
    movies_danwei_list = movies_danwei_list_pattern.findall(response)
    # print(movies_danwei_list)
    # print(font_url)
    # print(movies_name_list)
    # print(movies_boxoffice_list)
    return font_url, movies_name_list, movies_boxoffice_list, movies_danwei_list


def compare_axis(font_axis1, font_axis2):
    ''' use Euclidean Distance to compare two font_axis`s similaiity '''
    if len(font_axis1) < len(font_axis2):
        font_axis1.extend([(0, 0) for num in range(len(font_axis2) - len(font_axis1))])
    elif len(font_axis1) > len(font_axis2):
        font_axis2.extend([(0, 0) for num in range(len(font_axis1) - len(font_axis2))])
    font_axis1 = np.array(font_axis1)
    font_axis2 = np.array(font_axis2)
    return np.sqrt(np.sum(np.square(font_axis1 - font_axis2)))


def parseOnlineFont(online_font, offline_font):
    '''
    1. 解析 onlinefont 和 offlinefont 的 fonts_axis 和name_list
    2. 遍历 onlinefont 的 name_list 月 font_axis 与 offlinefont 的 fonts_axis 进行计数遍历比较
    3. 以最相似的 offlinefont 的 num 取出 name，再取出name的value 值， 以onlinefont的name为key写入新的dict
    '''
    online_fonts_axis, online_font_name_list = getAxis(online_font)
    offline_fonts_axis, offline_font_name_list = getAxis(offline_font)
    for online_font_name, online_font_axis in zip(online_font_name_list, online_fonts_axis):
        similarity_list = []
        for num in range(len(offline_font_name_list)):
            similarity_list.append(compare_axis(online_font_axis, offline_fonts_axis[num]))
        similarity_array = np.array(similarity_list)
        index = similarity_array.argmin()
        online_dict[online_font_name] = offline_dict[offline_font_name_list[index]]


def run():
    '''
    finish the all logic in maoyan spider
    '''
    font_url, movies_name_list, movies_boxoffice_list, movies_danwei_list = getMaoyanWoffUrl(url='https://maoyan.com/board/1')
    file_name = downOnlineFont(url=font_url)
    offline_font = TTFont('2c59abfa3b184d16183ee2609a46d5342268.woff')
    online_font = TTFont(file_name)
    parseOnlineFont(online_font, offline_font)
    print(online_dict)
    for name in online_dict :
        new_name = (name.replace('uni','&#x')).lower()
        for num in range(len(movies_boxoffice_list)) :
            movies_boxoffice_list[num] = movies_boxoffice_list[num].replace(new_name,online_dict[name]).replace(';','')
    for i in range(0,len(movies_name_list),2):
        print(f'{movies_name_list[i]}的 时时票房：{movies_boxoffice_list[i]}{movies_danwei_list[i]} ，总票房：{movies_boxoffice_list[i+1]}{movies_danwei_list[i+1]}')

if __name__ == '__main__':
    run()
    # offline_font = TTFont('2c59abfa3b184d16183ee2609a46d5342268.woff')
    # online_font = TTFont('bcddc6efbdbdd8ca70585478eba2535a2264.woff')
    # parseOnlineFont(online_font, offline_font)
    # print(online_dict)

