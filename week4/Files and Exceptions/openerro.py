def main():
    f = None
    try:
        f = open('早安.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('無法打開指定文件!')
    except LookupError:
        print('指定到未知編碼!')
    except UnicodeDecodeError:
        print('解析錯誤!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
