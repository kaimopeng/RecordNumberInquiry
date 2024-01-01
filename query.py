import requests
import re
from bs4 import BeautifulSoup
import time
import cv2
import base64
import os
import hashlib


def chinaz(company):
    try:
        burp0_url = "https://icp.chinaz.com/{}".format(company)
        html = requests.get(burp0_url).text
        soup = BeautifulSoup(html, 'html.parser')
        table = str(soup.find('font', id='permit'))
        beian1 = re.findall(r'(.ICP[备|证]\d{7,10}号)', table)
        beian2 = re.findall(r'(.B2-\d{8})', table)
        beian = beian1 + beian2
        ba = list(set(beian))
        if ba:
            bah = ''.join(ba)
            print(bah)
            list_beian.append(bah)
        else:
            return 0
    except:
        pass


def icplishi(company):
    try:
        burp0_url = "https://icplishi.com:443/company/{}/".format(company)
        burp0_headers = {
            "Sec-Ch-Ua": "\"Chromium\";v=\"117\", \"Not;A=Brand\";v=\"8\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"
        }
        html = requests.get(burp0_url, headers=burp0_headers).text
        soup = BeautifulSoup(html, 'html.parser')
        table = str(soup.find('td', rowspan='1'))
        beian1 = re.findall(r'(.ICP[备|证]\d{7,10}号)', table)
        beian2 = re.findall(r'(.B2-\d{8})', table)
        beian = beian1 + beian2
        ba = list(set(beian))
        if ba:
            bah = ''.join(ba)
            print(bah)
            list_beian.append(bah)
        else:
            return 0
    except:
        pass


def icp(company):
    try:
        burp0_url = "https://www.110icp.com:443/index.php?keyword={}&s=beian&c=search".format(
            company)
        html = requests.get(burp0_url).text
        soup = BeautifulSoup(html, 'html.parser')
        table = str(soup.find('table', class_='tftable'))
        beian1 = re.findall(r'(.ICP[备|证]\d{7,10}号)', table)
        beian2 = re.findall(r'(.B2-\d{8})', table)
        beian = beian1 + beian2
        ba = list(set(beian))
        if ba:
            bah = ''.join(ba)
            print(bah)
            list_beian.append(bah)
        else:
            return 0
    except:
        pass


def beianx(company):
    try:
        burp0_url = "https://www.beianx.cn:443/search/{}".format(company)
        burp0_cookies = {
            "__51huid__JfwpT3IBSwA9n8PZ":
            "a500d976-04bb-5a56-bd03-d8eb49e67781",
            "__51vcke__JfvlrnUmvss1wiTZ":
            "58630161-395e-534c-aa0f-a34d1aa4fce1",
            "__51vuft__JfvlrnUmvss1wiTZ": "1695104138587",
            "__51uvsct__JfvlrnUmvss1wiTZ": "5"
        }
        burp0_headers = {
            "Sec-Ch-Ua": "\"Chromium\";v=\"117\", \"Not;A=Brand\";v=\"8\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"
        }
        html = requests.get(burp0_url,
                            headers=burp0_headers,
                            cookies=burp0_cookies).text
        soup = BeautifulSoup(html, 'html.parser')
        table = str(
            soup.find('table',
                      class_='table table-sm table-bordered table-hover'))
        beian1 = re.findall(r'(.ICP[备|证]\d{7,10}号)', table)
        beian2 = re.findall(r'(.B2-\d{8})', table)
        beian = beian1 + beian2
        ba = list(set(beian))
        if ba:
            bah = ''.join(ba)
            print(bah)
            list_beian.append(bah)
        else:
            return 0
    except:
        pass


def tycbeian(company):
    try:
        burp0_url = "https://beian.tianyancha.com/search/{}".format(company)
        burp0_headers = {
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": "\"Chromium\";v=\"117\", \"Not;A=Brand\";v=\"8\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "close"
        }
        html = requests.get(burp0_url, headers=burp0_headers).text
        soup = BeautifulSoup(html, 'html.parser')
        table = str(soup.find('table', class_='table -ranking'))
        beian1 = re.findall(r'(.ICP[备|证]\d{7,10}号)', table)
        beian2 = re.findall(r'(.B2-\d{8})', table)
        beian = beian1 + beian2
        ba = list(set(beian))
        if ba:
            bah = ''.join(ba)
            print(bah)
            list_beian.append(bah)
        else:
            return 0
    except:
        pass


def get_cookies():
    cookie_headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'
    }
    err_num = 0
    while err_num < 3:
        try:
            cookie = requests.utils.dict_from_cookiejar(
                requests.get('https://beian.miit.gov.cn/',
                             headers=cookie_headers,
                             timeout=(3.06, 27)).cookies)['__jsluid_s']
            return cookie
        except:
            err_num += 1
            time.sleep(3)
    return -1


def get_sign(check_data, token):
    check_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/image/checkImage'
    base_header.update({
        'Content-Length': '60',
        'token': token,
        'Content-Type': 'application/json'
    })
    try:
        pic_sign = requests.post(check_url,
                                 json=check_data,
                                 headers=base_header,
                                 timeout=(3.06, 27)).json()
        sign = pic_sign['params']
    except:
        return -1
    return sign


def query_base(info):
    try:
        if info == "":
            raise ValueError("InputNone")
        info = re.sub("[^\\u4e00-\\u9fa5-A-Za-z0-9,-.()《》—（）]", "", info)
        input_zh = re.compile(u'[\u4e00-\u9fa5]')
        zh_match = input_zh.search(info)
        if zh_match:
            info_result = info
        else:
            input_url = re.compile(
                r'([^.]+)(?:\.(?:GOV\.cn|ORG\.cn|AC\.cn|MIL\.cn|NET\.cn|EDU\.cn|COM\.cn|BJ\.cn|TJ\.cn|SH\.cn|CQ\.cn|HE\.cn|SX\.cn|NM\.cn|LN\.cn|JL\.cn|HL\.cn|JS\.cn|ZJ\.cn|AH\.cn|FJ\.cn|JX\.cn|SD\.cn|HA\.cn|HB\.cn|HN\.cn|GD\.cn|GX\.cn|HI\.cn|SC\.cn|GZ\.cn|YN\.cn|XZ\.cn|SN\.cn|GS\.cn|QH\.cn|NX\.cn|XJ\.cn|TW\.cn|HK\.cn|MO\.cn|cn|REN|WANG|CITIC|TOP|SOHU|XIN|COM|NET|CLUB|XYZ|VIP|SITE|SHOP|INK|INFO|MOBI|RED|PRO|KIM|LTD|GROUP|BIZ|AUTO|LINK|WORK|LAW|BEER|STORE|TECH|FUN|ONLINE|ART|DESIGN|WIKI|LOVE|CENTER|VIDEO|SOCIAL|TEAM|SHOW|COOL|ZONE|WORLD|TODAY|CITY|CHAT|COMPANY|LIVE|FUND|GOLD|PLUS|GURU|RUN|PUB|EMAIL|LIFE|CO|FASHION|FIT|LUXE|YOGA|BAIDU|CLOUD|HOST|SPACE|PRESS|WEBSITE|ARCHI|ASIA|BIO|BLACK|BLUE|GREEN|LOTTO|ORGANIC|PET|PINK|POKER|PROMO|SKI|VOTE|VOTO|ICU|LA))',
                flags=re.IGNORECASE)
            info_result = input_url.search(info)
            if info_result is None:
                if info.split(".")[0] == "":
                    raise ValueError("OnlyDomainInput")
                raise ValueError("ValidType")
            else:
                info_result = info_result.group()
        info_data = {
            'pageNum': '1',
            'pageSize': '40',
            'serviceType': 1,
            'unitName': info_result
        }
        return info_data
    except:
        pass


def get_check_pic(token):
    url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/image/getCheckImage'
    base_header['Accept'] = 'application/json, text/plain, */*'
    base_header.update({'Content-Length': '0', 'token': token})
    try:
        p_request = requests.post(url=url,
                                  data='',
                                  headers=base_header,
                                  timeout=(3.06, 27)).json()
        p_uuid = p_request['params']['uuid']
        big_image = p_request['params']['bigImage']
        small_image = p_request['params']['smallImage']
    except:
        return -1
    with open('bigImage.jpg', 'wb') as f:
        f.write(base64.b64decode(big_image))
    with open('smallImage.jpg', 'wb') as f:
        f.write(base64.b64decode(small_image))
    background_image = cv2.imread('bigImage.jpg', cv2.COLOR_GRAY2RGB)
    fill_image = cv2.imread('smallImage.jpg', cv2.COLOR_GRAY2RGB)
    position_match = cv2.matchTemplate(background_image, fill_image,
                                       cv2.TM_CCOEFF_NORMED)
    max_loc = cv2.minMaxLoc(position_match)[3][0]
    mouse_length = max_loc + 1
    os.remove('bigImage.jpg')
    os.remove('smallImage.jpg')
    check_data = {'key': p_uuid, 'value': mouse_length}
    return check_data


def get_token():
    timeStamp = round(time.time() * 1000)
    authSecret = 'testtest' + str(timeStamp)
    authKey = hashlib.md5(authSecret.encode(encoding='UTF-8')).hexdigest()
    auth_data = {'authKey': authKey, 'timeStamp': timeStamp}
    url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/auth'
    try:
        t_response = requests.post(url=url,
                                   data=auth_data,
                                   headers=base_header,
                                   timeout=(3.06, 27)).json()
        token = t_response['params']['bussiness']
    except:
        return -1
    return token


def get_beian_info(info_data, p_uuid, token, sign):
    info_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/icpAbbreviateInfo/queryByCondition'
    base_header.update({
        'Content-Length': '78',
        'uuid': p_uuid,
        'token': token,
        'sign': sign
    })
    try:
        beian_info = requests.post(url=info_url,
                                   json=info_data,
                                   headers=base_header,
                                   timeout=(3.06, 27)).json()
        page_total = beian_info['params']['lastPage']
        end_row = beian_info['params']['endRow']
        info = info_data['unitName']
        listicp = []
        for i in range(0, page_total):
            for k in range(0, end_row + 1):
                info_base = beian_info['params']['list'][k]
                domain_licence = info_base['mainLicence']
                listicp.append(domain_licence)
            ba = list(set(listicp))
            for ic in ba:
                print(ic)
                list_beian.append(ic)
            info_data = {
                'pageNum': i + 2,
                'pageSize': '40',
                'serviceType': 1,
                'unitName': info
            }
            if beian_info['params']['isLastPage'] is True:
                break
            else:
                beian_info = requests.post(info_url,
                                           json=info_data,
                                           headers=base_header,
                                           timeout=(3.06, 27)).json()
                end_row = beian_info['params']['endRow']
                time.sleep(3)
    except:
        pass


if __name__ == '__main__':
    print("==============================================")
    print("=================燎众安全实验室==================")
    print("==============================================")
    list_beian = []
    with open('company.txt', 'r') as beiancofile:
        for companys in beiancofile:
            company = companys.strip()
            print(company)
            if chinaz(company):
                if icplishi(company):
                    if icp(company):
                        if beianx(company):
                            if tycbeian(company):
                                cookie = get_cookies()
                                info = query_base(company.strip())
                                try:
                                    global base_header
                                    base_header = {
                                        'User-Agent':
                                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
                                        'Origin': 'https://beian.miit.gov.cn',
                                        'Referer':
                                        'https://beian.miit.gov.cn/',
                                        'Cookie': f'__jsluid_s={cookie}'
                                    }
                                    if cookie != -1:
                                        token = get_token()
                                        if token != -1:
                                            check_data = get_check_pic(token)
                                            if check_data != -1:
                                                sign = get_sign(
                                                    check_data, token)
                                                p_uuid = check_data['key']
                                                if sign != -1:
                                                    get_beian_info(
                                                        info, p_uuid, token,
                                                        sign)
                                except:
                                    pass
    print(list_beian)
    file_domain = "beian.txt"
    furl = open(file_domain, "a")
    for add_domain in list(set(list_beian)):
        furl.write(add_domain + '\n')
    furl.close()
