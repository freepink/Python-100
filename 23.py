'''
题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
   '''
   
 def show(n):
    width = len("*"*n)
    for i in range(1,n+1,2):
        print("{:^{}}".format("*"*i,width))
    for i in range(n,0,-2):
        print("{:^{}}".format("*"*i,width))
