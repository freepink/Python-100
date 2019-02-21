#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

def f18(n,amt):
    sum = 0
    for i in range(1,amt+1):
        sum += int(str(n)*i)
        print(str(n)*i,end = "+")
    return sum
    
f18(2,5)
