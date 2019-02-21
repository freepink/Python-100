一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


count = 0
height =100
s_height = 0
for i in range(10):
    count +=1
    s_height += height
    height *= 0.5
    s_height += height
print(count,s_height-height,height)
