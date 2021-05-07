# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vSoXO7SUiMaOsKC5GFYeIRz1&client_secret=uTx9mLjaGh5Dda9X3yESYER9vFXONkfA'  # 只OCR接口
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=V3YieMZuZsxzmPPsX689WZr7&client_secret=HGhon7Ol9eieLAI9vMRPVnUCATMfsNVZ'  # 所有接口
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=8ehGhuwMVw18LYb9CzOYpsZV&client_secret=0g3g2iuwGwCgCcZQpfxndkVpxnG0OPlj'  # 所有接口 zsy
response = requests.get(host)
if response:
    print(response.json())