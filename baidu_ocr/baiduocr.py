# encoding:utf-8

import requests
import base64

'''
通用文字识别（高精度版）
'''
request_url = ""
request_url = ""
request_url = ""
request_url = ""
request_url = ""
request_url = ""
request_url = ""
request_url = ""
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/qrcode"  # 二维码识别
# request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"  # 表格文字识别(异步接口)
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/form"  # 表格文字识别(同步接口) ??
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"  # 手写文字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"  # 数字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage_loc"  # 网络图片文字识别（含位置版）
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"  # 网络图片文字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis_office"  # 办公文档识别 ??
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"  # 通用文字识别（标准含位置版）
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"  # 通用文字识别（标准版）
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"  # 通用文字识别（高精度版）
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"  # 通用文字识别（高精度含位置版）

# 二进制方式打开图片文件
f = open('/media/em/4.0T/chejian/image/lstm/保单车船税大写2020-11-14/JHS282_合计(人民币大写):检壹元贰角零分.jpg', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}
# access_token = '24.2018b6e872b97c5f3532ab4d62f70713.2592000.1621939560.282335-11271251'  # OCR
access_token = '24.210ec0bc6252a531e900a2f9dfaf34e2.2592000.1621940020.282335-24063854'  # 所有接口的token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
