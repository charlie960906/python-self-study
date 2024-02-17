import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=10):
    """生成指定長度的驗證碼
    :param code_len:驗證碼的長度(默認4個)
    :return: 由大小寫英文字母和數字組成的隨機驗證碼字串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))  

for _ in range(10):
    print(generate_code()) 