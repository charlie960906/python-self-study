"""
某公司有三種類型的員工 分別是部門經理、程式設計師和銷售員
需要設計一個工資結算系統 根據提供的員工資訊來計算月薪
部門經理的月薪是每月固定15,000元
程式設計師的月薪以本月工作時間計算 每小時150元
銷售員的月薪是1,200元的底薪加上銷售額5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
     """員工"""

     def __init__(self, name):
         """
         初始化方法

         :param name: 姓名
         """
         self._name = name

     @property
     def name(self):
         return self._name

     @abstractmethod
     def get_salary(self):
         """
         獲得月薪

         :return: 月薪
         """
         pass


class Manager(Employee):
     """部門經理"""

     def get_salary(self):
         return 15000.0


class Programmer(Employee):
     """程式設計師"""

     def __init__(self, name, working_hour=0):
         super().__init__(name)
         self._working_hour = working_hour

     @property
     def working_hour(self):
         return self._working_hour

     @working_hour.setter
     def working_hour(self, working_hour):
         self._working_hour = working_hour if working_hour > 0 else 0

     def get_salary(self):
         return 150.0 * self._working_hour


class Salesman(Employee):
     """銷售員"""

     def __init__(self, name, sales=0):
         super().__init__(name)
         self._sales = sales

     @property
     def sales(self):
         return self._sales

     @sales.setter
     def sales(self, sales):
         self._sales = sales if sales > 0 else 0

     def get_salary(self):
         return 1200.0 + self._sales * 0.05


def main():
     emps = [
         Manager('大大'), Programmer('中中'),
         Manager('小小'), Salesman('平平'),
         Salesman('丁丁'), Programmer('琪琪'),
         Programmer('噹噹')
     ]
     for emp in emps:
         if isinstance(emp, Programmer):
             emp.working_hour = int(input('請輸入%s本月工作時間: ' % emp.name))
         elif isinstance(emp, Salesman):
             emp.sales = float(input('請輸入%s本月銷售額: ' % emp.name))
         # 同樣是接收get_salary這個訊息但是不同的員工表現出了不同的行為(多型)
         print('%s本月薪資為: %s元' %
               (emp.name, emp.get_salary()))


if __name__ == '__main__':
     main()