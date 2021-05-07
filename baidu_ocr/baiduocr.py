# encoding:utf-8

import requests
import base64

'''
通用文字识别（高精度版）
'''
request_url = ""  # 
request_url = ""  # 
request_url = ""  # 
request_url = ""  # 
request_url = ""  # 
request_url = ""  # 
request_url = ""  # 
# request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise/finance"  # IOCR财会版
# request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise"  # IOCR通用版API文档
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/intelligent_ocr"  # 智能结构化识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/facade"  # 门脸文字识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/lottery"  # 彩票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/seal"  # 印章识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/meter"  # 仪器仪表盘读数识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"  # 公式识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis"  # 试卷分析与识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_certificate"  # 车辆合格证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/used_vehicle_invoice"  # 二手车销售发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_invoice"  # 机动车销售发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vin_code"  # VIN码识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"  # 车牌识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license"  # 驾驶证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license"  # 行驶证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_detail"  # 医疗费用明细识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/insurance_documents"  # 保单识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_record"  # 病案首页识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_statement"  # 医疗费用结算单识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/medical_invoice"  # 医疗发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice_verification"  # 增值税发票验真
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/ferry_ticket"  # 船票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/receipt"  # 通用票据识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/toll_invoice"  # 过路过桥费发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/bus_ticket"  # 汽车票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/air_ticket"  # 飞机行程单识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/taxi_receipt"  # 出租车票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/train_ticket"  # 火车票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/invoice"  # 通用机打发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/quota_invoice"  # 定额发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"  # 增值税发票识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard_enc"  # 身份证识别（加密版）
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/multi_card_classify"  # 多卡证类别检测
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/birth_certificate"  # 出生医学证明识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/household_register"  # 户口本识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/taiwan_exitentrypermit"  # 台湾通行证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/HK_Macau_exitentrypermit"  # 港澳通行证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/passport"  # 护照识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_card"  # 名片识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"  # 营业执照识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard"  # 银行卡识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"  # 身份证识别
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/qrcode"  # 二维码识别
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
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"  # 通用文字识别（高精度含位置版）

# 二进制方式打开图片文件
f = open('/media/em/4.0T/chejian/image/lstm/保单车船税大写2020-11-14/JHS282_合计(人民币大写):检壹元贰角零分.jpg', 'rb')
# f = open('/media/em/4.0T/chejian/image/0206_D3Y696_LRH12R5D0C0000197___20201020___.jpg', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}
access_token = '24.85af79556c0fbbda80f622b38867c1d4.2592000.1622971446.282335-24123873'  # 所有接口的token zsy
# access_token = '24.210ec0bc6252a531e900a2f9dfaf34e2.2592000.1621940020.282335-24063854'  # 所有接口的token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
