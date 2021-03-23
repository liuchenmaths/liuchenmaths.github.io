import os
import time

content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
while True:
    os.system('clear')
    print(content)
    time.sleep(0.1)
    content = content[1:] + content[0]