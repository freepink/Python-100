'''25.题目：求1+2!+3!+...+20!的和。'''

fact = 1
sum_fact =0
for i in range(1,21):
    fact *= i
    sum_fact += fact
print(sum_fact)
