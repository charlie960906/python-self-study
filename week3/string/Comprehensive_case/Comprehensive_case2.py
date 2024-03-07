"""
《幸運的基督徒》
有15個基督徒和15個非基督徒在海上遇難
為了能讓一部分人活下来不得不將其中15個人扔到海里面去
有個人想了個辦法就是大家圍成一個圈
由某個人開始從1報數,報到9的人就丟到海裡
他後面的人接着從1开始報數,報到9的人繼續丟到海裡面,直到丟掉15個人。
由於上帝的保佑,15個基督徒都幸免於難,問這這些人最開始是怎麼站的,哪些位置是基督徒哪些位置是非基督徒?
"""

def main():
    persons = [True]*30
    counter,index,number=0,0,0
    while counter<15:
        if persons[index]:
            number +=1
            if number ==9:
                persons[index]=False
                counter +=1
                number = 0
        index +=1
        index %= 30
    for person in persons:
        print('基'if person else '非',end='')


if __name__ == '__main__':
    main()
    