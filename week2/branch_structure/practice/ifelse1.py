"""
用戶身份驗證
"""

username=input('請輸入用戶名:')
password=input('請輸入密碼:')

if username=='charlie'and password=='1314520':
    print('驗證成功!')
else:
    print('驗證失敗!')
# 用户名是charlie且密码是1314520則驗證成功否则验证失败