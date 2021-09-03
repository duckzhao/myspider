# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-07-20 19:12
# software: PyCharm

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

def getb64RSA(text, pubkey):
    '''
    :param text : 采用str传入即可
    :param pubkey: 采用多行字符串赋值即可，但是要分为带pem格式的和不带pem格式的两种调用方式
    :return: b64编码后的加密结果
    '''
    # 判断下是否为标准pem格式的文件
    if 'BEGIN PUBLIC KEY' not in pubkey :
        pubkey = processpubkey(pubkey)
    # 导入公钥
    rsakey = RSA.importKey(pubkey)
    # 实例化加密对象
    cipher = PKCS1_v1_5.new(rsakey)
    # 进行加密，需要将str的加密数据转为bytes类型
    encrypt_result = cipher.encrypt(text.encode(encoding = 'utf-8'))
    # 加密的结果也是bytes，转为b64,再转为str
    encrypt_result = str(base64.b64encode(encrypt_result),encoding='utf-8')
    print(encrypt_result)
    return encrypt_result

# 处理方案先用64取余再整取
def processpubkey(pubkey):
    beginstr = '-----BEGIN PUBLIC KEY-----' + '\n'
    endstr = '-----END PUBLIC KEY-----'
    num = int(len(pubkey)/64)
    mod = len(pubkey)%64
    str_list = [pubkey[64*i :64*(i+1)] + '\n' for i in range(num)]
    laststr = pubkey[mod*(-1):] + '\n'
    newpubkey = ''
    for str in str_list :
        newpubkey += str
    pubkey = beginstr + newpubkey + laststr + endstr
    return pubkey

if __name__ == '__main__':
    # 不带pem传入案例,传入一整行，长度默认216
    pubkey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5GVku07yXCndaMS1evPIPyWwhbdWMVRqL4qg4OsKbzyTGmV4YkG8H0hwwrFLuPhqC5tL136aaizuL/lN5DRRbePct6syILOLLCBJ5J5rQyGr00l1zQvdNKYp4tT5EFlqw8tlPkibcsd5Ecc8sTYa77HxNeIa6DRuObC5H9t85ALJyDVZC3Y4ES/u61Q7LDnB3kG9MnXJsJiQxm1pLkE7Zfxy29d5JaXbbfwhCDSjE4+dUQoq2MVIt2qVjZSo5Hd/bAFGU1Lmc7GkFeLiLjNTOfECF52ms/dks92Wx/glfRuK4h/fcxtGB4Q2VXu5k68e/2uojs6jnFsMKVe+FVUDkQIDAQAB'
    # 带pem传入案例，不限长度
#     pubkey = '''-----BEGIN PUBLIC KEY-----
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5lalja
# N9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7P
# AzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQ
# q+CA6agNkqly2H4j6wIDAQAB
# -----END PUBLIC KEY-----'''
    getb64RSA('12354468486465',pubkey)
