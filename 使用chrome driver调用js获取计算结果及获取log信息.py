# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-07-17 20:52
# software: PyCharm

from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getjscode(path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='chromedriver.exe')
    with open(path, mode='r',encoding='utf-8') as f:
        js = f.read()
    # js 为一个str，可以使用代码增加最后会变化的调用和输出的两行
    js = js + '''
    return (getdata('{"copyrightId":"600541478","type":1,"auditionsFlag":0}'));
    '''
    jscode = driver.execute_script(js)
    # driver.close()
    return jscode

def getlogjs(path):
    chrome_options = Options()
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    # driver = webdriver.Chrome(desired_capabilities=d)
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe',desired_capabilities=d)
    with open(path, mode='r') as f:
        # js 为一个str，可以使用代码增加最后会变化的调用和输出的两行
        js = f.read()
    # print(js)
    driver.execute_script(js)
    jscode = driver.get_log('browser')[0]
    return jscode

if __name__ == '__main__':
    path = 'migu01.js'
    jscode = getjscode(path)
    print(jscode)

    path = 'printlog.js'
    jscodo = getlogjs(path)
    print(jscodo)