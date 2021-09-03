# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-02-13 16:01
# software: PyCharm
import sys
import requests

def download(url, file_path):
    # verify=False 这一句是为了有的网站证书问题，为True会报错
    r = requests.get(url, stream=True)

    # 既然要实现下载进度，那就要知道你文件大小，下面这句就是得到总大小
    total_size = int(r.headers['Content-Length'])
    temp_size = 0

    with open(file_path, "wb") as f:
        # iter_content()函数就是得到文件的内容，
        # 有些人下载文件很大怎么办，内存都装不下怎么办？
        # 那就要指定chunk_size=1024，大小自己设置，
        # 意思是下载一点写一点到磁盘。
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                #############花哨的下载进度部分###############
                done = int(50 * temp_size / total_size)
                # 调用标准输出刷新命令行，看到\r回车符了吧
                # 相当于把每一行重新刷新一遍
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()  # 避免上面\r 回车符，执行完后需要换行了，不然都在一行显示

if __name__ == '__main__':

    file_url = 'http://tyst.migu.cn/public/product5th/product34/2019/07/1822/2009%E5%B9%B406%E6%9C%8826%E6%97%A5%E5%8D%9A%E5%B0%94%E6%99%AE%E6%96%AF/%E6%A0%87%E6%B8%85%E9%AB%98%E6%B8%85/MP3_320_16_Stero/60054701923.mp3'  # 文件链接
    file_path = "xxx.mp3"  # 文件路径
    # 调用上面下载函数即可
    download(file_url,file_path)
