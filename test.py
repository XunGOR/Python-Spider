import requests
import re


def getHTMLTest(url):
    try:  # cookie的值为自己登录淘宝后，输入搜索内容后的cookie

        cookie = 'cna=TD1lFxlbUWwCAXFvFF9CSHsh; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; t=b8d4fb1c9901bf6f7421aacd9b002277; \
        sgcookie=E100KNHQ0Kl64K7pCzAJJRlDDdl6JGdhiwd8MhuPQeUDQ2OCfIHdJkPa4RjmuXm3dIkWhCs0YOZQ8M5oVUUGwp3qfA%3D%3D; \
        uc3=id2=UUjUL0ht5PFa4A%3D%3D&nk2=G5VVHYC%2F&vt3=F8dCufJL%2FWgRlvCWCxM%3D&lg2=W5iHLLyFOGW7aA%3D%3D; lgc=xungor; \
        uc4=id4=0%40U2o28nfSE3FbstBMXYB0PRpEGRSY&nk4=0%40GSaxK2IgTnqTnfAuiO4Zx%2Fw%3D; tracknick=xungor; \
        _cc_=VFC%2FuZ9ajQ%3D%3D; enc=QmUDEig69WgITfgeUa21ubx37dysZzgRQOMQzS0oSv5CSW1Kj3fJPsp8y%2BIOGUvguqz4CKDnnlz%2FSSKtKdk9SQ%3D%3D; \
        mt=ci=-1_0; _tb_token_=313e73fbeab77; xlly_s=1; v=0; birthday_displayed=1; alitrackid=www.taobao.com; \
        lastalitrackid=www.taobao.com; cookie2=77701d3b0e822a7c2c89360dbeef339e; JSESSIONID=60E49332C11381AE7C95513FF1A200FA; \
        tfstk=cndOBN4zMDmguT_pzdH3Ga28q63hZRiAAPs0M4MTYyoUTMVAiYAkwLA-CZ_xj2C..; \
        l=eBE6RpgqOOu1w9RBBOfwourza77OSIRAguPzaNbMiOCP_d1p5X5VWZ7DCN89C3GVh622R3-dCUULBeYBqIv4n5U62j-la_kmn; \
        uc1=cookie14=Uoe0aDmc9B3Ieg%3D%3D; _m_h5_tk=68efd20de9f3374e84e51b1c5992b3d1_1605603976118; \
        _m_h5_tk_enc=129c586beaa3fac04742ce1aba835be7; isg=BKWlmgeJFhd4bHL96sart_iitGHf4ll0MuPek6eKy1zrvsUwbzAsRDNfTCLIvnEs'

        r = requests.get(url, headers={'cookie' : cookie}, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  # eval函数可以将获得的字符串的最外层的单引号或者双引号去掉
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = input("请输入要查找的商品名称: ")
    print("你输入的商品为: " , goods)
    print("正在查找....")
    print("以下为查找到的商品详情: ")
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLTest(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
