'''
from os.path import splitext

def get_suffix(filename,ignore_dot=True):
    return splitex(filename)[1][1:]
'''

def get_suffix(filename,ignore_dot=True):
    """獲取程式的後綴名
    
    :param filename:文件名
    :param ignore_dote:是否忽略後綴名前面的點
    :return: 文件的後綴名
    """
    #從字符串中逆向查找.出現的位址
    pos = filename.rfind('.')
    #通過切片操片從文件名中取出後綴名
    if pos<=0:
        return ''
    return filename[pos+1:] if ignore_dot else filename[pos:]
print(get_suffix('readme.txt')) #txt
print(get_suffix('readme.text.md')) #md
print(get_suffix('.readme'))
print(get_suffix('readme.'))
print(get_suffix('readme'))