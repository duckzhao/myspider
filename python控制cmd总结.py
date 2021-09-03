# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-07-24 15:24
# software: PyCharm

import os


# 传入要在cmd执行的命令即可，缺点返回值 仅为 0 / 1 ，表示执行成功与否，无法获取cmd展示的结果（但该结果可在console屏幕展示）---如乱码需将pycharm编码改为gbk
# os.system('cd /usr/local ; mkdir newdir')   多条命令间用 ; 分号隔开
def run_cmd_command(command):
    check_state = os.system(command)
    return check_state


def get_cmd_print(command):
    with os.popen(r'{}'.format(command), 'r') as f:
        text = f.read().splitlines()  # 按行转为list
    return text


if __name__ == '__main__':
    state = run_cmd_command('chrome.exe')  # state = 0 ，无输出结果
    state = run_cmd_command('ipconfig')  # state = 0 ，输出结果乱码
    print(state)
    # text = get_cmd_print('chrome.exe')  # 返回 空字符串
    # text = get_cmd_print('ipconfig')
    # print(text)
