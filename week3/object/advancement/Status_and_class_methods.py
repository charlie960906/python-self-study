from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c =map(int,input('a=,b=,c=').split())
    #靜態方式和類方式是通過給類發訊息來調用
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        #可以通過給類發訊息來調用對象但是傳入接收消息的對象作參數
        #print(Triangle(perimenter(t)))
        print(t.area())
       #print(trangle.area(t))
    else:
        print('無法構成三角形.')


if __name__ == '__main__':
    main()    