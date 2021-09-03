# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2020-07-20 20:43
# software: PyCharm
import base64
import rsa


def str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)
    if len(b_str) < 162:
        return False
    hex_str = ''

    # 按位转换成16进制
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2
    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    print([modulus, exponent])
    return [modulus, exponent]


def to_para(key, message):
    ''':key：传入公钥，不带begin和end字符，一行传入即可'''
    key = str2key(key)
    message = str(message).encode()
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message, rsa_pubkey)
    b64str = str(base64.b64encode(crypto), encoding='utf-8')
    print(b64str)
    return b64str

def use_modulusAexponent(message):
    message = str(message).encode()
    modulus = int('BC087C7C00848CE8A349C9072C3229E0D595F817EDDE9ABF6FC72B41942A759E97956CE9CB7D1F2E99399EADBACC0531F16EAE8EFCB68553DE0E125B2231ED955ADBF5208E65DC804237C93EB23C83E7ECDA0B586ECF31839038EE6B640E0EEC5FF17D219FDEA33E730F287F0D384C74A53DFE1F91ACC63C7C92039A43AC6E97',16)
    exponent = int('10001',16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(message, rsa_pubkey)
    b64str = str(base64.b64encode(crypto), encoding='utf-8')
    print(b64str)
    return b64str

if __name__ == '__main__':
    # to_para(
    #     'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8asrfSaoOb4je+DSmKdriQJKWVJ2oDZrs3wi5W67m3LwTB9QVR+cE3XWU21Nx+YBxS0yun8wDcjgQvYt625ZCcgin2ro/eOkNyUOTBIbuj9CvMnhUYiR61lC1f1IGbrSYYimqBVSjpifVufxtx/I3exReZosTByYp4Xwpb1+WAQIDAQAB',
    #     '4ea5c508a6566e76240543f8feb06fd457777be39549c4016436afda65d2330e')
    use_modulusAexponent('12345678')


