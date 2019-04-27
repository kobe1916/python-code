#瓶盖换可乐问题
n = int(input("你有多少可乐?"))      #可乐数
k = int(input("兑换一瓶可乐所需瓶盖数"))     #兑换所需瓶盖数
x = n             #现有瓶盖数
while x >=k:  
    x -= k        #兑换后瓶盖数
    n += 1        #兑换一次可乐数加一
    x += 1        #兑换一次瓶盖数加一
print(n)



#N位数水仙花问题
N = int(input("cdfskjcs"))       #获得输入
if N>=3 and N<= 7:                #判断
    for n in range(10**(N-1),10**N):     #遍历
        sum = 0    
        s = str(n)              
        for i in range(N):         #遍历位数
            sum += int(s[i])**N    #运算
            if sum == n:           #判定
                print(n)
else:
    print("shu ru cuo wu")


#判断素数问题
m = int(input("fds"))
if m >1:
    for i in range(2,m):
        if m%i == 0:
            print("%d不是素数"%m)
            break
        else:
            print("%d是素数"%m)

