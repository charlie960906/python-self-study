def is_prime(num: int)->bool:
    """判斷一個正整數是不是質數

    :param num: 正整數
    :return: 如果是質數回傳True,否則回傳False
    """

    for i in range(2,int(num **0.5)+1):
        if num%i ==0:
            return False
        return num !=i
    
if is_prime(int(input("輸入一個數字:")))==True:
    print("是質數")

else:
    print("不是質數")
