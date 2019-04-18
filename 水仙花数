1.将数字转换为字符串，用索引获取百位十位个位数字
for i in range(100,1000):
    s=str(i)
    if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
         print(i)
         
         
2.用算数运算获取百位十位个位数字
for i in range(100,1000):
    bai=i//100
    shi=i%100//10
    ge=i%10
    if i==bai**3+shi**3+ge**3:
        print(i)
        
        c语言中整数除以小数答案自动取整，除非预先定义为float且运算是＋.0答案为小数
        py中整数除以小数答案为小数要获得整数用整数除//
        
3.循环嵌套
for bai in range(1,10):
    for shi in range(10):
        for ge in range(10):
            x=bai*100+shi*10+ge
            if x==bai**3+shi**3+ge**3:
                print(x)
