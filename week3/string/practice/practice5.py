def is_leap_year(year):
    """
    判斷閏年
    """
    return year%4==0 and year%100!=0 or year%400==0

def which_day(year,month,date):
    """
    計算一年的第幾天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total=0
    for index in range(month-1):
        total+=days_of_month[index]
    return total+date

def main():
    print(which_day(2007,9,6))
    print(which_day(2024,3,6))
    print(which_day(2022,1,1))
    print(which_day(1234,5,6))

if __name__=='__main__':
    main()
