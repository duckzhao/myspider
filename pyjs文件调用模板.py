# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-01-18 17:11
# software: PyCharm

import execjs
import os

# 导入js,读取保存的js文件，指定utf-8格式保险起见。
with open(r'migu01.js', encoding='utf-8', mode='r') as f:
    JsData = f.read()
# 加载js文件，使用call执行,call中有几个参数，首先明确需要执行的函数。随后附加该函数的参数,依次传入即可
psd = execjs.compile(JsData).call('getdata', '123456')
print(psd)
