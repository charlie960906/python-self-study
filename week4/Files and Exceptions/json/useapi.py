import requests
import json


def main():
    resp = requests.get('http://apis.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()

"""
API 由於我無法註冊申請因此目前抓不到
"""