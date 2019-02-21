'''26.题目：利用递归方法求5!。'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n* fact(n-1)
        
facta(5)
