class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age=age

    #:訪問器 - getter方式
    @property
    def name(self):
            return self._name
        
    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self,age):
        self._age = age


    def play(self):
        if self._age <= 16:
            print('%s正在玩switch.'% self._name) 
        else:
            print('%s正在玩xbox.'%self._name)


def main():
     person = Person('黃小鈞',16)
     person.play()
     person.age =20
     person.play()

    
if __name__ =='__main__':
     main()