#该脚本能探测存活同时可以将存活的IP直接写入到ip.txt文件中
import pythonping
from concurrent.futures import ThreadPoolExecutor

def get_ip(ip):
    res = pythonping.ping(ip)
    if "Reply" in str(res):
        print(ip + " 是存活地址")
        with open('ip.txt','a') as f:
            f.write(ip + '\n')

ip = []
for num in range(1,255):
    ip.append("192-168-1-" + str(num) + ".pvp3474.bugku.cn")
    # ip.append("192.168.1." + str(num))
with ThreadPoolExecutor(max_workers=100) as executor:
    result = executor.map(get_ip,ip)