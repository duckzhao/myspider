import re

headers= r"""
Host: s.taobao.com
Connection: keep-alive
Content-Length: 137188
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarykJ0gvWKZOiEjG5oA
Origin: https://s.taobao.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://s.taobao.com/search?q=&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&tfsid=O1CN01JHjFvr1DHWJUOdTvA_!!2-imgsearch.png&app=imgsearch
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: thw=cn; tracknick=zk15829954267; enc=UiWa%2BnYYbGsrNahrEyw2PXm9WWClbOzw4DEA%2BlsgfXRmomBYfMpyO2P%2FrLjr%2FWpYCJAHiGT55qV4YXHpiENbiQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; cna=QumqGPy4mBMCAW8SMo/marpS; xlly_s=1; mt=ci%3D-1_1; UM_distinctid=1782add3307385-0e98734a35a7c3-31346d-100200-1782add33083b2; t=0353c7ca26db9c3a31e076ae0f4c428d; sgcookie=E100Q9NL4fhn7k35iByOymqMmTEPlRrV3V64TacAIc0XUSHlW3kQQIRwK%2BPEJjQIiChiNlcweIpD7vpyOK0VbJl%2B9g%3D%3D; uc3=nk2=GcP56dA6BvIqYZ1hcA%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCuAotXdyxLb6O4Io%3D&id2=UUwZ%2FlwE8fR1rA%3D%3D; lgc=zk15829954267; uc4=id4=0%40U27Gj784Amd1rAz5DX0mQBwBsQ9L&nk4=0%40GwqygU4M%2FC9b8lmZKDhSYCxmm46a%2FESc; _cc_=V32FPkk%2Fhw%3D%3D; _tb_token_=e3875eaee3ee9; _m_h5_tk=512dfe116c778bf787a8f538878f1292_1615651184637; _m_h5_tk_enc=40ae910b7af65f8e2ef0d530bf120868; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=12f0457a35c111ae5bfec1770cd506f0; uc1=cookie14=Uoe1hx89CLvwJQ%3D%3D; tfstk=ctUGBdgwTlosD4m3VNg_1A1rQfjRaFAZC0nU8rcveuGZxFUZ_sA2Y3u10dMUIrKf.; l=eBTEx3wuOQrWp1cWBO5Blurza779XIOb8oVzaNbMiInca61CtF_9cNCQ9E9MSdtjgtfxUe-zLAUwVReXPM4dgfQTY8xrCyCoNY96-; isg=BLm5Vm1b_eS6PJ48eJ0thgkMyCWTxq14tPyI3tvvR-BfYtj0IBKTSG7k4GaUXkWw
"""

header = ''
for i in headers:
    if i == '\n':
        i = "',\n'"
    header += i
header=re.sub(': ',"': '",header)

ret=header[2:].replace(' ', '')+'\''
print(ret[:-4])