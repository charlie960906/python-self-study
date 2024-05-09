"""
驗證輸入使用者名稱和IG的ID是否有效並給出對應的提示訊息

要求:使用者名稱必須由字母、數字或底線構成且長度在6~20個字元之間,IG的ID是1~9的數字
"""
import re


def main():
     username = input('請輸入使用者名稱: ')
     qq = input('請輸入IG ID:')
     # match函數的第一個參數是正規表示式字串或正規表示式對象
     # 第二個參數是要跟正規表示式做符合的字串對象
     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
     if not m1:
         print('請輸入有效的使用者名稱.')
     m2 = re.match(r'^[1-9]\d{1,8}$', qq)
     if not m2:
         print('請輸入有效的ID.')
     if m1 and m2:
         print('你輸入的資訊是有效的!')


if __name__ == '__main__':
     main()