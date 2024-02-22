import os
import time


def main():
    content='HYJdevelop歡迎你'
    while True:
        #清理螢幕的輸出
        os.system('cls') #os.system('clear)
        print(content)
        #暫停200毫秒
        time.sleep(0.2)
        content = content[1:]+content[0]

if __name__ == '__main__':
    main()