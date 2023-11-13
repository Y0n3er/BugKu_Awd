import requests
from bs4 import BeautifulSoup

url = 'https://ctf.bugku.com/pvp/submit.html?token=2ed7f88432099a6dd582daf280e9dea5&flag='

with open('flag.txt', 'r') as file:
    for line in file:
        flag = line.strip()
        res = requests.get(url=url + flag)
        # print(res.status_code)
        # print(url + flag)
        soup = BeautifulSoup(res.text, 'html.parser')
        response=soup.find('h3',{'class':'m-t-30'}).text
        # print(response)
        if '恭喜您，Flag正确' in response:
            print('提交flag成功')
        else:
            print('提交flag失败')
