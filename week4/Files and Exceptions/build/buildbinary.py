def main():
    try:
        with open('good.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('棒棒.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件無法打開.')
    except IOError as e:
        print('讀寫文件時出現錯誤.')
    print('程式執行結束.')


if __name__ == '__main__':
    main()