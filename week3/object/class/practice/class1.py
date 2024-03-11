class Student(object):
    #__init__是一個特殊方法用在建立對象時進行初始化操作
    #通過這個方法我們可以為學生對象綁定name和age兩個數性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在學習%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age<18:
            print('%s只能觀看《海綿寶寶》.'% self.name)
        else:
            print('%s正在觀看Formula 1影集.'% self.name)


def main():
        stu1 = Student('宥鈞',16)
        stu1.study('python程式設計')
        stu1.watch_movie()
        stu2= Student('黃小鈞',20)
        stu2.study('AI白皮書')
        stu2.watch_movie()

if __name__ == '__main__':
        main()