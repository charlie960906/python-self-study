import json


def main():
    mydict = {
        'name': '老黃',
        'age': 16,
        'qq': 123456,
        'friends': ['阿Q', '桶面'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存完成!')


if __name__ == '__main__':
    main()